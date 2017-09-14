#! /usr/bin/python3
# bulletPointAdder.py adds '*' to the beginning of
# each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

#TODO separate lines and add stars

pyperclip.copy(text)