from tkinter import *
import math

root = Tk()
root.title("Научный калькулятор")
root.geometry("500x300")

# разбивка экрана на части с помощью надписей с текстом

# создание экрана приложения

screen = LabelFrame(root, text="Экран")
screen.pack()

screen_text = Entry(screen, width=50, relief=GROOVE, font="Arial 16", justify=RIGHT, state=DISABLED)
screen_text.pack()

# работа с памятью и очисткой
memory = LabelFrame(root, text="Память и очистка")
memory.pack()
# создание кнопок памяти и очистки
but_C = Button(memory, text="C", height=2, width=5)
but_CE = Button(memory, text="CE", height=2, width=5)
but_clear = Button(memory, text="◄", height=2, width=5)
but_MS = Button(memory, text="MS", height=2, width=5)
but_MC = Button(memory, text="MC", height=2, width=5)
but_MR = Button(memory, text="MR", height=2, width=5)
but_addM = Button(memory, text="M+", height=2, width=5)
but_munusM = Button(memory, text="M-", height=2, width=5)
# размещение кнопок в приложение
but_C.grid(row=0, column=0, padx=2)
but_CE.grid(row=0, column=1, padx=2)
but_clear.grid(row=0, column=2, padx=2)
but_MS.grid(row=0, column=3, padx=2)
but_MC.grid(row=0, column=4, padx=2)
but_MR.grid(row=0, column=5, padx=2)
but_addM.grid(row=0, column=6, padx=2)
but_munusM.grid(row=0, column=7, padx=2)

root.mainloop()
