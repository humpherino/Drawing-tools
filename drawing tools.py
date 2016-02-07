
from turtle import*   # do and val are inputs for the function
from tkinter import ttk, Text

def escape():    #quit function
    app.destroy()

def calc(*args):   #Defines the movement calculation
    in_text = (input1.get()) #gets the text from input1
    try:
        movement_amount=int(in_text) #TC requires that the number be an int
    except:
        pass

        
    def TC (do,val):   #So TC is the function name - needs to be called when running the program
        do = do.upper() #converts all to CAPITAL letters
        if do =='F':
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

def fAction():
    TC('f',i)
def bAction():
    TC('b',i)
def rAction():
    TC('r',i)
def lAction():
    TC('l',i)
def uAction():
    TC('u',i)
def dAction():
    TC('d',i)
def nAction():
    TC('n',i)

if __name__ == '__main__':
    
    app = Tk() # 'app' will be on the top layer
    # Tk main frame, title and more

    app.title('Draw Controls')
    mainframe = ttk.Frame(app, padding="8 8 8 8")
    buttons = ttk.Frame(app, paddding="0 0 0 0", width=50, height=20)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    buttons.grid(column=0, row=1)

    #form components

    in_label = ttk.Label(mainframe, text="Movement Amount:")
    in_label.grid(column=0, row=0)
    input1 = Entry(mainframe, width=64, height=8)
    input1.insert("")
    input1.grid(column=0, row=4)

    #defining the buttons

    ttk.Button(buttons, text="Go", command=calc).grid(column=0, row=0)
    ttk.Button(buttons, text="Exit", command=escape).grid(column=1, row=0)
    ttk.Button(buttons, text="Pen up", command=uAction).grid(column=0, row=1)
    ttk.Button(buttons, text="Forward", command=fAction).grid(column=1, row=1)
    ttk.Button(buttons, text="Pen Down", command=dAction).grid(column=2, row=1)
    ttk.Button(buttons, text="Left", command=lAction).grid(column=0, row=2)
    ttk.Button(buttons, text="Reset", command=nAction).grid(column=1, row=2)
    ttk.Button(buttons, text="Right", command=rAction).grid(column=2, row=2)
    ttk.Button(buttons, text="Backwards", command=bAction).grid(column=1, row=3)

    input1.focus() #focus the input box upon launch
    app.bind('<Return>', calc)   #allows for use of enter key as submit
    app.bind('<Escape>', escape)

    #allow for the use of control+a to select all of the text

    app.bind('<Control-a>', ctrla)

    #infinite loop

    app.mainloop()
    
