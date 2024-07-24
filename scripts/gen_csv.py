#!/usr/bin/env python3
import shutil
import os
import sys

if len(sys.argv) != 3:
    print('provide type and parameter')
    sys.exit(1)

directory = f"cacti_sweeps/{sys.argv[2]}/results"
new_csv = f"{sys.argv[2]}.csv"

type = sys.argv[1] # 'cache', '3D', 'RAM'
if type == 'cache':
    lo = 57
    hi = 69
elif type == '3D':
    lo = 61
    hi = 83

csv = shutil.copy(f"cacti_sweeps/{type}_headings.csv", new_csv)
f = open(new_csv, 'a')

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    results = open(file, 'r')
    lines = results.readlines()
    lines = list(map(lambda x: x.rstrip(), lines))

    f.write("\n" + filename)
    for i in range(lo, hi):
        if lines[i][0] == 't':
            print(filename + 'produced at least one incorrect row')
            break
        if i == 68: # split cache height x cache width
            f.write(', ' + lines[i][lines[i].index(':')+2:lines[i].index(':')+10])
            f.write(', ' + lines[i][lines[i].index(':')+13:])
            break
        if lines[i][0] not in ['T', 'A', 'P']:
            f.write(', ' + lines[i][lines[i].index(':')+2:])
    
f.close()
print("csv generated")