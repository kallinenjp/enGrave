import tkinter as tk

def insert_text():
    text_widget.insert(tk.END, "This is a new line.\n")

root = tk.Tk()

text_widget = tk.Text(root, height=5, width=30)
text_widget.pack()

# The first insertion will be at the very start
text_widget.insert(tk.END, "Initial text.\n")

# This button adds new text at the end on a new line
button = tk.Button(root, text="Add Line", command=insert_text)
button.pack()

root.mainloop()
