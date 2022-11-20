import random
import time
from GuessGame import guessgame1, guessgame2, guessgame3, guessgame4, guessgame5
from MemoryGame import memorygame1, memorygame2, memorygame3, memorygame4, memorygame5


def welcome():
    name = input("Please Enter Your name Here: ")
    print("Hello", name, "and welcome to the World of Games (WoG)""\n""Here you can find many cool games to play.""\n")



def load_game():
    choose_a_game = input("Please choose a game to play:""\n""1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back""\n""2. Guess Game - guess a number and see if you chose like the computer""\n""3. Currency Roulette - try and guess the value of a random amount of USD in ILS""\n")

    input_difficulty = input("Please choose game difficulty from 1 to 5:")

#Memory Game
    if choose_a_game == '1' and input_difficulty == '1':
        return memorygame1()
    if choose_a_game == '1' and input_difficulty == '2':
        return memorygame2()
    if choose_a_game == '1' and input_difficulty == '3':
        return memorygame3()
    if choose_a_game == '1' and input_difficulty == '4':
        return memorygame4()
    if choose_a_game == '1' and input_difficulty == '5':
        return memorygame5()
#Guess Game
    if choose_a_game == '2' and input_difficulty == '1':
        return guessgame1()
    if choose_a_game == '2' and input_difficulty == '2':
        return guessgame2()
    if choose_a_game == '2' and input_difficulty == '3':
        return  guessgame3()
    if choose_a_game == '2' and input_difficulty == '4':
        return  guessgame4()
    if choose_a_game == '2' and input_difficulty == '5':
        return guessgame5()

#Currency Game
    if choose_a_game == '3':
        return currencygame()




def currencygame():
    print("c")
