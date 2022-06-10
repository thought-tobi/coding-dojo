import unittest

from word import Word


class MyTestCase(unittest.TestCase):

    def test_init_word(self):
        word = Word('cat')
        assert len(word.char_dict) == 3
        assert word.char_dict['c'] == 1
        assert word.char_dict['a'] == 1
        assert word.char_dict['t'] == 1

    def test_compare_unequal_words(self):
        cat = Word('cat')
        doggo = Word('doggo')

        assert cat.hash != doggo.hash

    def test_compare_anagrams(self):
        kinship = Word('kinship')
        pinkish = Word('pinkish')

        assert kinship.hash == pinkish.hash


if __name__ == '__main__':
    unittest.main()
