from tkinter import *
from tkinter import ttk
from function import now_lesson
import time


def tick():
    watch.after(1000, tick)
    watch['text'] = time.strftime("%H:%M:%S")


def tick_for_lesson():
    lbl.after(60000, tick_for_lesson)
    lbl['text'] = now_lesson()


root = Tk()
root.title('Расписание')
root.geometry('700x600')
root.resizable(width=False, height=False)


lbl = ttk.Label(root, text=now_lesson(), font=("Arial", 15))
lbl.place(x=300, y=400)

lbl2 = ttk.Label(root, text='Время в Душанбе:', font="Arial 15")
lbl2.place(x=250, y=20)

lbl3 = ttk.Label(root, text='Сейчас:', font="Arial 15")
lbl3.place(x=305, y=360)

watch = ttk.Label(font="Arial 100")
watch.place(x=70, y=50)

tick()
# tick_for_lesson()

if __name__ == '__main__':
    root.mainloop()
