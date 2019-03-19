# Program: SQL Login Page
# Date 11/03/2019
# Author: Emile
from tkinter import *
from tkinter import messagebox as mb
import sqlite3

DATABASE = 'Database/login.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

# Create Window
window = Tk()
window.title("Login")
window.geometry("400x400")
window.resizable(False, False)

# Global variables
user_email = ""

# Button Functions
def exitButton():
    window.quit()
    window.destroy()
    db.close()
    exit()

def loginButton():
    # Take the values of the username and password fields
    username_output = username_box.get()
    password_output = password_box.get()

    # Check if these values match in the database
    user_check = "SELECT * FROM user WHERE username = ? AND password = ?"
    cursor.execute(user_check, [username_output, password_output])
    user_check_result = cursor.fetchall()

    # If the username and password are present in the database, log in the user
    if user_check_result:
        welcome_message = Label(window, width=20, text="Hello "+user_check_result[0][3], font=("bold", 20))
        welcome_message.place(x=40, y=300)
    elif username_output == "" or password_output == "":
        mb.showwarning("Warning", "Please fill out all fields")
    elif username_output != "" and password_output != "":
        mb.showerror("Error", "Incorrect Username or Password")
    else:
        mb.showerror("Error", "Something went wrong, please try again")

def forgotPasswordButton():
    mb.showinfo("Info", "Please enter your email")
    forgot_password_entry = Entry(window, width=25, bd=2)
    forgot_password_entry.place(x=90, y=300)
    submit_email = Button(window, text="Submit", width=15, command=submitEmail, bg="gray")
    submit_email.place(x=250, y=295)
     = forgot_password_entry.get()


def submitEmail():
    #smtpObj = smtplib.SMTP('localhost')
    #smtpObj.sendmail(sender, receivers, message)
    mb.showinfo("Info", "An email with your password has been sent to")



# ------ Widgets ------

# Labels
indicator_label = Label(window, width=20, text="SQL Login", font=("bold", 20))
indicator_label.place(x=40, y=30)
username_label = Label(window, width=20, text="Username:", font=("bold", 12))
username_label.place(x=0, y=100)
password_label = Label(window, width=20, text="Password:", font=("bold", 12))
password_label.place(x=0, y=150)

# Buttons
login_button = Button(window, text="Log In", width=30, command=loginButton, bg="red")
login_button.place(x=90, y=200)
exit_button = Button(window, text="Exit", width=30, command=exitButton, bg="red")
exit_button.place(x=90, y=250)
forgot_password_button = Button(window, text="Forgot Password?", width=15, command=forgotPasswordButton, bg="gray", font=("italic", 7))
forgot_password_button.place(x=280, y=175)

# Input Boxes
username_box = Entry(window, width=30, bd=3)
username_box.place(x=140, y=100)
password_box = Entry(window, width=30, bd=3, show="*")
password_box.place(x=140, y=150)



# Main Loop
window.mainloop()
