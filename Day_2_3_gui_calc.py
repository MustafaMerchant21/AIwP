import tkinter as tk

def click(event):
    button_text = event.widget["text"]
    current = str(entry.get())
    
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Python Calculator")

entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.SUNKEN, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font=("Arial", 16), width=5, height=2)
        btn.grid(row=i+1, column=j)
        btn.bind("", click)

root.mainloop()
