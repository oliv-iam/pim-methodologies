#!/usr/bin/env bash
category=$1
mv ./*.csv "results/$category" 
cd cacti_sweeps || exit
ls -d -- */ | grep -v '_sweeps' | xargs -I {} mv {} "$category"
