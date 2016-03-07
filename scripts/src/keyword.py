class Keyword:
    def __init__(self, keyword):
        if keyword in ['add', 'find']:
            self.value = keyword
        else:
            self.value = 'find'
