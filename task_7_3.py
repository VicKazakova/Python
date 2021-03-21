import shutil

initial_folder = 'my_project_for_task_3'
new_folder = 'templates'
try:
    shutil.copytree(initial_folder, new_folder)  # копируем все данные в корень папки
except FileExistsError:
    print('File exists')
else:
    print('copy: done')
try:
    shutil.move(new_folder, initial_folder)  # перемещаем внутрь проектной папки
except shutil.Error:
    print('Already moved')
else:
    print('move: done')
try:
    shutil.rmtree(new_folder)  # при повторном запуске снова создастся папка в корне, поэтому сносим ее, если она есть
except FileNotFoundError:
    pass
else:
    pass
