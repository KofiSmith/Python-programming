# importing whole module
from tkinter import *
from tkinter.ttk import *
# importing strftime function to
#retrieve system time
from time import strftime
# creating tkinter window
root = Tk()
root.title('Clock')
#this function is used to display time on the label
def time():
  string = strftime('%H:%M:%S %p')
  lbl.config(text = time)
  lbl.after(1000, time)

#styling the label widget so that clock will look more attractive
lbl = Label(root, font=('calibri',40,'bold'),
            background='black',
            foreground= 'white')
#placing clock at the center of tkinter window
lbl.pack(anchor = 'center')
time()
mainloop()




