import os
import shutil
import glob
import pandas as pd

extension = 'csv'


def getDataFolders():
    all_folders = [name for name in os.listdir(
        os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), name))]
    print(all_folders)
    unused_folders = ['.ipynb_checkpoints', '.vscode',
                      'join-csv.py', '.git', "00000000 - Campaña"]
    folders = [item for item in all_folders if item not in unused_folders]
    return folders


dirs = getDataFolders()
# print(os.getcwd())

# print(dirs)
for dir in dirs:
    all_files = [i for i in glob.glob(os.getcwd()+"\\"+dir+"\\"+"*.csv")]
    print(all_files)
    print("--")

    combined_csv = pd.concat(
        [pd.read_csv(f, encoding='UTF-16 LE') for f in all_files])
    combined_csv.to_csv(os.path.join(os.getcwd(), "..", "Email Send Analisys",
                        "data", dir+".csv"), index=False, encoding="utf-8")

# for file in all_filenames:
#     if file != filename:
#         if not os.path.exists(directory):
#             os.makedirs(directory)

#         if os.path.exists(directory):
#             shutil.move(file, directory)

# if os.path.exists(directory):
#   shutil.move(directory, '../Email Reports/'+directory)

# if os.path.exists(filename):
#   shutil.move(filename,'../Email Send Analisys/data/'+filename)
