from dataclasses import dataclass, field
import hashlib
import json
from typing import Union, DefaultDict
from collections import defaultdict


class Word:
    def __init__(self, string):
        self.string: str = string
        self.char_dict = self.add_char_dict()
        self.hash = self.calculate_dict_hash()

    def calculate_dict_hash(self):
        dhash = hashlib.md5()
        # We need to sort arguments so {'a': 1, 'b': 2} is
        # the same as {'b': 2, 'a': 1}
        encoded = json.dumps(self.char_dict, sort_keys=True).encode()
        dhash.update(encoded)
        return dhash.hexdigest()

    def add_char_dict(self):
        char_dict_tmp = defaultdict(int)
        for character in self.string:
            char_dict_tmp[character] += 1
        return char_dict_tmp
