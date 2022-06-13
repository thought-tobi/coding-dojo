import datetime
from typing import List, Dict

from word import Word


def load_words() -> List[Word]:
    with open("wordlist.txt", encoding="ISO-8859-1") as file:
        s = file.read()
        words = []
        for word in s.split("\n"):
            words.append(Word(word))
        return words


def cluster_words_into_anagrams(words: List[Word]) -> Dict[List[chr], List[str]]:
    anagrams = {}
    for word in words:
        if word.characters in anagrams:
            anagrams[word.characters].append(word.string)
        else:
            anagrams[word.characters] = [word.string]
    return anagrams


def filter_non_anagrams(word_cluster: Dict[List[chr], List[str]]):
    for key in list(word_cluster):
        if len(word_cluster[key]) == 1:
            del word_cluster[key]


def print_anagrams(word_cluster: Dict[List[chr], List[str]]):
    for value in word_cluster.values():
        print(value)


def main():
    start = datetime.datetime.now()
    list_of_words = load_words()
    read_file_time = datetime.datetime.now()

    anagram_cluster = cluster_words_into_anagrams(list_of_words)

    filter_non_anagrams(anagram_cluster)

    print_anagrams(anagram_cluster)
    end = datetime.datetime.now()

    print(f"Read wordlist in {(read_file_time - start).total_seconds() * 1000}ms")
    print(f"Ran in {(end - start).total_seconds() * 1000}ms")


if __name__ == "__main__":
    main()
