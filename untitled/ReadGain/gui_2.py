import tkinter

main_window = tkinter.Tk()

main_window.title("Python Window")
main_window.geometry("640x480")
explanation = """At present only gif and small images are supported and after adding an interface""" \
              """ everything will be supported"""
picture = tkinter.PhotoImage(file="flask.png")
label = tkinter.Label(main_window,  padx=10, text=explanation,)
label.pack(side='left')

label_2 = tkinter.Label(main_window, image=picture)
label_2.pack(side='right')

# canvas = tkinter.Canvas(main_window, relief='raised', borderwidth=1)
# canvas.pack(side='bottom')
left_frame = tkinter.Frame(main_window)
left_frame.pack(side='right', anchor='n', fill=tkinter.Y, expand=False,)

button = tkinter.Button(left_frame, borderwidth=1, text='Button')
button_1 = tkinter.Button(left_frame, borderwidth=1, text='Button 1')
button_2 = tkinter.Button(left_frame, borderwidth=1, text='Button 2')
button.pack(side='bottom',)
button_1.pack(side='bottom',)
button_2.pack(side='bottom',)


main_window.mainloop()

