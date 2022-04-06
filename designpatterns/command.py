from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "The command interface, that all commands will implement"
    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"


class Invoker:
    "The Invoker Class"

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        "Register commands in the Invoker"
        self._commands[command_name] = command

    def execute(self, command_name):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")


class Receiver:
    "The Receiver"

    @staticmethod
    def run_command_1():
        "A set of instructions to run"
        print("Executing Command 1")

    @staticmethod
    def run_command_2():
        "A set of instructions to run"
        print("Executing Command 2")


class Command1(ICommand):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()


class Command2(ICommand):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()


# Create a receiver
receiver = Receiver()

# Create Commands
command_1 = Command1(receiver)
command_2 = Command2(receiver)

# Register the commands with the invoker
invoker = Invoker()
invoker.register("1", command_1)
invoker.register("2", command_2)

# Execute the commands that are registered on the Invoker
invoker.execute("1")
invoker.execute("2")
invoker.execute("1")
invoker.execute("2")

