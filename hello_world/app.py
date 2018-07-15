def get_print_string(name):
    """Get Hello World string with name."""
    return f'Hello {name}! This is Shawnkoon.'

if __name__ == '__main__':
    name = input('Hi, what is your name?\n>> ')
    msg = get_print_string(name)
    print(msg)
