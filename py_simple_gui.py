import PySimpleGUI as psg
import string
# from output_g_code import conversion_van

psg.theme("default1")

layout = [
    [
        psg.Text("Enter Text: ", size=(10, 1)),
        psg.InputText(do_not_clear=False)
    ],
    [
        psg.Text("Select Options: "),
        psg.Radio("H = 2", "group1"),
        psg.Radio("H = 3", "group1"),
        psg.Radio("H = 4", "group1"),
        psg.Radio("H = 5", "group1"),
        psg.Radio("H = 6", "group1"),
    ],
    [
        psg.Button("Convert"),
        psg.Button("Exit")
    ]
]

window = psg.Window("Form", layout)

a_var = []
e_var = []
h_var = ""
low_string = list(string.ascii_lowercase)

while True:
    event, values = window.read()
    if event == "Exit" or event == psg.WIN_CLOSED:
        break

    elif event == "Convert":
        in_string = values[0]
        for index in in_string:
            a_var.append(index)
        for i in in_string:
            e_var.append(low_string.index(i) + 1)

        var_list = [values[1], values[2], values[3],
                    values[4], values[5],
                    ]
        for index in var_list:
            # print(index) debugging
            if index is True:
                h_var = str(var_list.index(index) + 2)

        # output finished code
        for index in values[0]:
            print("G65 P8200 H{0}. E{1} F100. D100. R3. Z-2.5 ({2})"
                  .format(h_var, e_var, a_var))

        # debugging
        print(a_var)
        print(e_var)
        print("H" + h_var + ".")
        print(values)

window.close()
