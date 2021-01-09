from tkinter import *

print("hello")
root = Tk()
root.title("Github 4 life")
Label(root, text = "Test boi").grid(row = 0, column = 0)
e = Entry(root, width = 100, borderwidth = 5)
e.grid(row = 1, column = 0, columnwidth = 2)
Label(root, text = "water").grid(row = 0, column = 1)
root.mainloop()
