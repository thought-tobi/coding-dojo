import unittest
import anagrams


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

if __name__ == '__main__':
    unittest.main()
