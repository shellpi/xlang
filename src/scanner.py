import xparse
import xerror

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
            if word == 'hprint':
                self.HPRINT = True
            elif word == 'hprintln':
                self.HPRINTLN = True
            else:
                xerror.panic(f'X syntax error: Keyword {word} does not exist')

    def scan(self, code: str):
        Code = xparse.__x_parse(code)
        for word in Code:
            self.scan_word(word)