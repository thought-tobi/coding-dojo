from typing import List, Dict, DefaultDict
from collections import defaultdict
import hashlib
import json

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


def calculate_dict_hash(word: Word):
    dhash = hashlib.md5()
    # We need to sort arguments so {'a': 1, 'b': 2} is
    # the same as {'b': 2, 'a': 1}
    encoded = json.dumps(word.characters_dict, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


def add_hashes(words: List[Word]):
    for word in words:
        word.dict_hash = calculate_dict_hash(word)


def get_all_anagrams(words: List[Word]) -> List[List[Word]]:
    hash_dict = {}
    for word in words:
        if word.dict_hash in hash_dict:
            hash_dict[word.dict_hash].append(word)
        else:
            hash_dict[word.dict_hash] = [word]
    for key in hash_dict:
        if len(hash_dict[key]) > 2:
            print(hash_dict[key])


if __name__ == "__main__":
    list_of_words = load_words()
    add_dicts(list_of_words)
    add_hashes(list_of_words)
    get_all_anagrams(list_of_words)
