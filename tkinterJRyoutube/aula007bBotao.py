from tkinter import *
from random import randint
from random import choice

app = Tk()
app.title('Entry - v.0.1.0')
app.geometry('900x600')

inp = Entry(app)
inp.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

# -- create button clear --
msg = Label(app, text=' ')
msg.grid(row=2, column=0, padx=20, pady=5)


def show_input(event=None):
    input_rec = (inp.get()).split(',')
    msg.config(text=choice(input_rec))
    # msg = Label(app, text=choice(input_rec))
    # msg.grid(row=2, column=0, padx=20, pady=5)


button1 = Button(app, text='Show', command=show_input)
button1.grid(row=1, column=0, padx=20, pady=5)
button1.focus()
button1.bind('<KP_Enter>', show_input)
button1.bind('<Return>', show_input)
button1.bind('<Button-3>', show_input)

quit_button = Button(app, text='Close', command=app.quit)
quit_button.grid(row=1, column=1, padx=20, pady=5)

"""
read keys
def fun(event):
    print(event.keysym, event.keysym == 'KP_Enter')
    if event is True:
        button1.bind("<KP_Enter>", show_input)


app.bind("<KeyRelease>", fun)
"""

app.mainloop()
