from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
session_state = "work"
work_sessions = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, session_state, work_sessions
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    label["text"] = "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    session_state = "work"
    work_sessions = 0
    update_timer_text()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global session_state, work_sessions
    work_sessions += 1
    if work_sessions % 8 == 0:
        session_state = "long_break"
        label["text"] = "Long_break"
        countdown(LONG_BREAK_MIN * 60)
    elif work_sessions % 2 == 0:
        session_state = "short_break"
        label["text"] = "Short_break"
        countdown(SHORT_BREAK_MIN * 60)
    else:
        session_state = "Work_Time"
        label["text"] = "Work_time"
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


def update_timer_text():
    if session_state == "Work_Time":
        canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
    elif session_state == "short_break":
        canvas.itemconfig(timer_text, text=f"{SHORT_BREAK_MIN}:00")
    elif session_state == "long_break":
        canvas.itemconfig(timer_text, text=f"{LONG_BREAK_MIN}:00")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label.grid(row=1, column=2)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=3, column=1)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=3, column=3)

label_check = Label(text="✔", bg=YELLOW, fg=GREEN)
label_check.grid(row=4, column=2)

update_timer_text()

window.mainloop()
