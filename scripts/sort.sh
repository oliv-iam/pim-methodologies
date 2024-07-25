#!/usr/bin/env bash
direc="$1"
mkdir "cacti_sweeps/$direc" || direc+=1 && mkdir "cacti_sweeps/$direc"
echo "new directory: cacti_sweeps/$direc"
cd "cacti_sweeps" || exit
mkdir "$direc"/configs && mkdir "$direc"/results && mkdir "$direc"/output
mv ../*.cfg "$direc"/configs
mv ../*.txt "$direc"/results
mv ../*.out "$direc"/output 
echo 'sorted'
