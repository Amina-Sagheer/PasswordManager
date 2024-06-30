import random
from tkinter import *


def generate_password():
    """Generates a random password based on specified criteria."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random lengths for letters, symbols, and numbers
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(3, 5)

    # Select random characters from each category
    password_letters = random.sample(letters, nr_letters)
    password_numbers = random.sample(numbers, nr_numbers)
    password_symbols = random.sample(symbols, nr_symbols)

    # Combine and shuffle characters to form the password
    password_list = []
    password_list.extend(password_numbers)
    password_list.extend(password_symbols)
    password_list.extend(password_letters)
    random.shuffle(password_list)
    generated_password = ''.join(password_list)

    # Clear existing text in password_entry and insert generated password
    password_entry.delete(0, 'end')
    password_entry.insert(0, generated_password)


# Initialize tkinter window
my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx=20, pady=20)

# Canvas setup
canvas = Canvas(height=200, width=200)
image_url = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_url)
canvas.grid(column=1, row=0)

# Labels setup
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Username/Email:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries setup
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, columnspan=2, sticky="we")
website_entry.focus()
username_entry = Entry(width=30)
username_entry.grid(column=1, row=2, columnspan=2, sticky="we")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="we")


def save_data():
    """Saves website, username, and password data to a file."""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    data = f"Website : {website}, Username/Email: {username}, Password: {password}\n"

    # Write data to file and clear entry fields
    with open("data.txt", "a") as file:
        file.write(data)
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)


# Buttons setup
generate_password_button = Button(text="Generate Password", bg="white", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="we")
add_button = Button(text="Add", bg="white", width=30, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="we")

# Start the tkinter main loop
my_window.mainloop()
