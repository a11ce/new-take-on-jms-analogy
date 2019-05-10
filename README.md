# Unofficial code related to A New Take on John Maynard Smith's Concept of Protein Space for Understanding Molecular Evolution

## How to use

## Setup

- Edit line 3 of `setup/setup.sh` to include the datasets you want to generate.
- Run `setup/setup.sh`

(Rest of how to use to come)

## File summary

- `findMutations.py`: Finds possible mutations for a word.
- `randomPath.py`: Finds a random possible mutation path from a starting word.
- `findPath.py`: Finds a mutation path between two words.
- `loadDict.py`: Helper to load csv data as a dict.

### setup/

- `setup.sh`: Runs the following two commands, and saves final csv to `data/csv/`
---
- `download1gramData.sh`: Downloads and unzips all 1grams from Google Books and saves to `data/raw_ngram/`.
- `rawToCsv.py`: Converts unzipped 1gram data to word,frequency csv.

### data/ (after setup)

- `raw1gram/`: 1gram files as downloaded from Google Books.
- `csv/`: word,frequency csv files.