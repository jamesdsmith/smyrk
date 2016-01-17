# coding: utf-8

import smyrk
import emoji
import readline
from tree import *

# Fix Python 2.x.
try: input = raw_input
except NameError: pass

emoji_bindings =  [ 
(':>', '😏'),
(':)', '😊'),
(';)', '😉'),
(':(', '😟'),
('B)', '😎'),
(':D', '😃'),
('D:', '😩'),
(':d', '😋'),
(';p', '😜'),
(':p', '😛'),
(':o', '😮'),
(':s', '😖'),
(':x', '😶'),
(':|', '😐'),
(':/', '😕'),
(':[', '😳'),
(':>', '😏'),
(':@', '😷'),
(':*', '😘'),
(':!', '😬'),
(':3', '😺'),
('(y)', '👍'),
('(n)', '👎'),
('0', '0️⃣'),
('1', '1️⃣'),
('2', '2️⃣'),
('3', '3️⃣'),
('4', '4️⃣'),
('5', '5️⃣'),
('6', '6️⃣'),
('7', '7️⃣'),
('8', '8️⃣'),
('9', '9️⃣'),
('~', '👉'),
('(print)', '🖨'),
('F', '⚓️'),
('x', '❌'),
('<-', '👀'),
('->', '🗄'),
('?', '🤔'),
('lt', '🌚'),
('gt', '🌝'),
('^', '🏃'),
(';', '🚶'),
('r', '📖'),
('&', '☎️'),
('(ret)', '🔙'),
('+', '➕'),
('-', '➖'),
('/', '➗'),
('*', '✖️'),
]

class REPLDelegate(smyrk.RuntimeDelegate):
    def print_with_emoji(self, msg):
        out = ''
        for char in emoji_iter.all_chars(msg):
            out += char
            if char in emoji.UNICODE_EMOJI:
                out += ' '
        print(out)

    def output(self, msg):
        self.print_with_emoji(msg)

    def error(self, msg):
        self.print_with_emoji(msg)

class REPL:
    def __init__(self):
        self.runtime = smyrk.Runtime(REPLDelegate)

    def run(self):
        line = ''
        while line != '❌':
            line = input('smyrk> ')
            for key, value in emoji_bindings:
                line = line.replace(key, value)
            self.runtime.decode(line)

if __name__ == '__main__': REPL().run()