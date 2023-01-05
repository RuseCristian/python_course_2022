

from tkinter import *
import pandas as pd

excel_data = pd.read_excel('CompetitiiSah.xlsx')
print(excel_data.iloc[2])


root = Tk()


frame = Frame(root)
frame.pack()

data = "test."


def print_data():
    print("Data: ", data)


def edit_data():
    data = "edited data"


def save_data():
    # Save the data here
    with open("data.txt", "w") as f:
        f.write(data)


print_button = Button(frame, text="Print Data", command=print_data)
print_button.pack(side=LEFT)


edit_button = Button(frame, text="Edit Data", command=edit_data)
edit_button.pack(side=LEFT)


save_button = Button(frame, text="Save Data", command=save_data)
save_button.pack(side=LEFT)


root.mainloop()
