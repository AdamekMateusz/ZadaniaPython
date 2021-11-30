import os

current_path = os.getcwd()
list_of_file = os.listdir(current_path)

changing_name = []

for file in list_of_file:
    if file.endswith('.jpg'):
        changing_name.append(os.rename(file,file[:-3]+'png'))

