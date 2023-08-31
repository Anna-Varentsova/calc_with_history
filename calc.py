import tkinter as tk

history = []


def button_click(number):
    # функция для обработки нажатия кнопок
    current = display.get()  # получаем значение с экрана ввода
    display.delete(0, tk.END)  # сбрасываем все, что было на экране до нажатия
    display.insert(tk.END, current + str(number))  # вставляем в конец поля ввода то, что нажато


def button_clear():
    # функция для очистки поля ввода/вывода
    display.delete(0, tk.END)


def button_equal():
    # функция для вывода результата вычислений
    try:
        expression = display.get()  # получаем строку с экрана ввода
        result = eval(expression)  # вычисляем выражение в строке
        history.append(expression + " = " + str(result))
        display.delete(0, tk.END)  # стираем введенное выражение с экрана
        display.insert(tk.END, result)  # выводим вместо него результат вычислений
    except ZeroDivisionError:
        display.delete(0, tk.END)  # стираем введенное выражение с экрана
        display.insert(tk.END, 'ошибка деления на 0')  # выводим ошибку деления на 0
    except SyntaxError:
        display.delete(0, tk.END)  # стираем введенное выражение с экрана
        display.insert(tk.END, 'неверное выражение')  # выводим ошибку выражения


# окно программы и заголовок:
root = tk.Tk()
root.title("Калькулятор")

# поле ввода:
display = tk.Entry(root, width=30, justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# кнопки:
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "(", "0", ")", "+",
    "."]

# первоначальное расположение кнопок в окне root:
row = 1
column = 0

# создаем кнопки и привязываем к функции button_click()
for button in buttons:
    if column == 4:
        column = 0
        row += 1

    button_widget = tk.Button(root, text=button, width=5, pady=5, command=lambda button=button: button_click(button))
    button_widget.grid(row=row, column=column, padx=5, pady=5)

    column += 1

# создаем кнопку "=" и связываем с функцией button_equal()
equal_button = tk.Button(root, text="=", width=5, pady=5, command=button_equal)
equal_button.grid(row=row, column=column, padx=5, pady=5)

# создаем кнопку "Очистить" и связываем с функцией button_clear()
clear_button = tk.Button(root, text="Очистить", width=8, pady=5, command=button_clear)
clear_button.grid(row=row, column=column+2, padx=0, pady=5)


def show_history():
    # функция для просмотра истории действий
    history_window = tk.Toplevel(root)  # создание нового окна поверх root
    history_window.title("История действий")  # заголовок
    history_label = tk.Label(history_window, text="\n".join(history), height='10', width='35')  # метка для вывода истории
    history_label.pack(padx=10, pady=20)


history_button = tk.Button(root, text="История", width=8, pady=5, command=show_history)
history_button.grid(row=row, column=column+1, padx=0, pady=5)

# запускаем главный цикл:
root.mainloop()