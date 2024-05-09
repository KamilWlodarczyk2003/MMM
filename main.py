import os
from tkinter import *

BG_COLOR = "#f7e8bc"
TEXT_COLOR = "#141414"
INPUT_COLOR = "#5e5c5c"

window = Tk()
window.title("Projekt MMM")
window.config(bg=BG_COLOR)
window.geometry("900x700")

main_title = Label(text="Projekt MMM - zadanie 6", font=("Coco Gothic", 30, 'bold'), fg=TEXT_COLOR, bg=BG_COLOR)
main_title.place(x=200, y=10)

main_photo_canvas = Canvas(width=850, height=286, bg="black", highlightthickness=0)
exc_img = PhotoImage(file="exc.png")
main_photo_canvas.create_image(425, 143, image=exc_img)
main_photo_canvas.place(x=25, y=120)

m1_entry = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
m1_entry.place(x=730, y=230)
m1_text = Label(text= "W kg", fg="black")
m1_text.place(x=730, y = 250)

m2_entry = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
m2_entry.place(x=730, y=335)

window.mainloop()