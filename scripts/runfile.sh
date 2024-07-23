#!/usr/bin/env bash
cd cacti || exit
./cacti -infile "../${1}" > "${1#*/}".txt && mv ./*.txt ..