while True:
    try:
        a = int(input('Enter first digit: '))
        b = int(input('Enter second digit: '))
    except ValueError:
        print('Wrong input')
    else:
        print(f'Result a+b = {a+b}')
