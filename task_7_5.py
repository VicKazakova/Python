import os
import json


def get_dir_size(directory):
    future_files = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            file_format = file.rsplit('.', maxsplit=1)[-1].lower()
            if file_size in future_files:
                future_files[file_size][0] += 1
                if file_format not in future_files[file_size][1]:
                    future_files[file_size][1].append(file_format)
            else:
                future_files[file_size] = [1, [file_format]]
    final_result = {}
    for file_size, data_list in sorted(future_files.items()):
        final_result[file_size] = tuple(data_list)
        print(f'{file_size}: {data_list}')
    dir_name = os.path.dirname(__file__).split('\\')[-1] + '_summary.json'
    with open(dir_name, 'w', encoding='utf-8') as f:
        json.dump(final_result, f, ensure_ascii=False)


get_dir_size('my_project')
