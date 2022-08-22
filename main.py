from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip


def generate_password():

    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = random.randint(8, 10)
    rand_numbers = random.randint(2, 4)
    rand_symbols = random.randint(2, 4)

    password_list = []

    for _ in range(rand_letters):
        password_list.append(random.choice(letters))

    for _ in range(rand_numbers):
        password_list.append(random.choice(numbers))

    for _ in range(rand_symbols):
        password_list.append(random.choice(symbols))
    
    random.shuffle(password_list)

    password = ''.join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


def add_password():
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website_input.get():{
            'email': email,
            'password': password,
        }
    }

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title='Error', message='Please input all fields')
        
    else:
        with open('data.json', 'r') as file:
            data = json.load(file)
            data.update(new_data)
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)
                

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=300)
lock_img = PhotoImage(file='img.png')
canvas.create_image(180, 150, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', font=('Arial', 10))
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:', font=('Arial', 10))
email_label.grid(column=0, row=2)

password_label = Label(text='Password:', font=('Arial', 10))
password_label.grid(column=0, row=3)

website_input = Entry(width=75)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=75)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, '@gmail.com')

password_input = Entry(width=49)
password_input.grid(column=1, row=3)

generate_button = Button(text='Generate Password', width=20, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=65, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()