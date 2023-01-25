from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    Entry3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = Entry1.get()
    email = Entry2.get()
    password = Entry3.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Oppss", message="lütfen boşlukları doldurunuz")
    else:
        try:
            with open("file.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("file.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("file.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            Entry1.delete(0, END)
            Entry3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


screen = Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
photo_imgage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_imgage)
canvas.grid(column=2, row=0)

# Label1
Label1 = Label(text="Website", font=("Arial", 18, "bold"))
Label1.grid(column=1, row=1)
# Label2
Label2 = Label(text="Email/Username", font=("Arial", 18, "bold"))
Label2.grid(column=1, row=2)
# Label3
Label3 = Label(text="Password", font=("Arial", 18, "bold"))
Label3.grid(column=1, row=3)

# Entry1
Entry1 = Entry(width=38)
Entry1.grid(column=2, row=1, columnspan=2)
Entry1.focus()
# Entry2
Entry2 = Entry(width=38)
Entry2.grid(column=2, row=2, columnspan=2)
Entry2.insert(0, "ugurcan890@gmail.com")
# Entry3 buraya ekleme yapcan
Entry3 = Entry(width=21)
Entry3.grid(column=2, row=3)

# Button1
Button1 = Button(text="Generate Password", command=generate_password)
Button1.grid(column=3, row=3)
# Button2
Button2 = Button(text="Add", width=36, command=save)
Button2.grid(column=2, row=4, columnspan=2)


screen.mainloop()
