from termcolor import colored

printRed = lambda s: print(colored(s, 'red'))
printGreen = lambda s: print(colored(s, 'green'))
printBlue = lambda s: print(colored(s, 'blue'))
printYellow = lambda s: print(colored(s, 'yellow'))

inputRed = lambda s: input(colored(s, 'red'))
inputGreen = lambda s: input(colored(s, 'green'))
inputBlue = lambda s: input(colored(s, 'blue'))
inputYellow = lambda s: input(colored(s, 'yellow'))

def printCommands(command_dict, max_len=52):
    names = list(command_dict.keys())
    names.sort()

    COMMAND_LENGTH = 32
    printGreen('\nAvailable commands:')

    for name in names:
        line = ' - {}'.format(name)
        d = COMMAND_LENGTH - len(line)
        line += ' ' * d
        description = command_dict.get(name).get('description', '')
        line += description
        printGreen(line)
    printRed(' - quit (sign out)\n')

def list_all(items):
    def list_all_items(_):
        for i in items:
            printYellow(i)
        print('\n')
    return list_all_items