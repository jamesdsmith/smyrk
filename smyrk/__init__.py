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
    def __init__(self, command_type=''):
        self.command_type = command_type
        self.parameters = []

    def set_type(self, command_type):
        self.command_type = command_type

    def add_parameter(self, param):
        if len(self.parameters) > 0 and emoji.is_digit(self.parameters[-1]) and emoji.is_digit(param):
            self.parameters[-1] += param
        else:
            self.parameters.append(param)

    def __repr__(self):
        return 'Command({0}, {1})'.format(self.command_type, self.parameters)

    def __str__(self):
        msg = self.command_type
        for param in self.parameters:
            msg += param
        return msg

class Runtime:
    instructions = {'❌', '👉', '👀', '🗄', '➕', '➖', '✖️', '➗', '🤔', '🌚', '🌝', '🏃', '🚶', '📖', '🖨', '☎️', '🔙'}
    def __init__(self, DelegateClass):
        self.stack = []
        self.halted = False
        self.delegate = DelegateClass(self)

    def tokenize(self, line):
        commands = []
        new_command = None
        for char in emoji.all_chars(line):
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
        ""
        commands = self.tokenize(line)
        for command in commands:
            self.delegate.output(str(command))
            self.execute(command)

    def execute(self, command):
        ""

class RuntimeDelegate:
    def __init__(self, runtime):
        self.runtime = runtime

    def output(self, msg):
        """How to output something to the screen"""