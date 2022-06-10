from typing import List, Dict, DefaultDict
from collections import defaultdict
import hashlib

from Word import Word


def load_words() -> List[Word]:
    with open("wordlist.txt", encoding="ISO-8859-1") as file:
        s = file.read()
        words = []
        for word in s.split("\n"):
            words.append(Word(word))
        return words


# this function can be made obsolete by using the defaultdict implementation
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


def convert_word_to_defaultdict(word: str) -> DefaultDict:
    char_dict = defaultdict(int)
    for character in word:
        char_dict[character] += 1
    return char_dict


def add_dicts(words: List[Word]):
    for word in words:
        word.characters_dict = convert_word_to_dict(word.word)


if __name__ == "__main__":
    list_of_words = load_words()
    add_dicts(list_of_words)
