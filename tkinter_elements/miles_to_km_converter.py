from tkinter import *


def converter():
	miles_value = miles.get()
	km_val = round(int(miles_value) * 1.60934, 2)
	km_value.config(text=km_val)


window = Tk()
window.title("Miles to Km Convertor")
window.config(padx=20, pady=20)

# Label
my_label = Label(text="is equal to", font=("Arial", 10, "normal"))
my_label.grid(column=1, row=2)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 10, "normal"))
miles_label.grid(column=3, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 10, "normal"))
km_label.grid(column=3, row=2)

# Km value
km_value = Label(text="0", font=("Arial", 10, "normal"))
km_value.grid(column=2, row=2)

# Button
button = Button(text="Calculate", command=converter)
button.grid(column=2, row=3)

# Entry
miles = Entry(width=10)
miles.grid(column=2, row=1)

window.mainloop()
