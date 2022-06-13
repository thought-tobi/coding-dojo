class Word:
    def __init__(self, string):
        self.string: str = string
        self.characters = self.generate_characters_list()

    def generate_characters_list(self):
        return tuple(sorted(list(self.string)))
