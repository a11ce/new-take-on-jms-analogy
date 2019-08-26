#!/usr/bin/env bash

declare -a YEARSTOSAVE=("2000" )

./download1gramData.sh

for i in ${YEARSTOSAVE[@]}; do
    echo "Converting data to word,score csv for $i... (this can take about 20 minutes)"
    ./rawToCsv.py $i  > ../data/csv/$i.csv
done

python3 makeFiltered.py 2000