# learnTogether Week 13

from tkinter import *

root = Tk()
root.title('Simple Calculator')
root.resizable(False, False)

flag_equal = BooleanVar(False)
flag_operator = BooleanVar(False)

e = Entry(root, font=('lucida 20 bold'), fg='darkblue', width=21, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, 0)

def button_click(number):
    if flag_equal.get():
        current = ''
        flag_equal.set(False)
    else:
        current = (e.get()).replace(',', '')
    
    e.delete(0, END)
    if (current == '0') and (number == 0):
        e.insert(0, '0')
    elif (current == '0') and (number != 0):
        e.insert(0, '{:,}'.format(number))
    else:
        e.insert(0, '{:,}'.format(int(current + str(number))))

def button_clear():
    e.delete(0, END)
    e.insert(0, 0)
    math = ''
    flag_equal.set(False)
    flag_operator.set(False)

# operator = addition / subtraction / multiplication / division
def button_operations(operator):
    flag_operator.set(True)
    first_number = (e.get()).replace(',', '')
    global f_num
    global math
    math = operator
    if first_number != '':
        f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    flag_equal.set(True)

    if not flag_operator.get():
        return

    second_number = (e.get()).replace(',', '')

    if second_number == '':
        second_number = f_num

    e.delete(0, END)

    if math == 'addition':
        x = f_num + float(second_number)
        e.insert(0, '{:,}'.format(int(x))) if x-int(x) == 0 else e.insert(0, '{:,}'.format(x))
    
    if math == 'subtraction':
        x = f_num - float(second_number)
        e.insert(0, '{:,}'.format(int(x))) if x-int(x) == 0 else e.insert(0, '{:,}'.format(x))

    if math == 'multiplication':
        x = f_num * float(second_number)
        e.insert(0, '{:,}'.format(int(x))) if x-int(x) == 0 else e.insert(0, '{:,}'.format(x))

    if math == 'division':
        if second_number != '0':
            if f_num != 0:
                x = f_num / float(second_number)
                e.insert(0, '{:,}'.format(int(x))) if x-int(x) == 0 else e.insert(0, '{:,}'.format(x))
            else:
                e.insert(0, 'Result is undefined')
        else:
            if f_num != 0:
                e.insert(0, 'Cannot divide by zero')
            else:
                e.insert(0, 'Result is undefined')


# Define buttons
button_1 = Button(root, text='❶', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(1))
button_2 = Button(root, text='❷', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(2))
button_3 = Button(root, text='❸', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(3))
button_4 = Button(root, text='❹', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(4))
button_5 = Button(root, text='❺', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(5))
button_6 = Button(root, text='❻', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(6))
button_7 = Button(root, text='❼', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(7))
button_8 = Button(root, text='❽', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(8))
button_9 = Button(root, text='❾', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(9))
button_0 = Button(root, text='⓿', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_click(0))

button_add = Button(root, text='+', fg='green', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_operations('addition'))
button_equal = Button(root, text='=', font=('lucida 19 bold'), height = 1, width = 14, command=button_equal)
button_clear = Button(root, text='Clear', fg='brown', font=('lucida 19 bold'), height = 1, width = 14, command=button_clear)

button_subtract = Button(root, text='-', fg='green', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_operations('subtraction'))
button_multiply = Button(root, text='×', fg='green', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_operations('multiplication'))
button_divide = Button(root, text='÷', fg='green', font=('lucida 20 bold'), height = 1, width = 6, command=lambda: button_operations('division'))

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()