if __name__ == '__main__':
    random_number_int = 50
    counter_int = 1
    print('welcome to guessing app')

while counter_int <= 10:
    guessing_number_str = input('Enter a random number: ')
    guessing_number_int = int(guessing_number_str)
    if guessing_number_int > random_number_int:
        print('input higher than the random number "try again"')
    elif guessing_number_int < random_number_int:
        print('input lesser than random number "try again"')
    elif guessing_number_int == random_number_int:
        print('perfect number')
    counter_int += 1











