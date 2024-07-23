#!/usr/bin/env python3
import subprocess
import shutil

# inputs
parameter = "capacity"
mid = " "
values = list(range(20, 180, 20))

formatted_parameter = parameter.replace(' ', '_')

for v in values:
    # generate config file
    config = f"{formatted_parameter}_{v}.cfg"
    shutil.copy('cacti_sweeps/sweep.cfg', config)

    f = open(config, 'a')
    f.write(f"-{parameter}{mid}{v}")
    f.close()

    # run config file
    command = f"./runfile.sh {config}"
    try: 
        subprocess.run(command, shell=True, executable="/bin/bash")
        print(f"ran {command}")
    except:
        print(f"failed {command}")

# sort output to a directory, generate csv file, produce graph of output
subprocess.run(f"./sort.sh {formatted_parameter}", shell=True, executable="/bin/bash")
subprocess.call(f"./gen_csv.py {formatted_parameter}", shell=True)

print("done")
