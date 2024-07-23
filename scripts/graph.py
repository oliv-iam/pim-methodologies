#!/usr/bin/env python3
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import re
import os
import sys

"""
# load csv files to list
directory = sys.argv[1]
files = []
for filename in os.listdir(directory):
    if '.csv' in filename:
        files.append(os.path.join(directory, filename))
"""

# take in csv file as an argument
csv = sys.argv[1]
df = neat(pd.read_csv(csv))
cols = df.columns

# [adjust to accommodate other amounts of columns]
fig, axs = plt.subplots(3, 6, figsize=(14, 7))
fig.suptitle(csv.replace('_', ' ').replace('.csv', ''))

c_i = 1
for r in range(0, 3):
    for c in range (0, 6):
        try:
            axs[r][c].scatter('Name', cols[c_i], data=df)
            axs[r][c].set_yticks([])
            axs[r][c].set_title(re.sub(r"\(.*\)", "", cols[c_i]))
        except:
            print('oop')
        c_i += 1
        
fig.tight_layout()
plt.show()

# reformat dataframe (column names, sorting, types)
def neat(df):
    to_return = df.rename(columns={' t_RCD (Row to column command delay)': 't_RCD (Row to column command delay) (ns)',
                              ' t_RAS (Row access strobe latency)': 't_RAS (Row access strobe latency) (ns)', 
                              ' t_RC (Row cycle)': 't_RC (Row cycle) (ns)', ' t_CAS (Column access strobe latency)': 't_CAS (Column access strobe latency) (ns)',
                              ' t_RP (Row precharge latency)': 't_RP (Row precharge latency) (ns)',
                              ' t_RRD (Row activation to row activation delay)': 't_RRD (Row activation to row activation delay) (ns)',
                              ' Activation energy': 'Activation energy (nJ)', ' Read energy': 'Read energy (nJ)', ' Write energy': 'Write energy (nJ)',
                              ' Precharge energy': 'Precharge energy (nJ)', ' DRAM core area': 'DRAM core area (mm2)', 
                              ' DRAM area per die': 'DRAM area per die (mm2)', ' Area efficiency': 'Area efficiency (%)', ' DRAM die width': 'DRAM die width (mm)',
                              ' DRAM die height': 'DRAM die height (mm)', ' TSV area overhead': 'TSV area overhead (mm2)', ' TSV latency overhead': 'TSV latency overhead (ns)',
                              ' TSV energy overhead per access': 'TSV energy overhead per access (nJ)'})

    for col in to_return.columns:
        if col == 'DRAM core area (mm2)' or col == 'DRAM area per die (mm2)' or col == 'TSV area overhead (mm2)':
            to_return[col] = to_return[col].replace("mm2", "", regex=True)
        else:
            to_return[col] = to_return[col].replace("[a-z_A-Z%]", "", regex=True)
        if col == 'Name':
            to_return['Name'] = to_return['Name'].str.strip('.').astype(float)
            continue
        else:
            to_return[col].astype(float)
    to_return = to_return.sort_values(by='Name', ignore_index=True)
    
    return to_return