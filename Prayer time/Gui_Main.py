from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('600x600')
window.title("Muslim pro")
window.config(bg='seagreen')


class Widgets:
    label1 = Label(window, text="An app to tell you the prayer time in your chosen region",bg='seagreen', font=("Times new roman", 12,))
    label1.pack()

    first_frame = Canvas(window,width=400, height=400,)
    first_frame.pack()

    def __int__(self,main):

        self.drop_down = ttk.Combobox(Widgets.first_frame, values=['main','with'], font=("Arial", 20), width=7)
        self.drop_down.pack()


Widgets()

window.mainloop()
