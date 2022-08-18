from tkinter import *
import math


# функции для работы с памятью
def save_memory(event):
    memory_operand = screen_text.get()


def clear_memory(event):
    memory_operand = ""


def read_memory(event):
    screen_text.delete(0, last=END)
    screen_text.insert(0, memory_operand)


def add_memory(event):
    memory_operand = str(int(memory_operand) + int(screen_text.get()))


def reduce_memory(event):
    memory_operand = str(int(memory_operand) - int(screen_text.get()))


root = Tk()
root.title("Научный калькулятор")
root.geometry("500x300")

# разбивка экрана на части с помощью надписей с текстом

# создание экрана приложения

screen = LabelFrame(root, text="Экран")
screen.pack()

screen_text = Entry(screen, width=50, relief=GROOVE, font="Arial 16", justify=RIGHT)
screen_text.insert(0, "0")
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

# фрейм для размещения цифр и операций
block = Frame(root)
block.pack()

# фрейм для цифр и основных математических операций
numbers_frame = LabelFrame(block, text="Цифры")
numbers_frame.grid(row=0, column=1, padx=5)

# список для хранения цифр
sp_numbers = [Button(numbers_frame, text=str(i), height=2, width=5) for i in
              ("7", "8", "9", "+", "√", "4", "5", "6", "-", "x^2", "1", "2", "3", "/", "%", ".", "0", "+/-", "*", "=")]
# размещение кнопок на экране
k = 0
for row in range(4):
    for col in range(5):
        sp_numbers[k].grid(row=row, column=col)
        k += 1

# дополнительный блок математических операций
dopl_frame = LabelFrame(block, text="Дополнительные операции")
dopl_frame.grid(row=0, column=0)

measurements = Frame(dopl_frame)
measurements.grid(row=0, column=0, columnspan=5)

r_var = BooleanVar()
r_var.set(True)
degree = Radiobutton(measurements, text="Градусы", variable=r_var, value=True)
radians = Radiobutton(measurements, text="Радианы", variable=r_var, value=False)
degree.grid(row=0, column=0)
radians.grid(row=0, column=1)

# кнопки дополнительного блока
sp_dopl = [Button(dopl_frame, text=i, height=2, width=5) for i in
           ("sin", "ctg", "atg", "π", "e", "cos", "asin", "actg", "log2x", "ln", "tg", "acos", "x^y", "log10", "logxy")]

# размещение кнопок на экране
k = 0
for row in range(1, 4):
    for col in range(5):
        sp_dopl[k].grid(row=row, column=col, pady=3)
        k += 1

operand_left, operand_right = "0", "0"
memory_operand = ""

root.mainloop()
