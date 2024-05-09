import os
from tkinter import *

BG_COLOR = "#f7e8bc"
TEXT_COLOR = "#141414"
INPUT_COLOR = "#5e5c5c"

def check_buttons(sin_var, skok_var):
    
    global sin
    global skok
    
    if sin_var == True:
        sin.set(True)
        skok.set(False)
    elif skok_var == True:
        skok.set(True)
        sin.set(False)
    
        

window = Tk()
window.title("Projekt MMM")
window.config(bg=BG_COLOR)
window.geometry("900x700")

main_title = Label(text="Projekt MMM - zadanie 6", font=("Coco Gothic", 30, 'bold'), fg=TEXT_COLOR, bg=BG_COLOR)
main_title.place(x=200, y=10)

sin = BooleanVar()
skok = BooleanVar()

main_photo_canvas = Canvas(width=850, height=344, bg="black", highlightthickness=0)
exc_img = PhotoImage(file="exc.png")
main_photo_canvas.create_image(425, 172, image=exc_img)
main_photo_canvas.place(x=25, y=120)

m1_entry = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
m1_entry.insert(0, "kg")
m1_entry.place(x=730, y=230)

m2_entry = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
m2_entry.insert(0, "kg")
m2_entry.place(x=730, y=335)

k1_entry = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
k1_entry.insert(0, "N/m")
k1_entry.place(x=675, y=203)

k2_entry= Entry(window, width=6, bg=INPUT_COLOR, fg="white")
k2_entry.insert(0, "N/m")
k2_entry.place(x=675, y=308)

b1_entry = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
b1_entry.insert(0,"kg/s")
b1_entry.place(x=765, y=176)

b2_entry = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
b2_entry.insert(0,"kg/s")
b2_entry.place(x=765, y=280)

skok_check = Checkbutton(window, variable = skok, onvalue= True, offvalue = False, bg="white", command = lambda sin = False, skok = True : check_buttons(sin, skok))
skok_check.place(x=190, y=380)

sin_check = Checkbutton(window, variable = sin, onvalue= True, offvalue = False, bg="white", command = lambda sin = True, skok = False : check_buttons(sin, skok))
sin_check.place(x=400, y =380)

amplituda_input = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
amplituda_input.place(x=765, y =400)
amplituda_text = Label(text="Amplituda", font=("Coco Gothic", 20, 'bold'), fg=TEXT_COLOR, bg=BG_COLOR)
amplituda_text.place()

window.mainloop()