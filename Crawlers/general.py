import os

# Crawl to a website and create a file for it
def create_project_dir(directory):
    dir = './Websites/' + directory
    if not os.path.exists(dir):
        print('Creating a new project for ' + dir)
        os.makedirs(dir)


# Create queue and crawled file for each website inside the Websites dir
def create_data_file(project_name, base_url):
    dir = './Websites/'
    queue = dir + project_name + '/queue.txt'
    crawled = dir + project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        print('Creating queue file ', queue)
        write_data(queue, base_url)
    if not os.path.isfile(crawled):
        print('Creating crawled file ', crawled)
        write_data(crawled, '')

# Writes data into a queue and crawled file
def write_data(path, data):
    with open(path, 'w') as data_file:
        data_file.write(data)


# Add links to the queue and crawled data_file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the contents of a file
def delete_data(path):
    with open(path, 'w'):
        pass

# Converts the file to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.strip('\n'))
        return results

# Convert the set to file
def set_to_file(links, file):
    delete_data(file)
    for link in sorted(links):
        append_to_file(file, link)
