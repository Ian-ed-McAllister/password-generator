from pydoc import text
import tkinter as tk
from tkinter import *
import random
from xmlrpc.client import boolean




root = tk.Tk()
"""
function to make the password it will use by default lowercase letters and numbers, Then based on input it will add Uppercase letters and or Special characters based on user input.
If no number was given(either left blank not a digit) it will default to a length of 10
"""

def makePassword():
    chars="abcdefghijklmnopqrstuvwxyz1234567890"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special="!@#$%^&*?()'"
    if(cp.get()):
        chars = chars + upper
    if(sp.get()):
        chars = chars + special


    if sizeEntry.get().isdigit():
        password = ""
        for i in range(0,  int( sizeEntry.get())):
            password = password + random.choice(chars)
        output_entry.delete(0,len(output_entry.get()))   
        output_entry.insert(0,password)       
    else:
        if(cp.get()):
            chars = chars + upper
        if(sp.get()):
            chars = chars + special
        password = ""
        for i in range(0,  10):
            password = password + random.choice(chars)
        output_entry.delete(0,len(output_entry.get()))   
        output_entry.insert(0,password)       
    

    


size_label = tk.Label(root, text = "Please enter the size of the desired password")
size_label.grid(row=0,column=0)

sizeEntry = tk.Entry(root)
sizeEntry.grid(row = 0,column = 1)




output_label = tk.Label(root, text = "Output")
output_label.grid(row=1,column=0)
output_entry = tk.Entry(root)
output_entry.grid(row = 1,column = 1)


cp = BooleanVar()
upper_label = tk.Label(root,text = "Use Capital Letters: ")
upper_label.grid(row = 2,column = 0)
upper_include = tk.Checkbutton(root,variable=cp,onvalue=True,offvalue=False)
upper_include.grid(row = 2,column = 1)



sp = BooleanVar()
special_label = tk.Label(root,text = "Use Special Characters(%^#@ etc.): ")
special_label.grid(row = 3,column = 0)
special_include = tk.Checkbutton(root,variable=sp,onvalue=True,offvalue=False)
special_include.grid(row = 3,column = 1)



make_password = tk.Button(root, text = "make Password",padx=10,pady=5,fg="white",bg="#263D42",command=makePassword)
make_password.grid(row = 4,column = 0)

root.mainloop()