import unittest
import anagrams
from Word import Word


class MyTestCase(unittest.TestCase):

    def test_add_character_to_dict(self):
        empty_dict = {}
        anagrams.add_character_to_dict('A', empty_dict)
        assert empty_dict.get('A') == 1

    def test_add_character_to_non_empty_dict(self):
        non_empty_dict = {'A': 1, 'B': 3}
        anagrams.add_character_to_dict('B', non_empty_dict)
        assert non_empty_dict.get('A') == 1
        assert non_empty_dict.get('B') == 4

    def test_convert_word_to_dict(self):
        word = 'doggo'
        word_as_dict = anagrams.convert_word_to_dict(word)
        assert word_as_dict.get('d') == 1
        assert word_as_dict.get('o') == 2
        assert word_as_dict.get('g') == 2

    def test_default_dict_alternative(self):
        word = 'doggo'
        word_as_dict = anagrams.convert_word_to_defaultdict(word)
        assert word_as_dict.get('d') == 1
        assert word_as_dict.get('o') == 2
        assert word_as_dict.get('g') == 2


    def test_word_list(self):
        word_list = [Word("cat"), Word("doggo")]
        anagrams.add_dicts(word_list)
        assert word_list[0].characters_dict['c'] == 1
        assert word_list[0].characters_dict['a'] == 1
        assert word_list[0].characters_dict['t'] == 1

        assert word_list[1].characters_dict['d'] == 1
        assert word_list[1].characters_dict['o'] == 2
        assert word_list[1].characters_dict['g'] == 2


if __name__ == '__main__':
    unittest.main()
