import os

# Each website you scroll is a separate project
def create_project_dir(directory):
    if not os. path.exists(directory):
        print 'Creating project', directory
        os.makedirs(directory)


# Creating queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Creating a new file
def write_file(path, data):
    with open(path, 'w')as f:
        f.write(data)
        f.close()


# Add data on to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'r') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)