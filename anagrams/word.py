from dataclasses import dataclass, field
import hashlib
import json
from typing import Union, DefaultDict
from collections import defaultdict


class Word:
    def __init__(self, string):
        self.string: str = string
        self.characters = self.generate_characters_list()

    def generate_characters_list(self):
        return tuple(sorted(list(self.string)))
