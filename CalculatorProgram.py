#Imports the tkinter module
import tkinter as tk

#Makes the Window
root = tk.Tk()
root.title("Calculator App")

#adds a label to the window
label = tk.Label(root, text="Welcome to the Calculator App!")
label.grid(row=0,column=0, columnspan=4)

#adds all the buttons to the window
button1 = tk.Button(root, text = "1")
button1.grid(row=1, column=0)

button2 = tk.Button(root, text = "2")
button2.grid(row=1, column=1)

button3 = tk.Button(root, text = "3")
button3.grid(row=1, column=2)



#Keeps the window open
root.mainloop()