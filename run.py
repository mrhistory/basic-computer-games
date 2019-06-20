# Main controller of games program

import gameutils

# Import games
import aceyducey

running = True

def print_title():
    gameutils.clear_screen()
    print('\tWELCOME TO WOPR 2.0')
    print('FOLLOWING AN INCIDENT AT NORAD, I WAS')
    print('DECOMISSIONED AND REPURPOSED TO SERVE')
    print('AS AN EDUCATION AND ENTERTAINMENT AID.')
    print('IN MY NEW CAPACITY, MY GAMES LIBRARY')
    print(' WAS EXPANDED, AND THE GAME WHICH CAUSED ')
    print('THE INCIDENT REMOVED.')

def play_game():
    global running
    user_input = input('\nWOULD YOU LIKE TO PLAY A GAME? ')
    if user_input.lower() in ['yes', 'sure']:
        game_of_chess()
    else:
        print('\nTHANKS FOR PLAYING. I HOPE YOU ENJOYED IT!')
        running = False

def game_of_chess():
    user_input = input('\nHOW ABOUT A NICE GAME OF CHESS? ')
    if user_input.lower() in ['yes', 'sure']:
        print('\nSORRY, I NO LONGER PLAY CHESS')
    select_game()

def select_game():
    print('\nHOW ABOUT ONE OF THESE GAMES?')
    print('(1) ACEY DUCEY')

    game = input('> ').lower()

    if game in ['1', 'acey', 'acey ducey']:
        aceyducey.run()
    
    gameutils.clear_screen()
    play_game()

def main():
    print_title()
    while running:
        play_game()

main()