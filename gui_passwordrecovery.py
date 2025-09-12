from tkinter import *
from tkinter import messagebox
from dbcomms import *
from securepass import *

def main():

    def retrieve_password():
        website = website_entry.get()
        username = username_entry.get()
        key = key_entry.get()

        values = (website, username)

        if all((website, username, key)):
            data = password_recovery(values)
            if not data:
                messagebox.showerror(title="Error", message="Login Failed")
            else:
                plaintext_password = decrypt_password(data, key)
                if plaintext_password:
                    messagebox.showinfo(title="Success", message=f"Password Recovered: {plaintext_password}")
                else:
                    messagebox.showerror(title="Error", message="Password Recovery Failed")
        else:
            messagebox.showerror(title="Error", message="All fields required")



    window = Tk()
    window.title("Password Recovery")
    window.config(padx=20, pady=20)

    website_label = Label(window, text="Website:")
    website_label.grid(row=0, column=0, sticky='w')
    username_label = Label(window, text="Username:")
    username_label.grid(row=1, column=0, sticky='w')
    key_label = Label(window, text="Access Key:")
    key_label.grid(row=2, column=0, sticky='w')


    website_entry = Entry(width=43)
    website_entry.grid(row=0, column=1, sticky='w')
    website_entry.insert(END, "https://www.")
    website_entry.focus()
    username_entry = Entry(width=43)
    username_entry.grid(row=1, column=1, sticky='w')
    key_entry = Entry(width=43)
    key_entry.grid(row=2, column=1, sticky='w')
    key_entry.insert(END, "Rk1Jb2d6a1pZVzRrY0dBMFV5U3p6Zz09") # You should never do this in real-world (duh)

    recover_password = Button(window, text="Recover password", width=36, command=retrieve_password)
    recover_password.grid(row=3, column=1, sticky='w')



    window.mainloop()