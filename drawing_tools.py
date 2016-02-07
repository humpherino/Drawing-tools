from turtle import *  # Do and val are inputs.
from tkinter import ttk, Text


def escape():  # Quit function.
    app.destroy()


def calc(*args):  # Defines the movement calculation.
    in_text = (input1.get())  # Gets the text from input1.

    try:
        movement_amount = int(in_text)  # TC requires that the number be an int
    except:
        pass


def TC(do, val):  # TC is func name, must be called when running program

    do = do.upper()  # Converts all to CAPITAL letters

    if do == 'F':
        forward(val)    # Turns a do value of F into turtle command forward
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('Duds command, you lump!')


def ctrla(*args):

    focused = mainframe.focus_get()
    focused.tag_add(SEL, "1.0", END)
    focused.mark_set(INSERT, "1.0")
    focused.see(INSERT)

    return 'break'

# humph, write a comment here explaining what this does.

def action(kind):
    TC(kind,i)

if __name__ == '__main__':

    app = Tk()  # 'app' will be on the top layer
    # Tk main frame, title and more

    app.title('Draw Controls')
    mainframe = ttk.Frame(app, padding="8 8 8 8")
    buttons = ttk.Frame(app, paddding="0 0 0 0", width=50, height=20)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    buttons.grid(column=0, row=1)

    # Form components

    in_label = ttk.Label(mainframe, text="Movement Amount:")
    in_label.grid(column=0, row=0)
    input1 = Entry(mainframe, width=64, height=8)
    input1.insert("")
    input1.grid(column=0, row=4)

    # Defining the buttons

    ttk.Button(buttons, text="Go", command=calc).grid(column=0, row=0)
    ttk.Button(buttons, text="Exit", command=escape).grid(column=1, row=0)
    ttk.Button(buttons, text="Pen up", command=lambda: action('u').grid(column=0, row=1)
    ttk.Button(buttons, text="Forward", command=lambda: action('f')).grid(column=1, row=1)
    ttk.Button(buttons, text="Pen Down", command=lambda: action('d')).grid(column=2, row=1)
    ttk.Button(buttons, text="Left", command=lambda: action('l')).grid(column=0, row=2)
    ttk.Button(buttons, text="Reset", command=lambda: action('n')).grid(column=1, row=2)
    ttk.Button(buttons, text="Right", command=lambda: action('r')).grid(column=2, row=2)
    ttk.Button(buttons, text="Back", command=lambda: action('b')).grid(column=1, row=3)

    input1.focus()  # Focus the input box upon launch
    app.bind('<Return>', calc)   # Allows for use of enter key as submit
    app.bind('<Escape>', escape)

    # Allow for the use of control+a to select all of the text

    app.bind('<Control-a>', ctrla)

    # Infinite loop

    app.mainloop()
