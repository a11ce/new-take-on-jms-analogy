#!/usr/bin/env bash
for x in {a..z}
do
    wget "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-$x.gz" \
    -P ../data/raw1ngram/ wget  -q --show-progress -c   
done