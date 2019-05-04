#!/usr/bin/env bash

./download1gramData.sh
echo "Converting data to word,score csv..."
./rawToCsv.py > ../data/csv/fitness.csv