# Fanuc G-Code engraving app

# Current status:
# Basic UI window made, probably lotta work to get it implemented.
# User input stored as variables
# actually done weirdly enough

# TODO: Document the code (always need moar documentation)
# TODO: split code into modules and subs etc. like a real program
# TODO: build functions to do the conversion, remembering SNAP
# TODO: yes?

"""
Program Idea Outline

User opens the software
User inputs basic parameters, and a string to engrave.
User clicks Convert

Program takes string and splits it into a list?
program iterates through list and builds output list with E values
Program iterates through output list and prints to output textbox
Program uses format to output G-Code with user values.

"""
