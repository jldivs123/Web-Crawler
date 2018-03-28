import os

#Each folder means a certain website
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating a new project for ' + directory)
        os.makedirs(directory)

create_project_dir('9gag')
