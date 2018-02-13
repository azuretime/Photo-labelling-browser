# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 00:33:27 2018

@author: Jiang Jinjing
"""

import Tkinter as tk
import tkFileDialog
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title('Photo Labelling App')
root.geometry('1000x800')

path = tk.StringVar()
image=photo=[]
def openPhoto():
    path_ = tkFileDialog.askdirectory()
    path.set(path_)
    col = 1
    row = 1
    
    for file in os.listdir(path.get()):
        global image,photo
        if file.endswith(".jpg"):
            image.insert(0,Image.open(path.get()+"/"+file).resize((300, 200), Image.ANTIALIAS))
            photo.insert(0,ImageTk.PhotoImage(image[0]))
            if col == 1:
                C1=tk.Checkbutton(framein2, text=file, image = photo[0], \
                    compound='top', onvalue = 1, offvalue = 0)
                C1.grid(row = row, column = 0, sticky=tk.W)
                col+=1
            elif col == 2:
                C2=tk.Checkbutton(framein2, text=file, image = photo[0], \
                    compound='top', onvalue = 1, offvalue = 0)
                C2.grid(row = row, column = 1, sticky=tk.W)
                col+=1
            else:
                C2=tk.Checkbutton(framein2, text=file, image = photo[0], \
                    compound='top', onvalue = 1, offvalue = 0)
                C2.grid(row = row, column = 2, sticky=tk.W)
                col-=2
                row+=1
                
def myCanvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1000,height=700)
    
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame1.grid(row=0, sticky="ew")
frame2.grid(row=1, sticky="nsew")


canvas=tk.Canvas(frame2)
framein2=tk.Frame(canvas)
myscrollbar=tk.Scrollbar(frame2,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=framein2,anchor='nw')
framein2.bind("<Configure>",myCanvas)

lpath = tk.Label(frame1,text = "  Path  :   ").grid(row = 0, column = 0)
entry = tk.Entry(frame1, textvariable = path, width=50).grid(row = 0, column = 1)
b = tk.Button(frame1, text = "Select", command = openPhoto).grid(row = 0, column = 2)

root.mainloop()