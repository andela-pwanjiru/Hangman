import random

def get_w():
    """Get words from a dictionary and checks if they match what the\
    user entered"""
    words = {
            "PENNY":"Name of a girl",
            "ANDELA":"A technology company that trains developers",
            "AFRICA":"A continent",
            "EUROPE":"A continent",
            "GERMANY":"A country"
            }
    # Returns all keys in the dictionary in a list
    specific_words = words.keys()
    # Selects a random key from the dictionary
    key = random.choice(specific_words)
    # Gets the value of the corresponding key
    description = words[key]
    print 'Clue: %s' % description
    length = len(key)
    results = list('_'*length)
    print ''.join(results)
    # Initializes the number of chances the player has.
    chance_count = 9
    answer_letters = []
    while chance_count > 0:
        answer = raw_input("enter a letter:").upper()
        if answer in answer_letters:
            print "You have tried letter %s already." % (answer)
            continue
        answer_letters.append(answer)
        # Converts the key into a list for easy comparison with results.
        keys = list(key)
        flag = False
        # Replaces the found letter with the one inputed by the user.
        for index in range(length):
            if keys[index] == answer:
                results[index] = answer
                flag = True
        # Checks if the final word is equal to the word.
        if results == keys:
            print ''.join(results)
            print "Congratulations! You got it!"
            break
        print ''.join(results)
        if flag is not True:
            chance_count -= 1
        print "You have %d chances left" % chance_count

get_w()
