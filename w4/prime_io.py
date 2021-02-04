# learnTogether Week 4

def isPrime_1(num):
    for i in range(2, num//2 + 2):
        if (num % i) == 0:
            return False
    return True

def isPrime_2(num) : 

    if (num <= 1) : 
        return False
    if (num <= 3) : 
        return True

    if (num % 2 == 0 or num % 3 == 0) : 
        return False

    i = 5
    while(i * i <= num) : 
        if (num % i == 0 or num % (i + 2) == 0) : 
            return False
        i += 6

    return True

def getInput(message):
    while True:
        try:
            num = int(input(message))
            if num > 1:
                return num;
        except:
            print ('You have entered an invalid value.')
        else:
            print('The number must be positive and greater than one.')

while True:
    startNumber = getInput('\nPlease enter an integer number as starting number: ')
    endNumber = getInput('\nPlease enter an integer number as ending number: ')

    print('\n========== Result ==========')

    if (startNumber > endNumber):
        print('Starting number is greater than ending number')
    else:
        print('Run the program in two ways:')
        print('\n==> The first way.')
        for num in range(startNumber, endNumber + 1):
            if (isPrime_1(num)): 
                print(str(num) + ' is a prime.')

        print('\n==> The second way. (Optimized Method)')
        for num in range(startNumber, endNumber + 1):
            if (isPrime_2(num)): 
                print(str(num) + ' is a prime.')

    myKey = input('\nDo you want the program to run again. (Yes, press y. No, any key): ')
    
    if myKey != 'y':
        print('Exit the app')
        break;
        