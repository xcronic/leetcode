# console_color.py
class ConsoleColor:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'

def print_colored(text, color):
    print(f"{color}{text}{ConsoleColor.RESET}")

def print_red(text):
    print_colored(text, ConsoleColor.RED)

def print_green(text):
    print_colored(text, ConsoleColor.GREEN)

def print_blue(text):
    print_colored(text, ConsoleColor.BLUE)
