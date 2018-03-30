import os

#Each folder means a certain website
def create_project_dir(directory):
    dir = './Websites' + directory
    if not os.path.exists(dir):
        print('Creating a new project for ' + dir)
        os.makedirs(dir)


# Create queue and craled for each website
def create_queue_crawled(project_name, base_url):
    dir = './Websites/'
    queue = dir + project_name + '/queue.txt'
    crawled = dir + project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        print('Creating queue file ', queue)
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        print('Creating crawled file ', crawled)
        write_file(crawled, '')

# writes data into a txt format
def write_file(path, data):
    with open(path, 'w') as data_file:
        data_file.write(data)

create_queue_crawled('9gag', 'https://9gag.com/')
