from xparse import *
from xerror import *

import pyb


class Xlang_interpreter:
    def __init__(self):
        self.HPRINT   = False
        self.HPRINTLN = False
        self.LEDON    = False
        self.LEDOFF   = False

    def scan_word(self, word: str):
        if self.HPRINT:
            print(word, end='')
            self.HPRINT = False
        elif self.HPRINTLN:
            print(word)
            self.HPRINTLN = False
        elif self.LEDON:
            pyb.LED(int(word)).on()
            self.LEDON = False
        elif self.LEDOFF:
            pyb.LED(int(word)).off()
            self.LEDOFF = False
        else:
            if word == '':
                pass
            elif word == 'hprint':
                self.HPRINT = True
            elif word == 'hprintln':
                self.HPRINTLN = True
            elif word == 'ledon':
                self.LEDON = True
            elif word == 'ledoff':
                self.LEDOFF = True
            else:
                panic(f'\nX syntax error: Keyword {word} does not exist')

    def scan(self, code: str):
        Code = X_parse(code)
        for word in Code:
            self.scan_word(word)