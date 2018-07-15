from .app import get_print_string

if __name__ == '__main__':
    name = input('Hi, what is your name?\n>> ')
    msg = get_print_string(name)
    print(msg)
