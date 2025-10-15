"""
Main window code, includes input and output stored as variables
Also includes a button with a command to run the conversion program.

TODO: pass conversion program as a function into the update_output()
TODO: pass variables out to the conversion function.
"""
import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.geometry("430x480")
window.title('enGrave')

# Functions
def update_output():
    # Temporarily set state normal to allow editing
    output_text.config(state='normal')

    # Delete current content from the Text widget
    output_text.delete("1.0", tk.END)

    # update StringVar
    input_entry_string.set(entry_string.get())

    # brute force output, testing
    string_to_convert = input_entry_string.get()
    e_list = []
    a_list = []
    for char in string_to_convert.casefold():
        if char in avail_chars:
            index = avail_chars.index(char)
            character = char.upper()
            e_list.append('E' + str(index + 1).zfill(2))
            a_list.append(character)

    for i, item in enumerate(e_list):
        e_val = e_list[i]
        a_val = a_list[i]
        output_text.insert(
            tk.END,
            "G65 P8200 H{0}. {1} F{2}. D{3}. R{4}. Z{5}. ({6})\n"
            .format(
                h_var_input.get(),
                e_val,
                f_var_input.get(),
                d_var_input.get(),
                r_var_input.get(),
                z_var_input.get(),
                a_val
            )
        )

    # Set state back to DISABLED to make it read-only
    output_text.config(state='disabled')

# Variables
# Passthroughs
h_var_input = tk.IntVar(value = 3)
f_var_input = tk.IntVar(value = 1270)
d_var_input = tk.IntVar(value = 350)
r_var_input = tk.IntVar(value = 3)
z_var_input = tk.IntVar(value = -3)
# Changeable's
input_entry_string = tk.StringVar()
output_string = tk.StringVar()
# Constants
avail_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
               '4', '5', '6', '7', '8', '9', '.', '-', '/', ' ',
               ]

# Labels
top_label = tk.Label(window, text="Enter Variables as desired, integers only.")
top_label.grid(column = 0, row = 0, columnspan = 10)
label_h = ttk.Label(window, text="H - Height")
label_h.grid(column=0, row=1)
label_f = ttk.Label(window, text="F - Plunge Feed")
label_f.grid(column=1, row=1)
label_d = ttk.Label(window, text="D - Cut Feed")
label_d.grid(column=0, row=3)
label_r = ttk.Label(window, text="R - Retract")
label_r.grid(column=1, row=3)
label_z = ttk.Label(window, text="Z - Depth")
label_z.grid(column=0, row=5)

# Input
entry_h = ttk.Entry(window, textvariable=h_var_input, width=10, justify='center')
entry_h.grid(column=0, row=2)
entry_f = ttk.Entry(window, textvariable=f_var_input, width=10, justify='center')
entry_f.grid(column=1, row=2)
entry_d = ttk.Entry(window, textvariable=d_var_input, width=10, justify='center')
entry_d.grid(column=0, row=4)
entry_r = ttk.Entry(window, textvariable=r_var_input, width=10, justify='center')
entry_r.grid(column=1, row=4)
entry_z = ttk.Entry(window, textvariable=z_var_input, width=10, justify='center')
entry_z.grid(column=0, row=6)
entry_string = tk.Entry(window, width=67, textvariable=input_entry_string)
entry_string.grid(column=0, columnspan=5, row=7, pady=10, padx=10)

# Output
convert_button = ttk.Button(
    window,
    text="Convert",
    command=update_output)
convert_button.grid(column=1, row=8)
output_text = tk.Text(window, height=15, width=50)
output_text.grid(column=0, row=9, columnspan=10, padx=10, pady=10)

# Initialize run
window.mainloop()
