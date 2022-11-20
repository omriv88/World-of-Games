import random
import time

def memorygame1():
    r = input('Wellcome to The Memory Game difficult level 1 \nWe will show you 1 number for a short time, you will have to identify the number preese 1 if you ready')
    if r == 1:
        return
    generate_sequence = random.randint(1, 9)
    print(generate_sequence)
    time.sleep(0.7)
    for i in range(0, 100):
        print(' ')
    get_list_from_user = int(input('what is the number?: '))
    if get_list_from_user == generate_sequence:
        print("True")
    else:
        print("False")


def memorygame2():
    r = input('Wellcome to The Memory Game difficult level 2 \nWe will show you 2 numbers for a short time, you will have to identify the number preese 1 if you ready')
    if r == 1:
        return
    generate_sequence = random.randint(10, 99)
    print(generate_sequence)
    time.sleep(0.7)
    for i in range(0, 100):
        print(' ')
    get_list_from_user = int(input('what is the number?: '))
    if get_list_from_user == generate_sequence:
        print("True")
    else:
        print("False")

def memorygame3():
    r = input('Wellcome to The Memory Game difficult level 3 \nWe will show you 3 numbers for a short time, you will have to identify the number preese 1 if you ready')
    if r == 1:
        return
    generate_sequence = random.randint(101, 999)
    print(generate_sequence)
    time.sleep(0.7)
    for i in range(0, 100):
        print(' ')
    get_list_from_user = int(input('what is the number?: '))
    if get_list_from_user == generate_sequence:
        print("True")
    else:
        print("False")

def memorygame4():
    r = input('Wellcome to The Memory Game difficult level 4 \nWe will show you 4 numbers for a short time, you will have to identify the number preese 1 if you ready')
    if r == 1:
        return
    generate_sequence = random.randint(1001, 9999)
    print(generate_sequence)
    time.sleep(0.7)
    for i in range(0, 100):
        print(' ')
    get_list_from_user = int(input('what is the number?: '))
    if get_list_from_user == generate_sequence:
        print("True")
    else:
        print("False")

def memorygame5():
    r = input('Wellcome to The Memory Game difficult level 5 \nWe will show you 5 numbers for a short time, you will have to identify the number preese 1 if you ready')
    if r == 1:
        return
    generate_sequence = random.randint(10001, 99999)
    print(generate_sequence)
    time.sleep(0.7)
    for i in range(0, 100):
        print(' ')
    get_list_from_user = int(input('what is the number?: '))
    if get_list_from_user == generate_sequence:
        print("True")
    else:
        print("False")
