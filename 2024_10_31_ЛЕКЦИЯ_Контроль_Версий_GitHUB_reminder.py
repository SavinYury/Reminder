### ПРОГРАММА НАПОМИНАНИЕ
from tkinter import * # Импортируем из tkinter все функции
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import time
import datetime
#import pygame


# Создаем функцию установки времени срабатывания
def set_reminder():
    time_reminder = sd.askstring(title="Укажите время напоминания", prompt="Введите время (чч:мм)")
    if time_reminder:
        try: # Попытаемся создать проверку на исключение
            hour, minute = time_reminder.split(":") # Создаем список часы_минуты через двоеточие
            hour = int(hour) # Переводим переменную из строчного значения в целое число
            minute = int(minute) # Переводим переменную из строчного значения в целое число
            now_time = datetime.datetime.now() # Создаем переменную текущего времени от которого пойдет отсчет
#            print(now_time)
            global r_time # Поскольку переменная r_time используется в двух функциях назначаем ее глобальной
            r_time = now_time.replace(hour=hour, minute=minute, second=0) # Создаем переменную во время которой случится напоминания
#            print(r_time)
            mb.showinfo(title="Успех", message=f"Напоминание установлено на {hour}:{minute}") # Информируем что напоминание установлено
            check_time() # Как только успешно установилось время запускаем функцию сравнения времени
        except ValueError: # При вводе значений не в режиме часов минут обрабатываем ошибку
            mb.showerror(title="Ошибка", message=f"Неправильно указано время")

# Создаем функцию постоянной проверки текущего времени и сравнения со временем напоминания
def check_time():
    global r_time # Поскольку переменная r_time используется в двух функциях назначаем ее глобальной
    if r_time: # Создаем цикл проверки как только в переменной r_time появилось значение
        now = time.time() # В переменной текущего времени
#        print(now)
        if now >= r_time.timestamp(): # Цикл если текущее время now больше или равно установленного времени в напоминании r_time
            print("Играет музыка") # То срабатывает функция включения музыки
            r_time = None # После срабатывания напоминания обнуляем переменную установленного времени r_time
        window.after(1000, check_time) # Задаем проверку значений времени каждые 1000 миллисекунд и вызываем функцию check_time

### Создаем функцию для проигрывания музыки
#def play_music():
#    pygame.mixer.init() # Создаем шаблон миксера в pygame
#    pygame.mixer.music.load("") # Команда на загрузку музыки в миксер
#    pygame.mixer.music.play() # Даем команду на проигрывание музыкального файла


r_time = None # Создали (обозначили) переменную и присвоили какое-то нулевое значение

### Создаем графический интерфейс
window = Tk()
window.title("Напоминание") # Меняем название нашего всплывающего окна
width_d = window.winfo_screenwidth() # Создаем переменную запрашивающую ширину подключенного монитора
heidth_d = window.winfo_screenheight() # Создаем переменную запрашивающую высоту подключенного монитора
window.geometry(f"400x200+{(width_d//2)-200}+{(heidth_d//2)-100}") # Располагаем в центре окна

### Создаем метку
l = Label(window, text = "--Нажмите на кнопку и установите напоминание на любое время--")
l.pack(pady=10)

### Создаем кнопку
btn = Button(window, text = "Установить напоминание", command=set_reminder)
btn.pack(pady=10)

window.mainloop()
