from tkinter import *
import math

operand_left, operand_right = "0", "0"
sign = ""
memory_operand = "0"


# функции для работы с памятью
def save_memory(event):
    global memory_operand
    memory_operand = screen_text.get()


def clear_memory(event):
    global memory_operand
    memory_operand = "0"


def read_memory(event):
    global memory_operand, operand_right, operand_left, sign
    screen_text.delete(0, last=END)
    if "." in memory_operand:
        if memory_operand.split(".")[1] == "0":
            memory_operand = memory_operand.split(".")[0]
    if sign == "":
        operand_left = "0"
    else:
        operand_right = "0"
    screen_text.insert(0, memory_operand)


def add_memory(event):
    global memory_operand
    memory_operand = str(float(memory_operand) + float(screen_text.get()))


def reduce_memory(event):
    global memory_operand
    memory_operand = str(float(memory_operand) - float(screen_text.get()))


# функции для работы с очисткой
def clear_c(event):
    global operand_left, operand_right, sign
    if sign == "":
        operand_left = "0"
    else:
        operand_right = "0"
    screen_text.delete(0, last=END)
    screen_text.insert(0, "0")


def clear_ce(event):
    global operand_left, operand_right, sign
    operand_left, operand_right, sign = "0", "0", ""
    screen_text.delete(0, last=END)
    screen_text.insert(0, "0")


def backspace(event):
    global operand_left, operand_right, sign
    temp = screen_text.get()[:-1]
    if len(temp) == 0:
        temp = 0
    if sign == "":
        operand_left = temp
        screen_text.delete(0, last=END)
        screen_text.insert(0, operand_left)
    else:
        operand_right = temp
        screen_text.delete(0, last=END)
        screen_text.insert(0, operand_right)


# функция отображения чисел на экране
def screen_numbers(event, k):
    global operand_left, operand_right, sign
    if sign == "":
        operand_left += k
        if operand_left[0] == "0":
            operand_left = operand_left[1:]
        screen_text.delete(0, last=END)
        screen_text.insert(0, operand_left)
    else:
        operand_right += k
        if operand_right[0] == "0":
            operand_left = operand_right[1:]
        screen_text.delete(0, last=END)
        screen_text.insert(0, operand_right)


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

but_MS.bind("<Button-1>", save_memory)
but_MC.bind("<Button-1>", clear_memory)
but_MR.bind("<Button-1>", read_memory)
but_addM.bind("<Button-1>", add_memory)
but_munusM.bind("<Button-1>", reduce_memory)
but_C.bind("<Button-1>", clear_c)
but_CE.bind("<Button-1>", clear_ce)
but_clear.bind("<Button-1>", backspace)

for i in (0, 1, 2, 5, 6, 7, 10, 11, 12, 15, 16):
    sp_numbers[i].bind("<Button-1>", lambda e, k=sp_numbers[i]["text"]: screen_numbers(e, k))

root.mainloop()
