import emoji

"""
HALT  ❌
CONST 👉
LOAD  👀
STO   🗄
ADD   ➕
SUB   ➖
MUL   ✖️
DIV   ➗
EQL   🤔
LSS   🌚
GTR   🌝
JMP   🏃
FJMP  🚶
READ  📖
WRITE 🖨
CALL  ☎️
RET   🔙
"""

class Command:
    def __init__(self, cmd='', param=''):
        self.cmd = cmd
        self.param = param

    def set_type(self, cmd):
        self.cmd = cmd

    def add_parameter(self, param):
        if self.param != '' and emoji_iter.is_digit(self.param) and emoji_iter.is_digit(param):
            self.param += param
        else:
            self.param = param

    def __repr__(self):
        return 'Command({0}, {1})'.format(self.cmd, self.param)

    def __str__(self):
        return self.cmd + self.param

class EmptyStackException(Exception):
    pass

class Runtime:
    def __init__(self, DelegateClass):
        self.stack = []
        self.halted = False
        self.delegate = DelegateClass(self)
        self.environment = {}
        self.instructions = {
            '❌': lambda: "",
            '👉': lambda x: self.push(x),
            '👀': lambda x: self.push(self.environment[x]),
            '🗄': lambda x: self.pop(),
            '➕': lambda x: self.push(self.pop() + self.pop()),
            '➖': lambda x: self.push(self.pop() - self.pop()),
            '✖️': lambda x: self.push(self.pop() * self.pop()),
            '➗': lambda x: self.push(self.pop() / self.pop()),
            '🤔': lambda x: self.push(self.pop() == '👍'),
            '🌚': lambda x: self.push(self.pop() > self.pop()),
            '🌝': lambda x: self.push(self.pop() < self.pop()),
            '🏃': lambda x: "",
            '🚶': lambda x: "",
            '📖': lambda x: "",
            '🖨': lambda x: self.delegate.output(self.pop()),
            '☎️': lambda x: "",
            '🔙': lambda x: "",
        }

    def tokenize(self, line):
        commands = []
        new_command = None
        for char in emoji_iter.all_chars(line):
            if char in self.instructions:
                if new_command != None:
                    commands.append(new_command)
                new_command = Command(char)
            elif new_command != None:
                new_command.add_parameter(char)
            else:
                #Throw a runtime error
                ""
        if new_command != None:
            commands.append(new_command)
        return commands

    def decode(self, line):
        """Returns the next instruction in the line"""
        commands = self.tokenize(line)
        for command in commands:
            self.delegate.output(str(command))
            self.execute(command)

    def execute(self, command):
        try:
            self.instructions[command.cmd](command.param)
        except EmptyStackException as e:
            self.delegate.error(str(e))

    def push(self, item):
        self.stack = [item] + self.stack

    def pop(self):
        if len(self.stack) == 0:
            raise EmptyStackException("Tried to pop an empty stack")
        item = self.stack[0]
        self.stack = self.stack[1:]
        return item

class RuntimeDelegate:
    def __init__(self, runtime):
        self.runtime = runtime

    def output(self, msg):
        """How to output something to the screen"""

    def error(self, msg):
        """Properly handle errors"""