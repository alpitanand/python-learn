import pyperclip

text =pyperclip.paste()
lines=text.split()
for i in range (len(lines)):
    lines[i]='*'+lines[i]
text=''.join(lines)
pyperclip.copy(text)
