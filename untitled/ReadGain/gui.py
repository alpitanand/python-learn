try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
mainwindow = tkinter.Tk()
mainwindow.title("Hello World")
mainwindow.geometry('640x480+8+400')
label = tkinter.Label(mainwindow, text='Hello world')
label.pack(side='top')
canvas = tkinter.Canvas(mainwindow, relief='raised', borderwidth=1)
canvas.pack(side='left')
button1 = tkinter.Button(mainwindow, text="Alpit")
button1.pack(side='left')
mainwindow.mainloop()
