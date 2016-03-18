import random


def get_words():

    words = {
            'AFRICA':['A','F','R','I','C','A'],
            'ASIA': ['A','S','I','A'],
            'NOTEBOOK':['N','O','T','E','B','O','O','K'],
            'FILTER':['F','I','L','T','E','R'],
            'DOJO':['D','O','J','O'],
            'ANDELA':['A','N','D','E','L','A'],
            'PYTHON':['P','Y','T','H','O','N'],
            'HOPE':['H','O','P','E'],
            'WORDS':['W','O','R','D','S']
            }

    new_word = words[random.choice(words.keys())]
    length = len(new_word)
    results = list('_' * length)
    print ''.join(results)

    for tries in range(9):
        answer = raw_input('Enter a letter ')
        for index in range(length):
            if answer == new_word[index]:
                results[index] = answer

        if results == new_word:
            break

        print ''.join(results)



    # print results

get_words()
