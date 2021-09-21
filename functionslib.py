import gamedata as dt
import sys
import time
import os

def type_message(message, delay):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)

def chapter(name):
    os.system('cls')
    for i in dt.game[name]['dialogue']:
        type_message((i + "\n"), 0.1)
    type_message(dt.game[name]['prompt'], 0.1)
    user_input = ''
    while True:
        user_input = input(">")
        if user_input not in dt.game[name]['options']:
            print("Invalid Input")
            continue
        if user_input in dt.game[name]['options']:
            break
    chapter(dt.game[name]['switch'][user_input])

def main_menu():
    #main menu here
    print("Welcome to the Game")
    os.system("pause")
    chapter('start')