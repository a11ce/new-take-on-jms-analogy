#!/usr/bin/env bash

./download1gramData.sh
echo "Converting data to word,score csv... (this can take about 20 minutes)"
./rawToCsv.py > ../data/csv/fitness.csv