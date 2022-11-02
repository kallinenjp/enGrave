# import character data from nested_data.py can I work this in? nested data should
# contain everything I need
from nested_data import chars

# Current status:
# can take string, iterate over it and output correct e number and letter

# TODO: print engraving code each char, function?
# TODO: take user input, Function?
# TODO: Document the code
# TODO: split code into modules and subs etc. like a real program

# TODO: make ui/ux
# TODO: output use/help text to the user
# TODO: add variables for letter size, add logo codes somehow?
# TODO: yes.

# have location or method to get user input as string
# smash the string and remove any junk if needed.
# convert string to list

alpha_numeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
                 '4', '5', '6', '7', '8', '9', '', '/', '-', ' ', '.',
                 ]

# string_to_convert = ""
# e_list = []
# a_list = []
# for char in string_to_convert.casefold():
#     if char in alpha_numeric:
#         index = alpha_numeric.index(char)
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
