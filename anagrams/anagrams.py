from typing import List, Dict, DefaultDict
from collections import defaultdict


def load_words() -> List[str]:
    with open("wordlist.txt", encoding="ISO-8859-1") as file:
        s = file.read()
        return s.split("\n")


def add_character_to_dict(letter: chr, letter_dict: Dict[chr, int]):
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1


def convert_word_to_dict(word: str) -> Dict[chr, int]:
    char_dict = {}
    for character in word.lower():
        add_character_to_dict(character, char_dict)
    return char_dict


if __name__ == "__main__":
    print(len(load_words()))
