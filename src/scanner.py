from xparse import *
from xerror import *
from LED    import *

from time import sleep_ms as sleep


class Xlang_interpreter:
    def __init__(self):
        self.HPRINT   = False
        self.HPRINTLN = False
        self.LEDON    = False
        self.LEDOFF   = False
        self.SLEEP    = False

    def scan_word(self, word: str):
        if self.HPRINT:
            print(word, end='')
            self.HPRINT = False
        elif self.HPRINTLN:
            print(word)
            self.HPRINTLN = False
        elif self.LEDON:
            ledon(word)
            self.LEDON = False
        elif self.LEDOFF:
            ledoff(word)
            self.LEDOFF = False
        elif self.SLEEP:
            sleep(int(word))
            self.SLEEP = False
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
            elif word == 'sleep':
                self.SLEEP = True
            else:
                panic('\nX syntax error: Keyword {word} does not exist'.format())
                raise SystemExit

    def scan(self, code: str):
        Code = X_parse(code)
        for word in Code:
            self.scan_word(word)