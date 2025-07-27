import tkinter as tk
from tkinter import filedialog as fd
import os, os.path
import sys

def load_config():
    if not os.path.isfile(f"{sys.path[0]}/config.cfg"):
        f = open(f"{sys.path[0]}/config.cfg", "w")
        f.write(";;")

    f = open(f"{sys.path[0]}/config.cfg")
    vals = f.read().split(';')

    en1.insert(0,vals[0])
    en2.insert(0,vals[1])
    en3.insert(0,vals[2])

    update_lists()


def save_config():
    f = open(f"{sys.path[0]}/config.cfg", "w")
    f.write(f"{en1.get()};{en2.get()};{en3.get()}")


def update_lists():
    iwadListBox.delete(0,tk.END)
    modsListBox.delete(0,tk.END)

    for f in os.scandir(en2.get()):
        if f.is_file():
            iwadListBox.insert(tk.END, f.name)
    
    for f in os.scandir(en3.get()):
        if f.is_file():
            modsListBox.insert(tk.END, f.name)


def bt1_click():
    filename = fd.askopenfilename(filetypes=(
        ('Executable files', '*.exe'),
        ('All files', '*.*')
    ))
    en1.insert(0, filename)
    save_config()


def bt2_click():
    folder = fd.askdirectory()
    en2.delete(0,tk.END)
    en2.insert(0, folder)
    update_lists()
    save_config()


def bt3_click():
    folder = fd.askdirectory()
    en3.delete(0,tk.END)
    en3.insert(0, folder)
    update_lists()
    save_config()


def play_click():
    engine = en1.get()
    iwad = f"-iwad {en2.get()}/{iwadListBox.get(iwadListBox.curselection())}"
    mods = ""

    for m in modsListBox.curselection():
        mods += f"-file {en3.get()}/{modsListBox.get(m)} "

    os.system(f"{engine} {iwad} {mods}")


#Window
root = tk.Tk()
root.geometry("580x800")
root.resizable(False, False)
root.title("DOOM launcher")

#Title
lbTitle = tk.Label(root, text="DOOM LAUNCHER", font=("Algerian", 50))
lbTitle.pack(padx=20, pady=20)

#Entrys
entryFrame = tk.Frame(root)
entryFrame.pack(fill="x")

lb1 = tk.Label(entryFrame, text="Source port path:", font=("Arial", 10), fg="dimgray")
lb1.grid(row=0, column=0, sticky=tk.W, padx=10)
en1 = tk.Entry(entryFrame, font=("Arial", 14), width=45)
en1.grid(row=1, column=0, sticky=tk.W, padx=10)
bt1 = tk.Button(entryFrame, text="📁", font=("Arial", 14), command=bt1_click)
bt1.grid(row=1, column=1, sticky=tk.E, padx=10)

lb2 = tk.Label(entryFrame, text="IWADs path:", font=("Arial", 10), fg="dimgray")
lb2.grid(row=2, column=0, sticky=tk.W, padx=10)
en2 = tk.Entry(entryFrame, font=("Arial", 14), width=45)
en2.grid(row=3, column=0, sticky=tk.W, padx=10)
bt2 = tk.Button(entryFrame, text="📁", font=("Arial", 14), command=bt2_click)
bt2.grid(row=3, column=1, sticky=tk.E, padx=10)

lb3 = tk.Label(entryFrame, text="Mods path:", font=("Arial", 10), fg="dimgray")
lb3.grid(row=4, column=0, sticky=tk.W, padx=10)
en3 = tk.Entry(entryFrame, font=("Arial", 14), width=45)
en3.grid(row=5, column=0, sticky=tk.W, padx=10)
bt3 = tk.Button(entryFrame, text="📁", font=("Arial", 14), command=bt3_click)
bt3.grid(row=5, column=1, sticky=tk.E, padx=10)

#ListBoxes
listBoxFrame = tk.Frame(root, pady=20)
listBoxFrame.pack(fill="x")

iwadListBox = tk.Listbox(listBoxFrame, font=("Arial", 10), activestyle="dotbox", selectmode="single", height=22, width=38, exportselection=False)
iwadListBox.grid(row=0, column=0, sticky=tk.W, padx=10)
modsListBox = tk.Listbox(listBoxFrame, font=("Arial", 10), activestyle="dotbox", selectmode="multiple", height=22, width=38, exportselection=False)
modsListBox.grid(row=0, column=1, sticky=tk.E, padx=10)

#PlayButton
btPlay = tk.Button(root, text="PLAY", font=("Algerian", 30), padx=20, command=play_click)
btPlay.pack(fill="x")

#Load saved entry values
load_config()

#MainLoop
root.mainloop()