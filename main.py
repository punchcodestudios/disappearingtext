from tkinter import *

BLACK = "#000000"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"
timer = None

def reset():
    window.after_cancel(timer)

def start_timer():
    count_down(5)

def count_down(seconds):
    global timer
    timer = window.after(1000, count_down, seconds - 1)
    if int(seconds) == 0:
        clear_text()
        reset()

def clear_text():
    text_input.delete("1.0", END)

# ---------------------------- SETUP ------------------------------- #
window = Tk()
window.title("Disappearing Text")
window.config(pady=80, padx=100, bg=WHITE)

def key_handler(event):
    print(event.char)
    if timer:
        reset()
    start_timer()
window.bind('<Key>', key_handler)

header = Label(window)
header.config(text="Your text will be erased if you stop typing for five seconds", fg=BLACK, bg=WHITE, font=(FONT_NAME, 18, "bold"))
header.grid(row=0, column=1)

text_input = Text()
text_input.grid(row=1, column=1)


window.mainloop()
