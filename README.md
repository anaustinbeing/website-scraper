# Web Scraper
Scrape any websites to retrieve all hyperlinks from it in a matter of seconds.
***************

This Webscraping program is written in **Python 2.7.11**. Basically, it scrapes any websites and outputs all the links that it finds. The set of programs that eases this task are called web crawlers or spiderbots or simply spiders. Using threading module of Python, multiple spiders can be used to crawl multiple links at a time. You can change the number of threads in main.py file which is set to 3 for now. *Pretty cool! It saves time.*


A Web crawler, sometimes called a spider, is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing (web spidering). - as described in 
[wikipedia](https://en.m.wikipedia.org/wiki/Web_crawler).

Follow the steps below:
* **Clone or download** all .py files.
   Make sure all .py files are in the **same** directory.
* **Run** main.py
* **Type** in the website address which you need to scrape.
   **The program will do the rest for you.**
   
   
  
 **You can increse the number of spiders crawling by increasing the NUMBER_OF_THREADS in main.py file.**
   *Just simple!*
   

After the program is run, a new folder named **theausome** is generated which contains two files: **crawled.txt** and **queue.txt**.

 * **crawled.txt** contains all links that are crawled.
 * **queue.txt** contains all links waiting to be crawled.
 
 *Feel free to modify.*
