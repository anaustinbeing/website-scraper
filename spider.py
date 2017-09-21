import urllib
from linkfinder import LinkFinder
from general import *


class Spider:

    # Class variables (shared among all the spiders)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()           # Declaring an empty set for the waiting list
    crawled = set()         # Declaring an empty set for the crawled list

    # Initializing the variables
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)

    # Method to boot up the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # Method to crawl through a web page, get all the links and update the files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print '\n', thread_name, ' now crawling: ', page_url
            print '\nRemaining links: ', str(len(Spider.queue))
            print '\nCompleted: ', str(len(Spider.crawled))
            Spider.add_links_to_queue(Spider.get_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    # Method to get all the links in a web page
    @staticmethod
    def get_links(page_url):
        html_string = ''
        try:
            response = urllib.urlopen(page_url)
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.find_links(html_string)
            return finder.page_links()
        except:
            print 'Error crawling the page'
            return set()

    # Method to add the gathered links to the waiting list (queue)
    @staticmethod
    def add_links_to_queue(links):
        for link in links:
            if link not in Spider.crawled and link not in Spider.queue\
                    and Spider.domain_name in link:
                Spider.queue.add(link)

    # Method to update both queue file and crawled file
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
