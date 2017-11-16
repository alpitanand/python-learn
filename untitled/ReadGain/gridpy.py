import tkinter

main_window = tkinter.Tk()
main_window.title("Alpit")
main_window.geometry('640x480+8+200')

label = tkinter.Label(main_window, text='Hello world')
label.grid(row=0, column=0)

left_frame = tkinter.Frame(main_window, bg='red')
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, bg='blue', relief='raised', borderwidth=2)
canvas.grid(row=1, column=1)

right_frame = tkinter.Frame(main_window, bg ='pink')
right_frame.grid(row=1, column=2, sticky='n')

button = tkinter.Button(right_frame, text='Button')
button_2 = tkinter.Button(right_frame, text='Button_2')
button_3 = tkinter.Button(right_frame, text='Button_3')

button.grid(row=0, column=0)
button_2.grid(row=1, column=0)
button_3.grid(row=2, column=0)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

left_frame.config(relief='sunken', borderwidth=10)
right_frame.config(relief='sunken', borderwidth=10)
left_frame.grid(sticky='ns')
right_frame.grid(sticky='new')
right_frame.columnconfigure(0, weight=1)


button_2.grid(sticky='ew')
button.grid(sticky='ew')
button_3.grid(sticky='ew')

main_window.mainloop()
