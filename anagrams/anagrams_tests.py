import unittest

import anagrams
from word import Word


class MyTestCase(unittest.TestCase):

    def test_init_word(self):
        word = Word('cat')
        assert len(word.characters) == 3

    def test_compare_unequal_words(self):
        cat = Word('cat')
        doggo = Word('doggo')

        assert cat.characters != doggo.characters

    def test_compare_anagrams(self):
        kinship = Word('kinship')
        pinkish = Word('pinkish')

        assert kinship.characters == pinkish.characters

    def integration_test(self):
        kinship = Word('kinship')
        pinkish = Word('pinkish')

        enlist = Word('enlist')
        listen = Word('listen')
        inlets = Word('inlets')

        cat = Word('cat')

        word_list = [kinship, pinkish, enlist, listen, inlets, cat]

        anagram_cluster = anagrams.cluster_words_into_anagrams(word_list)
        assert len(anagram_cluster) == 2
        assert len(anagram_cluster.get(('e', 'i', 'l', 'n', 's', 't'))) == 3


if __name__ == '__main__':
    unittest.main()
