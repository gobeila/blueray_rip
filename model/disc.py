from collections import defaultdict

from model.title import Title


class Disc:

    def __init__(self, type = "", titles = defaultdict(Title)):
        self.type = type
        self.titles = titles

    def __repr__(self):
        return f"Disc('{self.type}', {self.titles})"
    
    def __str__(self):
        result = f"{self.type}\n"
        for key in self.titles.keys():
            result += f"Track {key}: "
            result += str(self.titles[key])
        return result