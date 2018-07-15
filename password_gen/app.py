import random
from string import punctuation

NOUNS = [
    'napkin', 'cross', 'philosophy', 'management', 'abbey', 'ring',
    'calendar', 'newsprint', 'hobbies', 'mariachi', 'bamboo', 'flow',
    'macaroni', 'brother', 'siding', 'dumbwaiter', 'attachment', 'trust',
    'salary', 'yurt', 'guidance', 'bugle', 'human', 'invite',
    'pattern', 'necessary', 'sneeze', 'poem', 'ballet', 'cylinder',
    'acrylic', 'robe', 'karen', 'petticoat', 'submarine', 'exam',
    'stain', 'locker', 'wharf', 'cloak', 'linen', 'fixture',
    'reaction', 'improvement', 'chafe', 'earth', 'negligee', 'bone',
    'she', 'tent', 'policeman', 'bustle', 'dogsled', 'restaurant',
    'laugh', 'turnip', 'turret', 'tadpole',
]

ADJECTIVES = [
    'environmental', 'boring', 'civil', 'unlikely', 'odd', 'traditional',
    'eastern', 'careful', 'old', 'recent', 'dangerous', 'electrical',
    'administrative', 'serious', 'suitable', 'happy', 'latter', 'sudden',
    'historical', 'comprehensive', 'hungry', 'unusual', 'weak', 'additional',
    'hot', 'different', 'relevant', 'alive', 'nervous', 'technical',
    'successfully', 'former', 'famous', 'emotional', 'aware', 'unhappy',
    'realistic', 'automatic', 'huge', 'actual', 'impressive', 'informal',
    'political', 'critical', 'significant', 'strict', 'funny', 'massive',
    'southern', 'aggressive', 'strong', 'substantial', 'helpful', 'lonely',
    'confident', 'capable', 'cold', 'pregnant', 'mental', 'medical',
    'efficient',
]

def password_gen():
    """Generate random password.

    Generates password in format of <adjective><noun><rand(0,1000)><punctuation>
    """
    adjective = random.choice(ADJECTIVES).capitalize()
    noun = random.choice(NOUNS).capitalize()
    numb = random.randrange(0, 1000)
    punc = random.choice(punctuation)

    return f'{adjective}{noun}{numb}{punc}'

if __name__ == '__main__':
    print('Welcome to Password Generator app')
    print('Please press Enter to get started.')
    while True:
        print(f'\nGenerated Password : {password_gen()}')
        user_input = input(f'Enter to continue or \'q\' to quit. ')

        if user_input.lower() == 'q':
            break
