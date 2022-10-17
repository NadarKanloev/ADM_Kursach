from tkinter import *
from tkinter import messagebox



def shuffle():
    return 0






root = Tk()

def btn_click():
    login = loginInput.get()
    Input = f'{str(login)}'
    s = Input.split()
    s_int = [int(item) for item in s]
    print(sum(s_int))
    messagebox.showinfo(title='Итог', message=Input)


root['bg'] = '#fafafa'   #цвет фона
root.title('Алгоритм Фишера-Йетса')
root.wm_attributes('-alpha', 1.0)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight= 1)

title = Label(frame, text='Ауга', bg='white', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

root.mainloop() #бесконечный цикл для работы программы