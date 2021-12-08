import tkinter as tk
from tkinter import messagebox, END, ANCHOR
from tkinter.filedialog import askopenfilename, asksaveasfilename

#define functions
def addtask():
    task = textbox.get()
    if task == "":
        tk.messagebox.showwarning("ERROR!", "Please enter a valid task")
    else:
        listfiles = listbox.get(0, END)
        if task not in listfiles:
            listbox.insert(END, task)
            textbox.delete(0,END)
        else:
            tk.messagebox.showwarning("ERROR!", "Duplicate Value")
    

def deltask():
    listbox.delete(ANCHOR)

def savefile():
    file_path = asksaveasfilename(defaultextension = "txt", filetypes = [("text files", "*.txt"), ("all files", "*.*")])
    if not file_path:
        return
    with open(file_path, "w") as write_file:
        text = listbox.get(0,END)
        for i in text:
            write_file.write(i + "\n")
    
def cleartask():
    listbox.delete(0,END)

def opentask():
    pass


#main window
window = tk.Tk()
window.geometry('500x500')
window.resizable(0,0)
window.title("Checklist")

#define fonts and colours
text_color = "#fffacd"
menu_color = "#dbd9db"
window_color = "#6c809a"
btn_color = "#e2cff4"
window.configure(bg = window_color)

#frames
input_frame = tk.Frame(window, bg = window_color)
input_frame.pack()
list_frame = tk.Frame(window, bg = window_color)
list_frame.pack()
btn_frame = tk.Frame(window, bg = window_color)
btn_frame.pack()

#textbox
textbox = tk.Entry(input_frame, font = ('Verdana', 16), borderwidth = 3)
textbox.grid(row = 0, column = 0, pady = 5, padx = 5)
add_btn = tk.Button(input_frame, text = "Add", font = ("Times New Roman", 14), bg = btn_color, command = addtask, borderwidth = 2)
add_btn.grid(row = 0, column = 1, pady = 5, padx = 5)

#buttons
del_btn = tk.Button(btn_frame, text = "Delete Items", font = ("Times New Roman", 14), bg = btn_color, command = deltask).grid(row = 0, column=0, pady = 5, padx = 5)
save_btn = tk.Button(btn_frame, text = "Save", font = ("Times New Roman", 14), bg = btn_color, command = savefile).grid(row = 0, column=1, pady = 5, padx = 5, ipadx = 10)
clear_btn = tk.Button(btn_frame, text = "Clear", font = ("Times New Roman", 14), bg = btn_color, command = cleartask).grid(row = 0, column=2, pady = 5, padx = 5, ipadx = 10)
open_btn = tk.Button(btn_frame, text = "Open", font = ("Times New Roman", 14), bg = btn_color, command = opentask).grid(row = 0, column=3, pady = 5, padx = 5, ipadx = 10)

#listbox
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side = "right",fill="y")
listbox = tk.Listbox(list_frame, width = 55, height = 15, bg = menu_color, yscrollcommand = scrollbar.set)
listbox.pack()
scrollbar.config(command = listbox.yview)
    
window.mainloop()
