from tkinter import *
from tkinter import messagebox
import pyperclip
import random


# ---------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
			   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['@', '!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '.']

	nr_letters = random.randint(6, 8)
	nr_symbols = random.randint(2, 4)
	nr_numbers = random.randint(2, 4)

	password_list = [random.choice(letters) for _ in range(nr_letters)]
	password_list += [random.choice(symbols) for _ in range(nr_symbols)]
	password_list += [random.choice(numbers) for _ in range(nr_numbers)]

	random.shuffle(password_list)

	password = "".join(password_list)

	pyperclip.copy(password)

	pass_entry.delete(0, END)
	pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
	website = website_entry.get()
	mail = mail_entry.get()
	password = pass_entry.get()

	if len(website) == 0 or len(password) == 0 or len(mail) == 0:
		messagebox.showinfo(title="Missing Info", message="Please make sure you haven't left any fields empty")
	else:
		is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \nEmail: {mail} \nPassword: {password}\nIs the information correct?")
		if is_ok:
			with open("passwords.txt", "a") as file:
				file.write(f"{website} | {mail} | {password}\n")
				website_entry.delete(0, END)
				pass_entry.delete(0, END)
				website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

website_entry = Entry(width=53)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()

mail_label = Label(text="Email/Username:")
mail_label.grid(column=1, row=3)

mail_entry = Entry(width=53)
mail_entry.grid(column=2, row=3, columnspan=2)
mail_entry.insert(index=END, string="harshitgoyal780p@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=1, row=4)

pass_entry = Entry(width=34)
pass_entry.grid(column=2, row=4)

pass_generate_button = Button(text="Generate Password", command=generate_password)
pass_generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=45, command=save_password)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
