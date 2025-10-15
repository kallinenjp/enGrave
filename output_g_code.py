"""
Last part to run, outputs g-code text.
passes h, e, f, d, r, z, and a variables in and actually constructs
the G65 line. Also direct outputs the remainder of the code.
I want to get this to A: Save a text file of the engraving in a directory.
and B: Open that text file.
Bonus points for naming properly, allowing user direction for directory,
outputting to usb if available, AKA check for USB, then Y/N for save to USB
"""

# from unnamed import x_var, y_var TODO: calculate string length and output

# from in_out import alpha_numeric

def conversion_van():
    """"""
    to_convert = entry_string.get()
    e_list = []
    a_list = []
    for char in to_convert.casefold():
        if char in alpha_numeric:
            index = alpha_numeric.index(char)
            character = char.upper()
            e_list.append(index + 1)
            a_list.append(character)
    for index in enumerate(e_list):
        return index
    for index in enumerate(a_list):
        return index


h_var = ""
e_var = ""
f_var = ""
d_var = ""
r_var = ""
z_var = ""
a_var = ""

out_string = f"G65 P8200 H{h_var} E{e_var} F{f_var} D{d_var} " \
             f"R{r_var} Z{z_var} ({a_var})"


def gcode_text(text: str = " ", width: int = 80) -> None:
    """ Print a string of g-code, with variables for engraving.

    :param str text: The string of user input to print.
    :param int width: The overall width to print within

    :raises ValueError: if the supplied string is too long to fit.
    """
    screen_width = width
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered)
        print(output_string)


gcode_text("%")
gcode_text("O4321")
gcode_text("G99 G90 G80 G49 G40 G00")
gcode_text("")
gcode_text("(T02 ENGRAVE)")
gcode_text("T25 M06")
gcode_text("G0 G55 X0. Y0.")
gcode_text("G43 Z10. H25.")
gcode_text("S3000 M03")
gcode_text("(ENGRAVE)")
for something in num_char_user_in:  # TODO: len(user_in) = iterations
    gcode_text("G65 P8200 {0} {1} {2} {3} {4} {5} {6}"
               .format(h_var, e_var, f_var, d_var, r_var, z_var, a_var)
               )
gcode_text("(H-HEIGHT)")
gcode_text("(E-LETTER CODE TO ENGRAVE)")
gcode_text("(F-PLUNGE FEED)")
gcode_text("(D-CUT FEED)")
gcode_text("(R-RAPID PLANE)")
gcode_text("(Z-DEPTH)")
gcode_text("Z25.")
gcode_text("G0 G53 Z0 M09")
gcode_text("M53")
gcode_text("G91 G28 X0 Y0")
gcode_text("G90 M5")
gcode_text("M19")
gcode_text("M30")
gcode_text("%")
