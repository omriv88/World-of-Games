import random

def guessgame1():
    print("Hi Wellcome to Guess Game Difficulty 1")
    generate_number = random.randint(1, 2)
    number_from_user = int(input('please generate number between 1 to 2: '))
    if number_from_user == generate_number:
        print("True")
    else:
        print("False")
def guessgame2():
    print("Hi Wellcome to Guess Game Difficulty 2")
    generate_number = random.randint(1, 2)
    number_from_user = int(input('please generate number between 1 to 2: '))
    if number_from_user == generate_number:
        print("True")
    else:
        print("False")

def guessgame3():
    print("Hi Wellcome to Guess Game Difficulty 3")
    generate_number = random.randint(1, 3)
    number_from_user = int(input('please generate number between 1 to 3: '))
    if number_from_user == generate_number:
        print("True")
    else:
        print("False")

def guessgame4():
    print("Hi Wellcome to Guess Game Difficulty 4")
    generate_number = random.randint(1, 4)
    number_from_user = int(input('please generate number between 1 to 4: '))
    if number_from_user == generate_number:
        print("True")
    else:
        print("False")

def guessgame5():
    print("Hi Wellcome to Guess Game Difficulty 5")
    generate_number = random.randint(1, 5)
    number_from_user = int(input('please generate number between 1 to 5: '))
    if number_from_user == generate_number:
        print("True")
    else:
        print("False")
