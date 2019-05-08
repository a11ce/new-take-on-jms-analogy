#!/usr/bin/env bash

let YEARTOSAVE="1950"

./download1gramData.sh
echo "Converting data to word,score csv... (this can take about 20 minutes)"
./rawToCsv.py $YEARTOSAVE  > ../data/csv/$YEARTOSAVE.csv