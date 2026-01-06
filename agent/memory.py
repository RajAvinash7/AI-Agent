class Memory:
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def add_short(self, data):
        self.short_term.append(data)

    def add_long(self, data):
        self.long_term.append(data)

    def get_context(self):
        return self.short_term[-5:] + self.long_term
