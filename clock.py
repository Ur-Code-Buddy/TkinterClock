from time import strftime
from tkinter import Label, Tk


window = Tk()
window.title("")
window.geometry("230x80")
window.configure(bg = "blue")
window.resizable(False, False)


clock_label = Label(window, bg="blue", fg="black", font = ("Serif", 30, 'bold'), relief='flat')
clock_label.place(x = 20, y = 20)

def updating_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, updating_label)

updating_label()
window.mainloop()