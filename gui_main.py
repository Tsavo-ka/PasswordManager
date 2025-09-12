from tkinter import *
from tkinter import messagebox
from dbcomms import *
from securepass import *
from passgen import *

def main():

    def generate_password():
        password_entry.delete(0, END)
        password = pass_generator()
        password_entry.insert(END, password)

    def pack_values():

        website = website_entry.get()
        username = email_entry.get()
        password = password_entry.get()
        salt, hash = hash_password(password)

        data = (website, username, salt, hash)

        if all((website, username, password)):
            try:
                write_to_table_credentials(data)
                write_to_table_securedpassword(website, username, password)
            except psycopg2.errors.UniqueViolation:
                messagebox.showerror("Error", "This user already exists for this website.")
            else:
                messagebox.showinfo("Success", "Registration successful")
        else:
            messagebox.showerror(title="Error", message="All fields are required")

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.insert(END, "https://www.")

    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=200, height=200)
    logo = PhotoImage(file='logo.png')
    canvas.create_image(100,100, image=logo)
    canvas.grid(row=0, column=1, columnspan=3, sticky='nsew')

    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0, sticky='w')
    email_label = Label(text="Email/Username:")
    email_label.grid(row=2, column=0, sticky='w')
    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0, sticky='w')
    error_label = Label(text="")
    error_label.grid(row=5, column=0, sticky='w')

    website_entry = Entry(width=43)
    website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
    website_entry.insert(END, "https://www.")
    website_entry.focus()
    email_entry = Entry(width=43)
    email_entry.grid(row=2, column=1, columnspan=2, sticky='w')
    password_entry = Entry(width=24)
    password_entry.grid(row=3, column=1, sticky='w')

    pass_gen_button = Button(text="Generate Password", command=generate_password)
    pass_gen_button.grid(row=3, column=2, sticky='e')
    add_button = Button(window, text="Add", width=36, command=pack_values)
    add_button.grid(row=4, column=1, columnspan=2, sticky='w')

    window.mainloop()