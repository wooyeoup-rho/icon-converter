import os, sys
from tkinter import *
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image

# CONSTANTS
BACKGROUND = "#D9D9D9"
FONT = "Tahoma"

# ---------------------------- RESOURCE PATH ------------------------------- #
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# FUNCTIONS
def convert_to_ico(file_path):
    try:
        image = Image.open(file_path)

        directory, file_name = os.path.split(file_path)
        name, extension = os.path.splitext(file_name)
        ico_path = os.path.join(directory, f"{name}.ico")

        image.save(ico_path, format="ICO", sizes=[icon_size])
        result_label.config(text=f"Converted to icon")
    except Exception as e:
        result_label.config(text="Error (no I won't elaborate)")
        print(f"Exception:\t{e}")

def on_drop(event):
    file_path = event.data

    if os.path.isfile(file_path):
        convert_to_ico(file_path)
    else:
        result_label.config(text="Invalid file")

def set_size(s):
    global icon_size, active_button
    icon_size = (s, s)

    if active_button:
        active_button.config(relief=RAISED, fg="black")

    active_button = buttons[s]
    active_button.config(relief=SUNKEN, fg="gray")

# UI
icon_size = (256, 256)
active_button = None

window = TkinterDnD.Tk()
window.title("ICO Converter")
window.config(padx=20, pady=20, bg=BACKGROUND)
window.minsize(300, 240)

for i in range(1, 7):
    window.rowconfigure(i, pad=5)
window.rowconfigure(0, pad=20)
window.columnconfigure(0, pad=50)

icon_photo = PhotoImage(file=resource_path("assets/images/icon.png"))
window.iconphoto(False, icon_photo)

target_photo = PhotoImage(file=resource_path("assets/images/target.png"))
canvas = Canvas(width=128, height=128, bg=BACKGROUND, highlightthickness=0)
canvas.create_image(0,0,anchor="nw", image=target_photo)
canvas.grid(row=1, column=0, rowspan=5)

title_label = Label(window, text="Drag and drop an image", font=(FONT, 12, "bold"), bg=BACKGROUND)
title_label.grid(row=0, column=0, columnspan=2)

result_label = Label(window, text="", font=(FONT, 8), bg=BACKGROUND)
result_label.grid(row=6, column=0, columnspan=2)

sizes = [16, 32, 64, 128, 256]
buttons = {}

row_count = 1
for size in sizes:
    button = Button(window, text=f"{size}x{size}", font=(FONT, 8), command=lambda s=size: set_size(s), width=10)
    button.grid(row=row_count, column=1, sticky="e")
    row_count += 1
    buttons[size] = button

default_size = 64
default_button = buttons[default_size]
set_size(default_size)
default_button.config(relief=SUNKEN)

window.drop_target_register(DND_FILES)
window.dnd_bind("<<Drop>>", on_drop)

window.mainloop()