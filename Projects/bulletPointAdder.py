#! /usr/bin/python3
# bulletPointAdder.py adds '*' to the beginning of
# each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
  lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)