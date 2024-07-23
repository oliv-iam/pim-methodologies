#!/usr/bin/env bash
mkdir cacti_sweeps/"$1" && cd cacti_sweeps/"$1" || exit
mkdir configs && mv ~/pim/*.cfg configs
mkdir results && mv ~/pim/*.txt results
mkdir output && mv ~/pim/*.out output
echo 'sorted'
