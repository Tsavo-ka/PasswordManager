from tkinter import *
from tkinter import messagebox
from dbcomms import *
from securepass import *

def main():

    def check_values():
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        values = (website, username)

        if all((website, username, password)):
            data = retrieve_data(values)
            if not data:
                messagebox.showerror(title="Error", message="Login Failed")
            else:
                correct_login = hash_check(data[0][3], data[0][2], password)
                if correct_login:
                    messagebox.showinfo(title="Success", message="Login successful")
                else:
                    messagebox.showerror(title="Error", message="Login failed")
        else:
            messagebox.showerror(title="Error", message="All fields required")



    window = Tk()
    window.title("Login")
    window.config(padx=20, pady=20)

    website_label = Label(window, text="Website:")
    website_label.grid(row=1, column=0, sticky='w')
    username_label = Label(window, text="Username:")
    username_label.grid(row=2, column=0, sticky='w')
    password_label = Label(window, text="Password:")
    password_label.grid(row=3, column=0, sticky='w')


    website_entry = Entry(width=43)
    website_entry.grid(row=1, column=1, sticky='w')
    website_entry.insert(END, "https://www.")
    website_entry.focus()
    username_entry = Entry(width=43)
    username_entry.grid(row=2, column=1, sticky='w')
    password_entry = Entry(width=43)
    password_entry.grid(row=3, column=1, sticky='w')

    login_button = Button(window, text="Login", width=36, command=check_values)
    login_button.grid(row=4, column=1, sticky='w')

    window.mainloop()