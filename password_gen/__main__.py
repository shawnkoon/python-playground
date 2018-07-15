from .app import password_gen

if __name__ == '__main__':
    print('Welcome to Password Generator app')
    print('Please press Enter to get started.')
    while True:
        print(f'\nGenerated Password : {password_gen()}')
        user_input = input(f'Enter to continue or \'q\' to quit. ')

        if user_input.lower() == 'q':
            break
