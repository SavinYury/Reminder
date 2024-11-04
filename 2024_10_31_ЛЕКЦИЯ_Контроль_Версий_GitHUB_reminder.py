### ПРОГРАММА НАПОМИНАНИЕ
from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import time
import datetime
import pygame

# Создаем функцию
def set_reminder():
    time_reminder = sd.askstring(title="Укажите время напоминания", prompt="Введите время (чч : мм)")
    if time_reminder:
        try:
            hour, minute = time_reminder.split(":")
            hour = int(hour)
            minute = int(minute)
            now_time = datetime.datetime.now()
            print(now_time)
            r_time = now_time.replace(hour+hour, minute+minute, second=0)
            print(r_time)
            mb.showinfo(title="Успех", message=f"Напоминание установлено на {hour}:{minute}")
            check_time()
        except ValueError:
            mb.showerror(title="Ошибка", message=f"Неправильно указано время")

# Создаем функцию проверки текущего времени
# и сравнения со временем напоминания

def check_time():
    global r_time
    if r_time:
        now = time.time()
        if now >= r_time.timestamp():
            print("Играет музыка")
            r_time = None
        window.after(1000, check_time)

### Создаем функцию для проигрывания музыки
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("")
    pygame.mixer.music.play()


r_time = None

window = Tk()
window.title("Напоминание")
width_d = window.winfo_screenwidth()
heidth_d = window.winfo_screenheight()
window.geometry(f"400x200+{width_d//2-200}+{heidth_d//2-100}")

l = Label(window, text = "Нажмите на кнопку и установите напоминание на любое время")
l.pack(pady=10)

btn = Button(window, text = "Установить напоминание", command=set_reminder)
btn.pack()

window.mainloop()
