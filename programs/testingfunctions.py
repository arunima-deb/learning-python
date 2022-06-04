import random
def word_selected(fname):
    word_file = open('hangman.txt','r+')
    secret_word = random.choice(word_file.read().split())
    word_file.close()
    return secret_word
