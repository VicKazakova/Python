import os
project_name = 'my_project'
f_names = ['settings', 'mainapp', 'adminapp', 'authapp']


def create_project(name, folder):
    dir_path = os.path.join(name, folder)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


create_project(project_name, f_names[0])
create_project(project_name, f_names[1])
create_project(project_name, f_names[2])
create_project(project_name, f_names[3])
