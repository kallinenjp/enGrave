# contains list of random bits of code or notes that I have been or will reference.

##########
# image viewer with window layout of two columns
##########
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

avail_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
               '4', '5', '6', '7', '8', '9', '.', '-', '/', ' ',
               ]

##########
# convert alphanumeric char to E code
##########
# string_to_convert = ""
# e_list = []
# a_list = []
# for char in string_to_convert.casefold():
#     if char in avail_chars:
#         index = avail_chars.index(char)
#         character = char.upper()
#         e_list.append(index + 1)
#         a_list.append(character)
#
# print(e_list)
# print(a_list)

# 32668J-AB001
# E30, E29, E33, E33, E35, E10, E39, E01, E02, E27, E27, E28 CORRECT
# E30, E29, E33, E33, E35, E10, E39, E01, E02, E27, E27, E28 OUTPUT

# A BIG BEAR
# E01, E40, E02, E09, E07, E40, E02, E05, E01, E18 CORRECT
# E01, E40, E02, E09, E07, E40, E02, E05, E01, E18 OUTPUT

##########
# Spirals
##########
# Select type, OD to 0, OD ID, etc...

# select CW or CCW
# CW = G02 CCW = G03

# Give cutter diameter
# Max diameter - cutter diameter is tool path.
# Min diameter + cutter diameter is tool path

# Input Max diameter and Min diameter
# "Enter OD of feature: "200"
# "Enter ID of feature: "100"

# Do the math for cutter offset, as well as "collision" checks
# AKA (Max - Offset) - (Min + Offset) != <0

# Enter speed, feed, step over % or MM

# Construct Code

# Output

##########
# Engraving
##########
# Input string(s) of characters
# Done, need multi-line input support

# Convert string to list of characters (including newline?)
# 80%, need to implement newline

# Convert each character in the list to E value
# 50%? I have the E number values now, need to implement

# Pick from metals? maybe unnecessary
#

# Construct code
# base app maybe 60%

# Output
# the struggle is real

##########
# Facing
##########
# Select square or round
# Enter workpiece dims
# Enter cutter dia
# enter speeds feeds % step over
# Construct code
# Output

##########
#
##########
#"""
#Last part to run, outputs g-code text.
#passes h, e, f, d, r, z, and a variables in and actually constructs
#the G65 line. Also direct outputs the remainder of the code.
#I want to get this to A: Save a text file of the engraving in a directory.
#and B: Open that text file.
#Bonus points for naming properly, allowing user direction for directory,
#outputting to usb if available, AKA check for USB, then Y/N for save to USB
#"""
#
## from unnamed import x_var, y_var TODO: calculate string length and output
#
## from in_out import alpha_numeric
#
#def conversion_van():
#    """"""
#    to_convert = entry_string.get()
#    e_list = []
#    a_list = []
#    for char in to_convert.casefold():
#        if char in alpha_numeric:
#            index = alpha_numeric.index(char)
#            character = char.upper()
#            e_list.append(index + 1)
#            a_list.append(character)
#    for index in enumerate(e_list):
#        return index
#    for index in enumerate(a_list):
#        return index
#
#
#h_var = ""
#e_var = ""
#f_var = ""
#d_var = ""
#r_var = ""
#z_var = ""
#a_var = ""
#
#out_string = f"G65 P8200 H{h_var} E{e_var} F{f_var} D{d_var} " \
#             f"R{r_var} Z{z_var} ({a_var})"
#
#
#def gcode_text(text: str = " ", width: int = 80) -> None:
#    """ Print a string of g-code, with variables for engraving.
#
#    :param str text: The string of user input to print.
#    :param int width: The overall width to print within
#
#    :raises ValueError: if the supplied string is too long to fit.
#    """
#    screen_width = width
#    if len(text) > screen_width - 4:
#        raise ValueError("String {0} is larger than specified width {1}"
#                         .format(text, screen_width))
#
#    if text == "*":
#        print("*" * screen_width)
#    else:
#        centered = text.center(screen_width - 4)
#        output_string = "**{0}**".format(centered)
#        print(output_string)
#
#
#gcode_text("%")
#gcode_text("O4321")
#gcode_text("G99 G90 G80 G49 G40 G00")
#gcode_text("")
#gcode_text("(T02 ENGRAVE)")
#gcode_text("T25 M06")
#gcode_text("G0 G55 X0. Y0.")
#gcode_text("G43 Z10. H25.")
#gcode_text("S3000 M03")
#gcode_text("(ENGRAVE)")
#for something in num_char_user_in:  # TODO: len(user_in) = iterations
#    gcode_text("G65 P8200 {0} {1} {2} {3} {4} {5} {6}"
#               .format(h_var, e_var, f_var, d_var, r_var, z_var, a_var)
#               )
#gcode_text("(H-HEIGHT)")
#gcode_text("(E-LETTER CODE TO ENGRAVE)")
#gcode_text("(F-PLUNGE FEED)")
#gcode_text("(D-CUT FEED)")
#gcode_text("(R-RAPID PLANE)")
#gcode_text("(Z-DEPTH)")
#gcode_text("Z25.")
#gcode_text("G0 G53 Z0 M09")
#gcode_text("M53")
#gcode_text("G91 G28 X0 Y0")
#gcode_text("G90 M5")
#gcode_text("M19")
#gcode_text("M30")
#gcode_text("%")

##########
#
##########

##########
#
##########

##########
#
##########

##########
#
##########

##########
#
##########
