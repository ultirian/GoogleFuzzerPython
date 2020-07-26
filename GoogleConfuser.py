#python google confusion engine, requires wordlist.
import random
import time
from webbot import Browser
from time import sleep
from random import randint

#Need browser that can sign in (todo)
def sign_in():
    web.go_to('google.com')
    web.click(id = 'gb_70')
    sleep(2)
    web.click(id = 'identifierId')
    web.type('test@test.com')
    web.press(web.Key.ENTER)

#loads word list
def load_words():
    with open('wordlist.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

#inserts search term into googles, forever.
def insert_searchterm():
    var = 1
    while var == 1 :
        web.type(f'{random.choice(setword)} {random.choice(setword)}')
        web.press(web.Key.ENTER)
        sleep(randint(1,7))
        web.go_back()

if __name__ == '__main__':
    web = Browser()

    #English word list from textfile.
    english_words = load_words()    
    #Convert set to list
    setword = list(english_words)

    sign_in()
    insert_searchterm() 

    

    
