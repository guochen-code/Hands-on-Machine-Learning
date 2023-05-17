import os

lst=['numpy','pandas']

for i in lst:
    source_path = f'/Users/chenguo/Full Stack/REST API/dependency_folder/{i}'
    target_path = f'/Users/chenguo/Full Stack/REST API/dist/main002/{i}'
    try:
        os.symlink(source_path, target_path, target_is_directory=True)
        print(f"Symbolic link created from {source_path} to {target_path}")
    except OSError as e:
        print(f"Failed to create symbolic link: {e}")
    except Exception as err:
        print('******error:',err)


import say_hello

import pandas as pd

df = pd.DataFrame()
say_hello.say_hello()
print('******** done ************')

---------------------------------------------------------------------------------------------------------------------
pyinstaller --onedir main002.py


---------------------------------------------------------------------------------------------------------------------
import os

parent_folder = '/Users/chenguo/Full Stack/REST API/dependency_folder'  # Replace with your parent folder path

# Get a list of all entries (files and folders) in the parent folder
entries = os.listdir(parent_folder)

# Filter the entries to include only folders
folders = [entry for entry in entries if os.path.isdir(os.path.join(parent_folder, entry))]

# Print the list of folders
for folder in folders:
    print(folder)


###############################################################################################################

import os

parent_folder = '/Users/chenguo/Full Stack/REST API/dependency_folder' 

# Get a list of all folders in the parent folder
folders = [folder for folder in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, folder))]

# Filter out dist-info folders
folders = [folder for folder in folders if not folder.endswith('.dist-info')]

# Print the remaining folders
for folder in folders:
    print(folder)

