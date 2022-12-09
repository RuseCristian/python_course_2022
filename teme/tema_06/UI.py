# Import the Tkinter library
from tkinter import *

# Create the main window
root = Tk()

# Create a frame to hold the buttons
frame = Frame(root)
frame.pack()

data = "test."
def print_data():
    print("Data: ", data)


def edit_data():
    # Edit the data here
    data = "edited data"


def save_data():
    # Save the data here
    with open("data.txt", "w") as f:
        f.write(data)


# Create a button to print the data
print_button = Button(frame, text="Print Data", command=print_data)
print_button.pack(side=LEFT)

# Create a button to edit the data
edit_button = Button(frame, text="Edit Data", command=edit_data)
edit_button.pack(side=LEFT)

# Create a button to save the data
save_button = Button(frame, text="Save Data", command=save_data)
save_button.pack(side=LEFT)

# Start the main event loop
root.mainloop()
