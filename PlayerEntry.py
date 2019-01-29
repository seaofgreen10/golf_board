

class PlayerEntry:

    def __init__(self):
        self.name = ''
        self.score = ''
        self.rank = ''
        self.date = ''
        self.time = ''



    def add_name(self, name):
        self.name = name

    def get_name(self):
        return self.name