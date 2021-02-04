# learnTogether Week 4

def fizz_buzz(num):
    if (num % 3) == 0 and (num % 5) == 0:
        return 'FizzBuzz'
    elif (num % 3) == 0:
        return 'Fizz'
    elif (num % 5) == 0:
        return 'Buzz'
    else:
        return num

def getInput(message):
    while True:
        try:
            num = int(input(message))
            if num >= 0:
                return num;
        except:
            print ('You have entered an invalid value.')
        else:
            print('The number must be positive')

while True:
    number = getInput('\nPlease enter an integer number: ')
    print(fizz_buzz(number))

    myKey = input('\nDo you want the program to run again. (Yes, press y. No, any key): ')
    
    if myKey != 'y':
        print('Exit the app')
        break
