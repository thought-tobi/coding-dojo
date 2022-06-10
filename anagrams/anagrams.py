from typing import List, Dict

from word import Word


def load_words() -> List[Word]:
    with open("wordlist.txt", encoding="ISO-8859-1") as file:
        s = file.read()
        words = []
        for word in s.split("\n"):
            words.append(Word(word))
        return words


def cluster_words_into_anagrams(words: List[Word]) -> Dict[str, List[str]]:
    word_cluster = {}
    for word in words:
        if word.hash in word_cluster:
            word_cluster[word.hash].append(word.string)
        else:
            word_cluster[word.hash] = [word.string]
    return word_cluster


def filter_non_anagrams(word_cluster: Dict[str, List[str]]):
    for key in list(word_cluster):
        if len(word_cluster[key]) == 1:
            del word_cluster[key]


def get_words_from_cluster(word_cluster: Dict[str, List[str]]):
    return word_cluster.values()


if __name__ == "__main__":
    list_of_words = load_words()
    cluster = cluster_words_into_anagrams(list_of_words)
    filter_non_anagrams(cluster)
    print(get_words_from_cluster(cluster))
