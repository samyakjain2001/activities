#Madlibs

# youtuber = "freecodecamp" #some string variable
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# adj = input("Adjective: ")
# lang = input("Coding language: ")
# yrs = input("Experience in years: ")
# madlib = f"Computer programming is so {adj}! I started with {lang} and I have {yrs} of experience!"
# print(f"\n{madlib}")

# Guess a Number
import random
# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess!= random_number:
#         guess  = int(input(f"Guess the number between 1 and {x}: "))
#         if guess < random_number:
#             print(f"The number is higher than {guess}.")
#         elif guess > random_number:
#             print(f"The number is lower than {guess}.")
#     print(f"Woahh! You have guessed the right number !!!")

# guess(int(input('Enter the range from 1 to : ')))

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too High(H), too low(L) or correct(C)?? ")
        if feedback == 'L':
            low = guess +1
        elif feedback == 'H':
            high = guess -1
    print(f"\nWoahh! Computer have guessed the right number, {guess} !!!")

# computer_guess(int(input("Enter the range from 1 to _: ")))

# Rock Paper Scissor

def play():
    user = input("\nWhat's you choice: \n'r' for rock, 'p' paper and 's' for scissors: " )
    computer  = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tied'
    if is_win(user, computer):
        return "You won !"
    return "You lost !"

def is_win(player, opponent):
    if(player =='r' and opponent=='s') or (player =='s' and opponent=='p') \
        or (player =='p' and opponent=='r'):
        return True
    else:
        return False
# print(play())


# Hangman Game
import string
from words import words
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word  = get_valid_word(words).upper()
    word_letter = set(word) #letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 5
    while len(word_letter) > 0 and lives > 0:
        print(f'\nYou have {lives} remaining, and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in  word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1
                print(f'Letter is not in the word, you have {lives} tries remaining :(')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
    if lives > 0:
        print('\nWoahhoo! You have guessed the word!!', word, '\n')
    else:
        print('\nUff! You couldn\'t guessed the word :( The word was:', word, '\n')
hangman()
# user_input = input("")


# TIC TAC TOE
# Check tit-tac-toe folder
    
