#!/usr/bin/env bash
config=$1
echo "config: $config" || exit
cd cacti || exit
./cacti -infile "../$config" > "${config#*/}".txt || exit
mv ./*.txt ..