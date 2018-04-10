from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:

    # Class variables are shared for all the class intances
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        dir = './Websites/'
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = dir + Spider.project_name + '/queue.txt'
        Spider.crawled_file = dir + Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider is on the move -- crawling: ', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_file(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' on the ' + page_url)
            print('Items on queue: ' + str(len(Spider.queue)) + ' | Items crawled: ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.fetch_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def fetch_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
            return finder.page_links()
        except Exception as e:
            print("Can not crawl page \n")
            print(str(e))
            return set()

    @staticmethod
    def add_links_to_queue(links):
        for link in links:
            if link in Spider.queue:
                continue
            if link in Spider.crawled:
                continue
            if Spider.domain_name not in link:
                continue
            Spider.queue.add(link)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
