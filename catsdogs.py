
files = ['cats.txt', 'dogs.txt', '1.txt']
#pet_names = ''
for file in files:
    try:
        with open(file) as pet:
            pet_names = pet.read()
    except FileNotFoundError:
        #print(f'File {file} is not found')
        pass
    else:
        print(pet_names, '\n')
