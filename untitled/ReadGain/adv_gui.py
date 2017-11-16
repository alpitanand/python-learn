import tkinter
import os
main_window = tkinter.Tk()

main_window.title("Grid Demo")
main_window.geometry('640x480')

label = tkinter.Label(main_window, text="Programming is fun..!!!",)
label.grid(row=0, column=1, columnspan=3,)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=3)
main_window.columnconfigure(3, weight=3)
main_window.columnconfigure(4, weight=3)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

file_list = tkinter.Listbox(main_window)
file_list.grid(row=1, column=0, sticky='nsew', rowspan=2, pady=5, padx=5)
file_list.config(border=2, relief='sunken')

for zone in os.listdir('/Windows/System32'):
    file_list.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=file_list.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
file_list['yscrollcommand'] = listScroll.set

optionFrame = tkinter.LabelFrame(main_window, text='File details',)
optionFrame.grid(row=1)
optionFrame.grid(row=1, column=2, sticky='ne')

optionFrame2 = tkinter.LabelFrame(main_window, text='Time Stamp')
optionFrame2.grid(row=1)
optionFrame2.grid(row=3, column=0, sticky='nsew', pady=5, padx=5)

hourLabel = tkinter.Spinbox(optionFrame2, width=2, values=tuple(range(0, 24)))
minuteLabel = tkinter.Spinbox(optionFrame2, width=2, values=tuple(range(0, 60)))
secondLabel = tkinter.Spinbox(optionFrame2, width=2, values=tuple(range(0, 60)))
hourLabel.grid(row=0, column=0)
minuteLabel.grid(row=0, column=1)
secondLabel.grid(row=0, column=2)

resultLabel = tkinter.Label(main_window, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(main_window)
result.grid(row=2, column=2, sticky='sw')

rbValue = tkinter.IntVar()
rbValue.set(3)

radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Time', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Date', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

print(rbValue.get())

main_window.mainloop()
