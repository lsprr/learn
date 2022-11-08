from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry('500x500')  # width x height
window.title('Untitled GUI')
# window.config(background='#0d1117')
# photo = PhotoImage(file='C:\\')
label = Label(
    window,
    text='Untitled',
    font=('Arial', 25, 'bold'),
    fg='#0d1117',
    # bg='gray',
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    # image=photo,
    compound='bottom'
)

label.pack()

# label.place(x=0, y=0)

# icon = PhotoImage(file='logo.png')
# window.iconphoto(True, icon)

count = 0


def click():
    global count
    count += 1
    print(count)


# photo = PhotoImage(file='like.png')
button = Button(
    window,
    text='Submit',
    command=click,
    font=('Comic Sans', 15),
    fg='#00FF00',
    bg='black',
    activeforeground='#00FF00',
    activebackground='black',
    state=ACTIVE,
    # image=photo,
    compound='bottom'
)
button.pack()

window.mainloop()  # place window on computer screen, listen for events
