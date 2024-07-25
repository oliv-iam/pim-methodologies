#!/usr/bin/env python3
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import re
import os
import sys

if len(sys.argv) != 3:
    sys.exit(1)

# reformat dataframe (column names, sorting, types)
def neat(df, type):
    to_return = df
    # add units to column names
    if type == '3D':
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

    # strip unwanted characters from columns
    for col in to_return.columns:
        if col == 'Name':
            to_return['Name'] = to_return['Name'].replace(r".*_", '', regex=True).replace(r"\.cfg\.txt", '', regex=True) # strip string
            try:
                to_return['Name'] = to_return['Name'].astype(float)
            except:
                continue
        if col == 'DRAM core area (mm2)' or col == 'DRAM area per die (mm2)' or col == 'TSV area overhead (mm2)':
            to_return[col] = to_return[col].replace("mm2", "", regex=True)
        else:
            to_return[col] = to_return[col].replace("[a-z_A-Z%]", "", regex=True)
            to_return[col].astype(float)

    to_return = to_return.sort_values(by='Name', ignore_index=True)
    
    return to_return

# take in type as an argument
type = sys.argv[1]

# take in csv file as an argument, load to dataframe
csv = sys.argv[2]
df = neat(pd.read_csv(csv), type)
cols = df.columns

# plot on a r x c grid
if type == 'cache': # 14 columns
    tot_r = 3
    tot_c = 5
    # max = 14
elif type == '3D': # 18 columns
    tot_r = 3
    tot_c = 6
    # max = 18
elif type == 'simple_cache': # 4 data columns
    tot_r = 2
    tot_c = 2

fig, axs = plt.subplots(tot_r, tot_c, figsize=(14, 7))
fig.suptitle(csv.replace('_', ' ').replace('.csv', ''))

#FIXME: adjust to stop after columns end
c_i = 1
for r in range(0, tot_r):
    for c in range(0, tot_c):
        try:
            print(df['Name'])
            print(df[cols[c_i]])
            axs[r][c].scatter('Name', cols[c_i], data=df)
            axs[r][c].set_title(cols[c_i])
            # axs[r][c].set_yticks([]) - erase y ticks
            # axs[r][c].set_title(re.sub(r"\(.*\)", "", cols[c_i])) - filter units out of title
        except:
            print('incomplete grid')
        c_i += 1
        
fig.tight_layout()
plt.show()
