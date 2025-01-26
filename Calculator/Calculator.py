from tkinter import *

# Create the main window
win = Tk()
win.title("Calculator")
win.geometry("400x500")
win.resizable(0, 0)

# Function to handle button click and update the expression
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)

# Function to remove the last character from the expression
def btn_backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

# Function to evaluate the expression and display the result
def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Function to handle key events
def key_event(event):
    key = event.keysym
    if key in '0123456789':
        btn_click(key)
    elif key == 'plus':
        btn_click('+')
    elif key == 'minus':
        btn_click('-')
    elif key == 'asterisk':
        btn_click('*')
    elif key == 'slash':
        btn_click('/')
    elif key == 'Return':
        btn_equal()
    elif key == 'BackSpace':
        btn_backspace()
    elif key == 'c':
        btn_clear()

# Initialize the expression variable
expression = ""
input_text = StringVar()

# Create the input frame
input_frame = Frame(win, width=312, height=50)
input_frame.pack(side=TOP)

# Create the input field inside the input frame
input_field = Entry(input_frame, font=('arial', 18, 'bold'), width=25, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0, ipady=10, padx=10, pady=10)
input_field.bind("<Return>", lambda event: btn_equal())  # Bind Enter key to btn_equal

# Bind keys
win.bind('<Key>', key_event)

# Create the buttons frame
btns_frame = Frame(win, width=310, height=270)
btns_frame.pack()

# Row 0 buttons
clear = Button(btns_frame, text='C', width=22, height=3, command=lambda: btn_clear()).grid(row=0, column=0, columnspan=2, padx=1, pady=1)
backspace = Button(btns_frame, text='⌫', width=10, height=3, command=lambda: btn_backspace()).grid(row=0, column=2, padx=1, pady=1)
divide = Button(btns_frame, text='/', width=10, height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

# Row 1 buttons
seven = Button(btns_frame, text='7', width=10, height=3, command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text='8', width=10, height=3, command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text='9', width=10, height=3, command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text='*', width=10, height=3, command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)

# Row 2 buttons
four = Button(btns_frame, text='4', width=10, height=3, command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text='5', width=10, height=3, command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text='6', width=10, height=3, command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text='-', width=10, height=3, command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)

# Row 3 buttons
one = Button(btns_frame, text='1', width=10, height=3, command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text='2', width=10, height=3, command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text='3', width=10, height=3, command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text='+', width=10, height=3, command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

# Row 4 buttons
zero = Button(btns_frame, text='0', width=22, height=3, command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
decimal = Button(btns_frame, text='.', width=10, height=3, command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text='=', width=10, height=3, command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

# Run the main loop
win.mainloop()