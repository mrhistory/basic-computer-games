# Python implementation of AceyDucey by Bill Palmby from BASIC Computer Games (1978)

import platform
import os
import random
import sys

bet = 0
user_bank = 100
first_card = 0
second_card = 0
final_card = 0

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_title_card():
    clear_screen()
    print('\tACEY DUCEY CARD GAME')
    print('CREATIVE COMPUTING MORRISTOWN, NEW JERSEY')
    print('\n\n')
    print('ACEY-DUCEY IS PLAYED IN THE FOLLOWING MANNER')
    print('THE DEALER (COMPUTER) DEALS TWO CARDS FACE UP')
    print('YOU HAVE AN OPTION TO BET OR NOT BET DEPENDING')
    print('ON WHETHER OR NOT YOU FEEL THE CARD WITH HAVE')
    print('A VALUE BETWEEN THE FIRST TWO.')
    print('IF YOU DO NOT WANT TO BET, INPUT A 0')

def print_user_dollars():
    print('\n')
    print(f'YOU HAVE {user_bank} DOLLARS')

def print_card_value(card):
    if card == 11:
        print('JACK')
    elif card == 12:
        print('QUEEN')
    elif card == 13:
        print('KING')
    elif card == 14:
        print('ACE')
    else:
        print(card)

def deal_two_cards():
    global first_card
    global second_card
    print('\n')
    print('HERE ARE YOUR NEXT TWO CARDS')
    first_card = random.randint(2, 14)
    second_card = random.randint(2, 14)
    while first_card >= second_card:
        first_card = random.randint(2, 14)
        second_card = random.randint(2, 14)
    print_card_value(first_card)
    print_card_value(second_card)

def take_bet():
    global bet
    print('\n')
    bet = int(input('WHAT IS YOUR BET? '))
    
    while bet > user_bank:
        print('SORRY, MY FRIEND, BUT YOU BET TOO MUCH')
        print(f'YOU HAVE ONLY {user_bank} DOLLARS TO BET')
        print('\n')
        bet = input('WHAT IS YOUR BET? ')
    
    if bet == 0:
        print('CHICKEN!!')
        main()
        
def deal_final_card():
    global final_card
    final_card = random.randint(2, 14)
    while final_card == first_card or final_card == second_card:
        final_card = random.randint(2, 14)
    print_card_value(final_card)

def evaluate_cards():
    global user_bank
    if (final_card > first_card and final_card < second_card) \
    or (final_card < first_card and final_card > second_card):
        print('YOU WIN!!!')
        user_bank += bet
    else:
        print('SORRY, YOU LOSE')
        user_bank -= bet

def evaluate_user_bank():
    global user_bank
    if user_bank > 0:
        main()
    else:
        print_user_dollars()
        print('\n')
        print('SORRY, FRIEND, BUT YOU BLEW YOUR WAD')
        try_again = input('TRY AGAIN? (YES OR NO)')
        
        if try_again.lower() == 'yes':
            user_bank = 100
            main()
        else:
            exit()

def exit():
    print('OK. HOPE YOU HAD FUN!')
    sys.exit(0)

def main():
    print_user_dollars()
    deal_two_cards()
    take_bet()
    deal_final_card()
    evaluate_cards()
    evaluate_user_bank()

def init():
    print_title_card()
    main()

init()