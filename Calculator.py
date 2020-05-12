# import  tkinter for gui
from tkinter import *


# get number function
def btn(number):
    global operater
    operater = operater + str(number)
    textInput.set(operater)


# clear function
def clear():
    global operater
    operater = ''
    textInput.set('')
    Display.insert(0, 'Start Calculating..')


# finding the result
def equal():
    global operater
    sumup = float(eval(operater))
    textInput.set(sumup)
    operater = ''


root = Tk()
root.title("Calculator")
operater = ''
textInput = StringVar(value='Start calculating')

######################## Display Screen ########################

Display = Entry(root, font=('araial', 30, 'bold'), fg='black', bg='white', justify='right', bd='20',
                textvariable=textInput)
Display.grid(columnspan='4')

######################## Screen ########################

# Buttons

###################################### row 1
btn7 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='7', bg='green',
              command=lambda: btn(7)).grid(row=1,
                                           column=0)
btn8 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='8', bg='green',
              command=lambda: btn(8)).grid(row=1,
                                           column=1)
btn9 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='9', bg='green',
              command=lambda: btn(9)).grid(row=1,
                                           column=2)
btnC = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='C', bg='red',
              command=lambda: clear()).grid(row=1,
                                            column=3)
###################################### row 2

btn4 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='4', bg='green',
              command=lambda: btn(4)).grid(row=2,
                                           column=0)
btn5 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='5', bg='green',
              command=lambda: btn(5)).grid(row=2,
                                           column=1)
btn6 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='6', bg='green',
              command=lambda: btn(6)).grid(row=2,
                                           column=2)
btnPlus = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='+', bg='orange',
                 command=lambda: btn('+')).grid(
    row=2,
    column=3)

##################################### row 3
btn1 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='1', bg='green',
              command=lambda: btn(1)).grid(row=3,
                                           column=0)
btn2 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='2', bg='green',
              command=lambda: btn(2)).grid(row=3,
                                           column=1)
btn3 = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='3', bg='green',
              command=lambda: btn(3)).grid(row=3,
                                           column=2)
btnMinus = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='-', bg='orange',
                  command=lambda: btn('-')).grid(
    row=3,
    column=3)

#################################### row 4
btnZero = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='0', bg='green',
                 command=lambda: btn(0)).grid(row=4,
                                              column=0)
btnDot = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='.', bg='green',
                command=lambda: btn('.')).grid(row=4,
                                               column=1)
btnDivision = Button(root, padx='43', pady='15', bd='8', fg='white', font='arial,30,bold', text='/', bg='orange',
                     command=lambda: btn('/')).grid(
    row=4,
    column=2)
btnMultiply = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='X', bg='orange',
                     command=lambda: btn('*')).grid(
    row=4,
    column=3)

#################################### row 5

btnEQ = Button(root, padx='100', pady='15', bd='8', fg='white', font='arial,30,bold', text='=', bg='blue',
               command=lambda: equal()).grid(row=5,
                                             column=0,
                                             columnspan='2')
btnStBracket = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text='(', bg='orange',
                      command=lambda: btn('(')).grid(
    row=5, column=2)
btnClBracket = Button(root, padx='40', pady='15', bd='8', fg='white', font='arial,30,bold', text=')', bg='orange',
                      command=lambda: btn(")")).grid(
    row=5, column=3)

# loop the root for ui keep running.
root.mainloop()
