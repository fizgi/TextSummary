""" A Python program that prompts the user for
    the name of a file with an arbitrary ASCII document,
    reads the file, and prints a summary of the words in the document.

    author: fizgi
    date: 01-Apr-2020
    python: v3.8.2
"""

import os
from typing import IO, DefaultDict
from collections import defaultdict
from string import punctuation
from operator import itemgetter


file_name: str = input("Enter the file name: ")

try:  # to open the file
    path: IO = open(file_name, mode="r", encoding="utf-8")
except FileNotFoundError:
    print(f"File {file_name} is not found")
else:
    with path:  # close path after opening
        if os.path.getsize(file_name) == 0:
            print(f"'{file_name}' is empty. No calculations were made.")
        else:
            total_words = 0  # total word counter
            character_freq: DefaultDict[str, int] = defaultdict(int)  # container for characters
            distinct_words: DefaultDict[str, int] = defaultdict(int)  # container for words

            punc_translator = str.maketrans({key: None for key in punctuation})

            for line in path:
                if line == "\n": continue  # skip empty lines

                # lower and clean the line from unnecessary characters
                clean_string = line.strip("\n").lower().translate(punc_translator)

                for word in clean_string.split(" "):  # separate each word by ' '
                    total_words += 1  # increase total word count
                    distinct_words[word] += 1  # increase distinct word count
                    for char in word:
                        if char.isalnum():  # check the character if it is alpha-numeric
                            character_freq[char] += 1  # then count

            sorted_distinct_words = sorted(distinct_words.items(), key=itemgetter(1), reverse=True)
            sorted_character_freq = sorted(character_freq.items(), key=itemgetter(1), reverse=True)

            print(f"Total words: {total_words}\nTotal distinct words: {len(sorted_distinct_words)}")
            print("Top 25 most frequent words:", [(word, '{:,}'.format(count)) for (word, count) in sorted_distinct_words[:25]])
            print("Character frequency:", [(char, '{:,}'.format(count)) for (char, count) in sorted_character_freq])
