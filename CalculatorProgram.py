#Imports the tkinter module
import tkinter as tk

#Makes the Window
root = tk.Tk()
root.title("Calculator App")

#adds a label to the window
label = tk.Label(root, text="Welcome to the Calculator App!")
label.grid(row=0,column=0, columnspan=4)

#adds a text box to the window for user input and output

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=1, column=0, columnspan=4)

#allows the buttons to add to the entry box when clicked
def add_text(input):
    entry.insert(tk.END, input)

#adds all the buttons to the window

#Calculator Row 2 Buttons
button1 = tk.Button(root, text = "1", command=lambda: add_text("1"))
button1.grid(row=2, column=0)

button2 = tk.Button(root, text = "2", command=lambda: add_text("2"))
button2.grid(row=2, column=1)

button3 = tk.Button(root, text = "3", command=lambda: add_text("3"))
button3.grid(row=2, column=2)

buttonDivide = tk.Button(root, text = "/", command=lambda: add_text("/"))
buttonDivide.grid(row=2, column=4)

#Calculator Row 3 Buttons
button4 = tk.Button(root, text = "4", command=lambda: add_text("4"))
button4.grid(row=3, column=0)

button5 = tk.Button(root, text = "5", command=lambda: add_text("5"))
button5.grid(row=3, column=1)

button6 = tk.Button(root, text = "6", command=lambda: add_text("6"))
button6.grid(row=3, column=2)

buttonMultiply = tk.Button(root, text = "*", command=lambda: add_text("*"))
buttonMultiply.grid(row=3, column=4)

#Calculator Row 4 Buttons
button7 = tk.Button(root, text = "7", command=lambda: add_text("7"))
button7.grid(row=4, column=0)

button8 = tk.Button(root, text = "8", command=lambda: add_text("8"))
button8.grid(row=4, column=1)

button9 = tk.Button(root, text = "9", command=lambda: add_text("9"))
button9.grid(row=4, column=2)

buttonSubtract = tk.Button(root, text = "-", command=lambda: add_text("-"))
buttonSubtract.grid(row=4, column=4)

#Calculator Row 5 Buttons
button0 = tk.Button(root, text = "0", command=lambda: add_text("0"))
button0.grid(row=5, column=1)

buttonEquals = tk.Button(root, text = "=", command=lambda: add_text("="))
buttonEquals.grid(row=5, column=2)

buttonAdd = tk.Button(root, text = "+", command=lambda: add_text("+"))
buttonAdd.grid(row=5, column=4)

#Keeps the window open
root.mainloop()