from tkinter import *
import make_pass
window = Tk()

#comment for git
def get_alpha():
    listbox.delete(0, END)
    res = make_pass.alphabet_pass(int(input_len.get()))
    listbox.insert(END, res)


def get_digit():
    listbox.delete(0, END)
    res = make_pass.digit_pass(int(input_len.get()))
    listbox.insert(END, res)


def get_mixed():
    listbox.delete(0, END)
    res = make_pass.mixed_pass(int(input_len.get()))
    listbox.insert(END, res)


def copy_res():
    window.clipboard_clear()
    res = listbox.get(ACTIVE)
    window.clipboard_append(res)
    listbox.delete(0,END)
    listbox.insert(END, 'Copied to clipboard')


#Label widgets

label1 = Label(window, text='Enter length', relief=SUNKEN, borderwidth=4)
label1.grid(row=1, column=2)

label2 = Label(window, text='Select:', relief=SUNKEN, borderwidth=4)
label2.grid(row=2, column=4)


#Entry widgets

input_len = StringVar()
entry1 = Entry(window, width=10, textvariable=input_len)
entry1.grid(row=1, column=3)

#fuction buttons

button1 = Button(window, text='Get Alphabet', width=15, command=get_alpha)
button1.grid(row=1, column=5)

button2 = Button(window, text='Get Integer', width=15, command=get_digit)
button2.grid(row=2, column=5)

button3 = Button(window, text='Get Mixed', width=15, command=get_mixed)
button3.grid(row=3, column=5)

button4 = Button(window, text='Copy pass', relief=RAISED, borderwidth=6, command=copy_res)
button4.grid(row=2, column=3)

#Listbox window

listbox = Listbox(window, height=1, width=25)
listbox.grid(row=3, column=2, columnspan=3)
listbox.bind('<<ListboxSelect>>', copy_res)

window.mainloop()
