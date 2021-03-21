import os
from collections import defaultdict


def get_dir_size(directory):
    future_files = defaultdict(int)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            future_files[file_size] = future_files[file_size] + 1
    for file_size, files in sorted(future_files.items()):
        print(f'{file_size}: {files}')


get_dir_size('my_project_for_task_3')
get_dir_size('my_project')
