import os
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import time

BG_COLOR = "#f7e8bc"
TEXT_COLOR = "#141414"
INPUT_COLOR = "#143d59"

x1_values=[]
x2_values=[]
t_values=[]

def check_buttons(sin_var, skok_var):
    
    global sin
    global skok
    
    if sin_var == True:
        sin.set(True)
        skok.set(False)
    elif skok_var == True:
        skok.set(True)
        sin.set(False)
        
    if skok.get() == True:
        okres_input.delete(0, END)
        okres_input.place_forget()
        okres_text.place_forget()
    elif sin.get() == True:
        okres_input.place(x=700, y =425)
        okres_text.place(x= 650, y=425)
        okres_input.delete(0, END)
        okres_input.insert(0,"s")
    
def file_handeling(czy_sinus, dane):
    
    with open("dane.txt", "wt") as file:
        if czy_sinus:
            file.writelines("1\n")
        else:
            file.writelines("0\n")
            
            
        for key, value in dane.items():
            file.writelines(f"{value}\n")
            
    os.startfile("projekt_mmm.exe")
    
    time.sleep(2)
    read_exit_file()
    
def button_click():
    global sin
    
    aktualna_zmienna = ""
    is_working = True
    is_sin = False 
    
    dane = {
        "amp": amplituda_input.get(),
        "m1":m1_entry.get(),
        "m2":m2_entry.get(),
        "k1":k1_entry.get(),
        "k2":k2_entry.get(),
        "b1":b1_entry.get(),
        "b2":b2_entry.get(),
        
    }
    if(sin.get() == True):
        is_sin = True
        dane["okres"] = okres_input.get()
        
    try:
        for key, value in dane.items():
            aktualna_zmienna = key
            dane[key] = float(value)
    except:
        is_working = False
        messagebox.showerror(title=None, message=f"Błędna wartość: {aktualna_zmienna}" )
        
    if is_working == True:
        file_handeling(is_sin, dane)
    
def read_exit_file():
    t_values.clear()
    x1_values.clear() 
    x2_values.clear()
    with open("wyjscie.txt", "r") as file:
        list = file.readlines()
        

    for line in list:
        if line != "":
            draft_list = line.split(";")
            t_values.append(float(draft_list[0]))
            x1_values.append(float(draft_list[1]))
            x2_values.append(float(draft_list[2]))
        #print(line)
        
    create_graph()

def create_graph():

    plt.clf()
    #plt.close()
    plt.plot(t_values, x1_values, label = "X1")
    plt.plot(t_values, x2_values, label = "X2")
    plt.legend() 
    plt.show()
    
    



window = Tk()
window.title("Projekt MMM")
window.config(bg=BG_COLOR)
window.geometry("900x700")

main_title = Label(text="Projekt MMM - zadanie 6", font=("Coco Gothic", 30, 'bold'), fg=TEXT_COLOR, bg=BG_COLOR)
main_title.place(x=200, y=40)

sin = BooleanVar(value= True)
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
amplituda_input.place(x=730, y =401)
amplituda_text = Label(text="Amplituda:", font=("Coco Gothic", 10, 'bold'), fg=TEXT_COLOR, bg="white")
amplituda_text.place(x= 650, y=400)

okres_input = Entry(window, width=6, bg=INPUT_COLOR, fg="white")
okres_input.place(x=700, y =425)
okres_input.insert(0,"s")
okres_text = Label(text="Okres:", font=("Coco Gothic", 10, 'bold'), fg=TEXT_COLOR, bg="white")
okres_text.place(x= 650, y=425)

calculate_button = Button(window, text="Wykonaj wykres", height=2, width=20, bg=INPUT_COLOR, font=("Coco Gothic", 10, 'bold'), fg="white", 	
activebackground = "#0e2c40", command= button_click, activeforeground="white")
calculate_button.place(x=380, y=415)



window.mainloop()