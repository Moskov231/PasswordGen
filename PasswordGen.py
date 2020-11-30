import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector



def error():
   messagebox.showinfo("Error","No Entry Given")

def low():
    entry.delete(0, END)

    # Get the length of passowrd
    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

        # if strength selected is medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

        # if strength selected is strong
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")

# Function for generation of password


def generate():
    password1 = low()
    entry.insert(10, password1)
    return password1


# Function for submitting to database
def submit():

    random_password = entry.get()
    user_id=Login_entry.get()

    if user_id!="" and random_password!="":
        mycursor.execute("INSERT INTO passgen(login,passgen)VALUES('%s','%s')"%(user_id,random_password))
        mydb.commit()
    else:
        error()
    mydb.close()


# Main Function
try:#Database connection

    mydb = mysql.connector.connect(host='Yourhostname',
                                         database='YourDatabaseName',
                                         user='YourUserName',
                                         password='YourPassword')

    mycursor=mydb.cursor()
except:
    print("No Connection")
finally:
    # create GUI window
    root = Tk()
    var = IntVar()
    var1 = IntVar()

# Title of your GUI window
    root.title("Random Password Generator")


# password generated
    Random_password = Label(root, text="Password")
    Random_password.grid(row=1)
    Login = Label(root, text="LoginID")
    Login.grid(row=0)
    Login_entry = Entry(root)
    Login_entry.grid(row=0, column=1)
    entry = Entry(root)
    entry.grid(row=1, column=1)

# create label for length of password
    c_label = Label(root, text="Length")
    c_label.grid(row=2)

# Submit Button & Generate Button
    submit_button = Button(root, text="Submit", command=submit)
    submit_button.grid(row=0, column=3)
    generate_button = Button(root, text="Generate", command=generate)
    generate_button.grid(row=0, column=4)
#Radio button
    radio_low = Radiobutton(root, text="Low", variable=var, value=1)
    radio_low.grid(row=1, column=3, sticky='E')
    radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
    radio_middle.grid(row=1, column=4, sticky='E')
    radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
    radio_strong.grid(row=1, column=5, sticky='E')
    combo = Combobox(root, textvariable=var1)

# Combo Box
    combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
    combo.current(0)
    combo.bind('<<ComboboxSelected>>')
    combo.grid(column=1, row=2)

# start the GUI
    root.mainloop()

