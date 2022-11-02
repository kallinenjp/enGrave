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

# image viewer with window layout of two columns
# import os.path
# file_list_column = [
#     [
#         psg.Text("Image Folder"),
#         psg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
#         psg.FolderBrowse(),
#     ],
#     [
#         psg.Listbox(
#             values=[], enable_events=True, size=(40, 20),
#             key="-FILE LIST-"
#         )
#     ]
#     ]
#
# # for now will only show the name of the chosen file
# image_viewer_column = [
#     [psg.Text("Choose an image:")],
#     [psg.Text(size=(40, 1), key="-TOUT-")],
#     [psg.Image(key="-IMAGE-")],
# ]
#
# # Full Layout
# layout = [
#     [
#         psg.Column(file_list_column),
#         psg.VSeperator(),
#         psg.Column(image_viewer_column),
#     ]
# ]
#
# window = psg.Window("Image Viewer", layout)
#
# while True:
#     event, values = window.read()
#     if event == "Exit" or event == psg.WIN_CLOSED:
#         break
#     # folder name was filled in, so get list of files
#     if event == "-FOLDER-":
#         folder = values["-FOLDER-"]
#         try:
#             # get list of files
#             file_list = os.listdir(folder)
#         except:
#             file_list = []
#
#         fnames = [
#             f
#             for f in file_list
#             if os.path.isfile(os.path.join(folder, f))
#             and f.lower().endswith((".png", ".gif"))
#         ]
#         window["-FILE LIST-"].update(fnames)
#     elif event == "-FILE LIST-":  # a file was chosen from the list
#         try:
#             filename = os.path.join(
#                 values["-FOLDER-"], values["-FILE LIST-"][0]
#             )
#             window["-TOUT-"].update(filename)
#             window["-IMAGE-"].update(filename=filename)
#         except:
#             pass
#
# window.close()
