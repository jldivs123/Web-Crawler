import threading
from queue import Queue
from spider import Spider
from general import *
from domain import *

# In python convention a variable with an ALL CAPITAL name suggests a constant
# Im using static values for now
PROJECT_NAME = 'www.pup.edu.ph'
HOMEPAGE = 'https://www.pup.edu.ph/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
print(str(get_domain_name(HOMEPAGE)))
