# learnTogether Week 2

flag = True
while flag:
    print('\nPlease enter an integer number as starting number :')
    startNumber = int(input())

    print('Please enter an integer number as ending number :')
    endNumber = int(input())

    print('\n========== Result ==========')

    if(startNumber > endNumber):
        print('Starting number is greater than ending number')
    else:
        for num in range(startNumber, endNumber + 1):
            print(num)
    
    print('\nDo you want the program to run again. Yes, press y. No, press n.')
    myKey = input()
    
    if myKey != 'y':
        flag = False
        print('Exit the app')

