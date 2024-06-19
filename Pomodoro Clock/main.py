from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	countdown(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
	canvas.itemconfig(timer_text, text=count)
	while count > 0:
		window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="05:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label.grid(row=1, column=2)
countdown(5)
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=3, column=1)

reset = Button(text="Reset", highlightthickness=0)
reset.grid(row=3, column=3)

label_check = Label(text="✔", bg=YELLOW, fg=GREEN)
label_check.grid(row=4, column=2)

window.mainloop()
