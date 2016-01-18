import emoji

class Command:
    def __init__(self, cmd='', param=''):
        self.cmd = cmd
        self.param = param

    def set_type(self, cmd):
        self.cmd = cmd

    def add_parameter(self, param):
        if self.param != '' and emoji.is_digit(self.param) and emoji.is_digit(param):
            self.param += param
        else:
            self.param = param

    def __repr__(self):
        return 'Command({0}, {1})'.format(self.cmd, self.param)

    def __str__(self):
        return self.cmd + self.param

class EmptyStackException(Exception):
    pass

class SmyrkRuntimeError(Exception):
    pass

class Runtime:
    def __init__(self, DelegateClass):
        self.stack = []
        self.halted = False
        self.delegate = DelegateClass(self)
        self.environment = {}
        self.instructions = {
            '❌': lambda x: self.delegate.exit(),
            '👉': lambda x: self.push(x),
            '👀': lambda x: self.push(self.environment[x]),
            '🗄': lambda x: self.pop(),
            '➕': lambda x: self.push(emoji.to_emoji(emoji.to_num(self.pop()) + emoji.to_num(self.pop()))),
            '➖': lambda x: self.push(emoji.to_emoji(emoji.to_num(self.pop()) - emoji.to_num(self.pop()))),
            '✖️': lambda x: self.push(emoji.to_emoji(emoji.to_num(self.pop()) * emoji.to_num(self.pop()))),
            '➗': lambda x: self.push(emoji.to_emoji(emoji.to_num(self.pop()) // emoji.to_num(self.pop()))),
            '🤔': lambda x: self.push(emoji.bool_to_emoji(emoji.to_num(self.pop()) == emoji.to_num(self.pop()))),
            '🌚': lambda x: self.push(emoji.bool_to_emoji(emoji.to_num(self.pop()) < emoji.to_num(self.pop()))),
            '🌝': lambda x: self.push(emoji.bool_to_emoji(emoji.to_num(self.pop()) > emoji.to_num(self.pop()))),
            '🏃': lambda x: "",
            '🚶': lambda x: "",
            '📖': lambda x: self.push(emoji.to_num(self.delegate.input())),
            '🖨': lambda x: self.delegate.output(self.pop()),
            '☎️': lambda x: "",
            '⚓️': lambda x: "",
            '🔙': lambda x: "",
        }

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
                raise SmyrkRuntimeError('Unknown command: {0}'.format(char))
        if new_command != None:
            commands.append(new_command)
        return commands

    def decode(self, line):
        """Returns the next instruction in the line"""
        try:
            commands = self.tokenize(line)
            for command in commands:
                self.delegate.output(str(command))
                self.execute(command)
        except EmptyStackException as e:
            self.delegate.error(str(e))
        except SmyrkRuntimeError as e:
            self.delegate.error(str(e))
        except KeyError as e:
            self.delegate.error('{0} is not defined'.format(str(e)))

    def execute(self, command):
        self.instructions[command.cmd](command.param)
        
    def push(self, item):
        self.stack = [item] + self.stack

    def pop(self):
        if len(self.stack) == 0:
            raise EmptyStackException('Tried to pop an empty stack')
        item = self.stack[0]
        self.stack = self.stack[1:]
        return item

class RuntimeDelegate:
    def __init__(self, runtime):
        self.runtime = runtime

    def output(self, msg):
        """Output something to the screen"""

    def input(self):
        """Get some input from the user"""

    def error(self, msg):
        """Properly handle errors"""

    def exit(self):
        """Properly exit the program that is using the runtime"""
        self.runtime.halted = True