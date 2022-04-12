import os
import shutil
import glob
import pandas as pd

extension = 'csv'
directory = ''
filename = directory + ".csv"

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

combined_csv = pd.concat([pd.read_csv(f, encoding='UTF-16 LE')
                          for f in all_filenames])
combined_csv.to_csv(filename, index=False, encoding="utf-8")

for file in all_filenames:
    if file != filename:
        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.exists(directory):
            shutil.move(file, directory)

if os.path.exists(directory):
    shutil.move(directory, '../Email Reports/'+directory)

if os.path.exists(filename):
    shutil.move(filename, '../Email Send Analisys/data/'+filename)
