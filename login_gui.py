# Program: SQL Login Page
# Date 11/03/2019
# Author: Emile & Reuben
from tkinter import *

# Create Window
window = Tk()
window.title("Login")
#window.resizable(False, False)

# Button Functions
def exitButton():
    window.quit()
    window.destroy()
    exit()

def loginButton():
    print("Wheat Biscuit")

# ------ Widgets ------

# Labels
indicator_label = Label(window, text="SQL Login")
indicator_label.grid(column=0, row=0)

# Buttons
login_button = Button(window, text="Log In", command=loginButton)
login_button.grid(column=0, row=1)
exit_button = Button(window, text="Exit", command=exitButton)
exit_button.grid(column=1, row=1)

# Input Boxes
username_box = Entry



# Main Loop
window.mainloop()
