from tkinter import *


# ---------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

	website = website_entry.get()
	mail = mail_entry.get()
	password = pass_entry.get()

	with open("passwords.txt", "a") as file:
		file.write(f"{website} | {mail} | {password}\n")
		website_entry.delete(0, END)
		pass_entry.delete(0, END)


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
