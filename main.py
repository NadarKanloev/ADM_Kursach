from tkinter import *;


def shuffle():
    return 0






root = Tk()


root['bg'] = '#fafafa'   #цвет фона
root.title('Алгоритм Фишера-Йетса')
root.wm_attributes('-alpha', 1.0)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack

frame = Frame(root, bg='gray')
frame.place(relwidth=1, relheight= 1)

title = Label(frame, text='Ауга', bg='gray', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow')
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

root.mainloop()