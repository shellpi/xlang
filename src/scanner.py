from xparse import *
from xerror import *

class Xlang_interpreter:
    def __init__(self):
        self.HPRINT   = False
        self.HPRINTLN = False

    def scan_word(self, word: str):
        if self.HPRINT:
            print(word, end='')
            self.HPRINT = False
        elif self.HPRINTLN:
            print(word)
            self.HPRINTLN = False
        else:
            if word == '':
                pass
            elif word == 'hprint':
                self.HPRINT = True
            elif word == 'hprintln':
                self.HPRINTLN = True
            else:
                panic(f'\nX syntax error: Keyword {word} does not exist')

    def scan(self, code: str):
        Code = X_parse(code)
        for word in Code:
            self.scan_word(word)