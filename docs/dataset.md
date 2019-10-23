# ***Setup/Dataset Generation***

Dataset generation is done in the following steps, all in `setup.sh`:

1. Download and unpack 1gram data from Google.
2. Convert the 1gram data to word,frequency CSV for each specified year.
    - Loop through each line in each file and:
        - If the line contains data for the specified year and the word (stripped of POS information) is the correct length, increment or initialize its value in a dictionary. This is done because data for a single word may be on multiple lines.
    - Write the dictionary to a CSV
3. Filter the created CSV by copying all lines where the frequency is over 800 to a new CSV. This value is selected to keep approximately the top 10% of words.
