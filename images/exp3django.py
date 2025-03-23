import tkinter as tk
from tkinter import messagebox
def loginform():
    if(usernameentry.get()=="user001"):
        text = "Welcome,"+usernameentry.get()
        messagebox.showinfo("Login Successful",text)
    else:
        text = "Invalid Username or Password"
        messagebox.showwarning("Login Failed",text)
root = tk.Tk()
root.title("Login Form")
root.geometry("300x300")
userlabel = tk.Label(root,text = "User Name:")
userlabel.grid(row=19,column=20,padx=100)
usernameentry = tk.Entry(root,width = 20)
usernameentry.grid(row=20,column=20,padx=100)
pwdlabel = tk.Label(root,text = "Password")
pwdlabel.grid(row=21,column=20,padx=100)
pwdentry = tk.Entry(root,width = 20,show="*")
pwdentry.grid(row=22,column=20,padx=100)
okbutton = tk.Button(root,text = "OK",command=loginform)
okbutton.grid(row=23,column=20,padx=100)
root.mainloop()
