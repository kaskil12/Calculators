import tkinter as tk

def legg_sammen():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        resultat.set(num1 + num2)
    except ValueError:
        resultat.set("Ugyldige tall")

def trekke_fra():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        resultat.set(num1 - num2)
    except ValueError:
        resultat.set("Ugyldige tall")

def multipliser():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        resultat.set(num1 * num2)
    except ValueError:
        resultat.set("Ugyldige tall")

def divider():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        if num2 != 0:
            resultat.set(num1 / num2)
        else:
            resultat.set("Kan ikke dele på null")
    except ValueError:
        resultat.set("Ugyldige tall")

root = tk.Tk()
root.title("Enkel Kalkulator")

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Legg sammen", command=legg_sammen)
button_add.grid(row=1, column=0, padx=10, pady=10)

button_subtract = tk.Button(root, text="Trekk fra", command=trekke_fra)
button_subtract.grid(row=1, column=1, padx=10, pady=10)

button_multiply = tk.Button(root, text="Multipliser", command=multipliser)
button_multiply.grid(row=2, column=0, padx=10, pady=10)

button_divide = tk.Button(root, text="Divider", command=divider)
button_divide.grid(row=2, column=1, padx=10, pady=10)

resultat = tk.StringVar()
result_label = tk.Label(root, textvariable=resultat)
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
