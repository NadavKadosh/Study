import random
from typing import List, Any

HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
HANGMAN_PHOTOS = {
    '1': """
    x-------x
    """,
    '2': """
    x-------x
    |
    |
    |
    |
    |
    """,
    '3':"""
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    '4':"""
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    '5': """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

    """,
    '6': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

    """,
    '7':"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}

print(HANGMAN_ASCII_ART)
print("ברוכים הבאים למשחק איש תלוי! \n יש לכם 7 נסיונות לפני שתיפסלו")



def is_valid_guess(letter_guessed):
    """
    the function checks if the input of the player is valid
    :type letter_guessed: str
    :param letter_guessed: str
    :return: boolean
    """
    if (len(letter_guessed) == 1 and letter_guessed.isalpha()):
        return True
    else:
        return False

def check_valid_guess (letter_guessed, old_letter_guessed):
    """
    the function cheks if the user already guessed the letter and if the letter is valid
    :param letter_guessed: the letter the user guessed
    :type letter_guessed: str
    :param old_letter_guessed: list of letters the user guessed
    :type old_letter_guessed: list
    :return: true if the input is ok
    """
    if is_valid_guess(letter_guessed) and not letter_guessed in old_letters_guessed:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    check if the letter is valid, and if it is, add him to the list
    :param letter_guessed: the letter the player guessed
    :type letter_guessed: str
    :param old_letters_guessed: the list of letters
    :type old_letters_guessed: list
    :return: true if the letter is good, and add it to the list. else- print X and show the list
    :rtype: bool
    """
    if check_valid_guess(letter_guessed, old_letters_guessed): # pay attention: the 'if' operate the check func
        return True
    else:
        print("Please insert a letter you didn't already guessed. you guessed:")
        split = "->"
        sorted_list = sorted(old_letters_guessed, key=str.lower)
        split = split.join(sorted_list)
        print(split)
        return False

def show_hidden_words(secret_word, old_letters_guessed):
    """
    the function return the word the player need to guess with empty slots
    :param secret_word: the word
    :type secret_word: str
    :param old_letters_guessed: the letters the player guessed
    :type old_letters_guessed: list
    :return: the word with empty places
    :rtype: str
    """
    rword = ''
    for char in secret_word:
        if char in old_letters_guessed:
            rword = rword + char + ' '
        else:
            rword = rword + '_ '
    return rword

def check_win (secret_word, old_letters_guessed):
    """
    the func checks if the player won
    :param secret_word: the word
    :param old_letters_guessed:
    :return: bool
    """
    if_true = True
    for char in secret_word:
        if char in old_letters_guessed:
            pass
        else:
            if_true = False 
            break
    return if_true

def print_hangman(num_of_tries):
    num = str(num_of_tries)
    print(HANGMAN_PHOTOS[num])

def choose_word (file_path, index):
    """
    return the number of words and the index of the words
    :param file_path: file path for words
    :param index: word index in the file
    :return: tuple with the word and number of words in the file
    """
    with open(file_path, "r") as the_file:
        word_list = []
        temp_list = the_file.readlines()
        for i in range(len(temp_list)): 
            word_list.append(temp_list[i].split(' '))
        for i in range(len(word_list)-1): 
            word_list[i][-1] = word_list[i][-1][:-1]
        new_word_list = []
        for line in word_list: 
            for word in line:
                a= word
                new_word_list.append(a)
        num_word_list = [] 
        for word in new_word_list:
            if word not in num_word_list:
                num_word_list.append(word)
        rtup = (new_word_list[index-1], len(num_word_list),len(new_word_list))
        return rtup

words_flie_path = input("Please insert path for a file with words:")
limit = choose_word(words_flie_path,0)[2]
print("Please insert a number between 1 and",limit)
word_index = int(input())
secret_word= choose_word(words_flie_path, word_index)[0]
secret_word_len=len(secret_word)
print("_ "*secret_word_len) 
MAX_TRIES = 7 
current_try = 0 
old_letters_guessed = [] 
while current_try < MAX_TRIES and not check_win(secret_word,old_letters_guessed):
    player_guess = str(input('Guess a letter:'))
    player_guess=player_guess.lower() 
    if is_valid_guess(player_guess):
        if player_guess not in old_letters_guessed and player_guess not in secret_word:
            current_try += 1
            print(current_try)
            print_hangman(current_try)
        try_update_letter_guessed(player_guess, old_letters_guessed)
        print(show_hidden_words(secret_word, old_letters_guessed))
        if check_win(secret_word, old_letters_guessed):
            print ("You win!")
    else:
        print("Please insert a letter. not multiple letters or number")
if not check_win(secret_word, old_letters_guessed):
    print("הפסדת, באסה")
