# learnTogether Week 3

# This program determines if three side lengths can make a triangle.

def chechTriangle(a = 3, b = 4, c = 5):
    global side1, side2, side3
    side1 = a
    side2 = b
    side3 = c

    if (a + b > c and b + c > a and c + a > b):
        return True
    else:
        return False

def resultTriangle(bol):
    if (bol):
        print('\n ==> The numbers ' + str(side1) + ', ' + str(side2) + ', ' + str(side3) + ' are the sides of a triangle.')
    else:
        print('\n    --> The numbers ' + str(side1) + ', ' + str(side2) + ', ' + str(side3) + ' can not be the sides of a triangle.')

resultTriangle(chechTriangle(7, 5, 10))
resultTriangle(chechTriangle(10, 5));
resultTriangle(chechTriangle(8, 15, 20))
resultTriangle(chechTriangle(5, 10))
resultTriangle(chechTriangle())
