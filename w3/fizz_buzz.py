# learnTogether Week 3

def fizz_buzz(num):
    if (num % 3) == 0 and (num % 5) == 0:
        return 'FizzBuzz'
    elif (num % 3) == 0:
        return 'Fizz'
    elif (num % 5) == 0:
        return 'Buzz'
    else:
        return num

flag = True
while flag:
    print('\nPlease enter an integer number: ', end = '')
    number = int(input())
    print(fizz_buzz(number))

    print('\nDo you want the program to run again? (Yes, press y. No, press n.): ', end = '')
    myKey = input()
    
    if myKey != 'y':
        flag = False
        print('Exit the app')
