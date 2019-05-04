#!/usr/bin/env bash
for x in {a..z}
do
    echo "Downloading $x..."
    wget "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-$x.gz" \
    -P ../data/raw1gram/ -q  --show-progress -c   
    echo "Unzipping $x..."
    gzip -d --keep "../data/raw1gram/googlebooks-eng-all-1gram-20120701-$x" \
     
done
