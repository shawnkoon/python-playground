MAX_COLUMN_COUNT = 6

def generate_clean_list(words, variable_name):
    res = set([word.split('\n')[0].lower() for word in words])

    print(f'{variable_name} = [')
    count = 0
    for word in res:
        if count == 0:
            print('    ', end='')

        if count == MAX_COLUMN_COUNT:
            print()
            print('    ', end='')
            count = 0

        print(f'\'{word}\'', end=', ')

        count = count + 1

    if count != 0:
        print()

    print(']')

with open('nouns.txt', 'r') as fp:
    words = fp.readlines()
    generate_clean_list(words, 'NOUNS')

print()

with open('adjectives.txt', 'r') as fp:
    words = fp.readlines()
    generate_clean_list(words, 'ADJECTIVES')
