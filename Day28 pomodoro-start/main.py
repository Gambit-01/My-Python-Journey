
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = f"00:00")
    timer_label.config(text = "TIMER",fg = GREEN)
    tick.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def time_starter():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 ==0:
        current_timing = long_break_sec
        timer_label.config(text = "Break",fg = RED)
    elif reps % 2 == 0:
        current_timing = short_break_sec
        timer_label.config(text = "Break",fg = PINK)
    else:
        current_timing = work_sec
        timer_label.config(text = "Work",fg = GREEN)

    count_down(current_timing)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        time_starter()
        marks = ""
        work_number = math.floor(reps/2)
        for num in range (work_number):
            marks += "✔"
        tick.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "Day28 pomodoro-start\omato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)


# The TIMER LABEL
timer_label = Label(text = "Timer",font = (FONT_NAME, 35, "bold"),fg = GREEN, bg = YELLOW)
timer_label.grid(row = 0, column = 1)

# Tick Label
tick = Label(font = (FONT_NAME, 15, "bold"),fg = GREEN, bg = YELLOW) 
tick.grid(row =3 , column = 1)


# Start Button
start_button = Button(text = "Start" , command = time_starter)
start_button.grid(row = 2, column = 0)

# Reset Button
reset_button = Button(text = "Reset", command = reset_timer)
reset_button.grid(row = 2, column = 2)



window.mainloop()