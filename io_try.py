# import character data from nested_data.py
from nested_data import chars

# Currently working: Single character translation from menu selection.

# Constants are not protected and are only a human-readable all-caps variable
VALUES_INDEX = 2
CHARACTER_INDEX = 1
E_VALUE = 2

# print selection list
while True:
    print("Please choose your character type:")
    for index, (characters, user_in, values) in enumerate(chars):
        print("{}: {}".format(index + 1, characters))
    print("0: Exit Program")

# Take user input, if invalid or "0" the code breaks and exits
    choice = int(input())
    if 1 <= choice <= len(chars):
        values_list = chars[choice - 1][VALUES_INDEX]
    else:
        break

# Print the character list
    print("Please choose your character:")
    for index, (user_in, char, values) in enumerate(values_list):
        print("{}: {}".format(index + 1, char.upper()))
    print("Invalid: return to album select")

# get user input, invalid input returns to album menu
    char_choice = int(input())
    if 1 <= char_choice <= len(values_list):
        title = values_list[char_choice - 1][CHARACTER_INDEX]
        e_value = values_list[char_choice - 1][E_VALUE]
    else:
        continue

    print("G65 P8200 H? {0} D0. R3. F0. Z-3. ({1})".format(e_value, title.upper()))
    print("*" * 80)
