from tkinter import *
from tkinter import messagebox
import math
import random


def shuffle(arr):
    for i in range(len(arr)-1, 0, -1):

        tmp = arr[i]
        rnd = math.floor((random.uniform(0, 1)) * (i+1))

        arr[i] = arr[rnd]
        arr[rnd] = tmp
    return arr

root = Tk()

def btn_click():
    login = loginInput.get()
    Input = f'{str(login)}'
    s = Input.split()
    s_int = [int(item) for item in s]
    shuffle(s_int)
    igl = [str(item) for item in s_int]
    messagebox.showinfo(title='Итог', message=igl)


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