from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('650x354')


def click(item):
    global expresie

    expresie += str(item)
    input_text.set(expresie)


def stergere():
    global expresie
    expresie = ""
    input_text.set("")


def egalitate():
    global expresie
    try:
        if expresie != "":
            rezultat = str(eval(expresie))
            input_text.set(rezultat)
            expresie = ""
    except ZeroDivisionError:
        expresie = ""
        input_text.set("Eroare! Te rugam sa apesi tasta C")



expresie = ''
input_text = StringVar()
input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('Comic Sans MS', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()


frame_butoane = Frame(window, width=500, height=304, bg='grey')
frame_butoane.pack()


Button(frame_butoane, text='C', font=('Comic Sans MS', 9, 'bold'), width=64, height=3, bg='#eee', cursor='hand2', command=lambda: stergere()).grid(row=0, columnspan=3, column=0)
Button(frame_butoane, text='/', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#FFA500", cursor='hand2', command=lambda: click('/')).grid(row=0, column=3)

Button(frame_butoane, text='7', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('7')).grid(row=1, column=0)
Button(frame_butoane, text='8', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('8')).grid(row=1, column=1)
Button(frame_butoane, text='9', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('9')).grid(row=1, column=2)
Button(frame_butoane, text='6', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('6')).grid(row=2, column=0)
Button(frame_butoane, text='5', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('5')).grid(row=2, column=1)
Button(frame_butoane, text='4', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('4')).grid(row=2, column=2)
Button(frame_butoane, text='3', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('3')).grid(row=3, column=0)
Button(frame_butoane, text='2', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('2')).grid(row=3, column=1)
Button(frame_butoane, text='1', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('1')).grid(row=3, column=2)

Button(frame_butoane, text='0', font=('Comic Sans MS', 9, 'bold'), width=42, height=3, bg="#eee", cursor='hand2', command=lambda: click('0')).grid(row=4, column=0, columnspan= 2)
Button(frame_butoane, text='.', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#eee", cursor='hand2', command=lambda: click('.')).grid(row=4, column=2)
Button(frame_butoane, text='=', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#FFA500", cursor='hand2', command=lambda: egalitate()).grid(row=4, column=3)
Button(frame_butoane, text='', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#FFA500", cursor='hand2', command=lambda: click('')).grid(row=1, column=3)
Button(frame_butoane, text='-', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#FFA500", cursor='hand2', command=lambda: click('-')).grid(row=2, column=3)
Button(frame_butoane, text='+', font=('Comic Sans MS', 9, 'bold'), width=20, height=3, bg="#FFA500", cursor='hand2', command=lambda: click('+')).grid(row=3, column=3)



window.mainloop()
