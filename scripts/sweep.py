#!/usr/bin/env python3
import subprocess
import shutil
import sys

# inputs
parameter = "dram_type"
mid = " "
values = ['DDR3', 'DDR4', 'LPDDR2', 'WideIO', 'Serial']
type = 'cache'

formatted_parameter = parameter.replace(' ', '_')

for v in values:
    # generate config file
    config = f"{formatted_parameter}_{v}.cfg"
    shutil.copy('cacti_sweeps/sweep.cfg', config)

    f = open(config, 'a')
    f.write(f"-{parameter}{mid}{v}")
    f.close()

    # run config file
    command = f"scripts/runfile.sh {config}"
    try: 
        p = subprocess.run(command, shell=True, executable="/bin/bash")
        # p.wait()
        print(f"ran {command}")
    except:
        print(f"failed {command}")
        sys.exit(1)

# sort output to a directory, generate csv file, produce graph of output
subprocess.run(f"scripts/sort.sh {formatted_parameter}", shell=True, executable="/bin/bash")
subprocess.call(f"scripts/gen_csv.py {type} {formatted_parameter}", shell=True)
subprocess.call(f"scripts/graph.py {type} {formatted_parameter}.csv", shell=True)

print("done")
