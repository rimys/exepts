
import json

filename = 'fav_num.json'

def num_input():
    fav_num_import = input('What is your favorite number? Enter: ')
    with open(filename, 'w') as f:
        json.dump(fav_num_import, f)


def core():
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        num_input()
    else:
        print(f'Your favorite numder is: {fav_num}')

def check_exist():
    with open(filename) as f:
        check = json.load(f)
        inz = input(f'Is your favorite number {check}? Answer (y/n):')
        if inz == 'y':
            print('Good')
        else:
            num_input()
    return True

core()
check_exist()