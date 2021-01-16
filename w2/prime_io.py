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
        print('Run the program in two ways:')
        print('\n==> The first way.')
        for num in range(startNumber, endNumber + 1):
            if num > 1:
                for i in range(2, num//2 + 2):
                    if (num % i) == 0:
                        break
                else:
                    print(str(num) + ' is a prime.')

        print('\n==> The second way. (Optimized Method)')
        for num in range(startNumber, endNumber + 1):
            if num <= 1:
                continue

            if num <= 3:
                print(str(num) + ' is a prime.')
                continue
                
            if (num % 2 == 0 or num % 3 == 0):
                continue

            i = 5
            while (i * i <= num): 
                if (num % i == 0 or num % (i + 2) == 0):
                    break
                i += 6
            else:
                print(str(num) + ' is a prime.')
    
    print('\nDo you want the program to run again. Yes, press y. No, press n.')
    myKey = input()
    
    if myKey != 'y':
        flag = False
        print('Exit the app')
