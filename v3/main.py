# v3_gui/calculator_gui.py

import tkinter as tk

def click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    btn = tk.Button(frame, text=button, font="Arial 15", width=5, height=2)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

clear_btn = tk.Button(root, text="C", font="Arial 15", height=2)
clear_btn.pack(fill=tk.BOTH)
clear_btn.bind("<Button-1>", click)

root.mainloop()
