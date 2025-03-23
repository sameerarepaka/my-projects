import tkinter as tk
root = tk.Tk()
root.title("My First Ever TKinter Window")
root.geometry("500x500")
label = tk.Label(root,text = "Welcome to the TKinter Package")
label.pack()
root.mainloop()