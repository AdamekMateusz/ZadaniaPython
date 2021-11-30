import os

all_files = os.listdir('/dev')

all_files = [file for file in all_files if os.path.isfile(os.path.join('/dev',file))]
print('Number of file: ', len(all_files))
