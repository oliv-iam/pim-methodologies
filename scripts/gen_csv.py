#!/usr/bin/env python3
import shutil
import os
import sys

directory = f"cacti_sweeps/{sys.argv[1]}/results"
new_csv = f"{sys.argv[1]}.csv"

csv = shutil.copy('cacti_sweeps/headings.csv', new_csv)
f = open(new_csv, 'a')

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    results = open(file, 'r')
    lines = results.readlines()
    lines = list(map(lambda x: x.rstrip(), lines))

    f.write("\n" + filename)
    for i in range(61, 83):
        if lines[i][0] == 't':
            print(filename + 'produced at least one incorrect row')
            break
        if lines[i][0] not in ['T', 'A', 'P']:
            f.write(', ' + lines[i][lines[i].index(':')+2:])
    
f.close()
print("csv generated")