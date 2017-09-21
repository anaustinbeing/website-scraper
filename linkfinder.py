from bs4 import BeautifulSoup
import urlparse

class LinkFinder:

    def __init__(self, base_url, page_url):
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def find_links(self, string):
        page = BeautifulSoup(string, "lxml")
        for links in page.find_all('a'):
            url = urlparse.urljoin(self.base_url, links.get('href'))
            self.links.add(url)

    def page_links(self):
        return self.links

