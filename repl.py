# coding: utf-8

import smyrk
import emoji
import readline
import sys

# Fix Python 2.x.
try: input = raw_input
except NameError: pass

emoji_bindings = [ 
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
('(t)', '👍'),
('(f)', '👎'),
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
('(p)', '🖨'),
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
        for char in emoji.all_chars(msg):
            out += char + ' '
        print(out)

    def output(self, msg):
        self.print_with_emoji(msg)

    def error(self, msg):
        self.print_with_emoji(msg)

class REPL:
    def __init__(self):
        self.runtime = smyrk.Runtime(REPLDelegate)

    def run(self, args):
        try:
            file_idx = -1
            for i, arg in enumerate(args):
                if arg == '-i':
                    file_idx = i + 1
                if i == file_idx:
                    file_idx = -1
                    lines = [line.strip() for line in open(arg, 'r')]
                    for line in lines:
                        self.runtime.decode(line)
            line = ''
            while not self.runtime.halted:
                line = input('smyrk> ')
                for key, value in emoji_bindings:
                    line = line.replace(key, value)
                self.runtime.decode(line)
        except EOFError:
            print('')

if __name__ == '__main__': REPL().run(sys.argv)