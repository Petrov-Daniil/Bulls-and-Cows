from tkinter import *
from random import *
import re

global comain


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.hello = Label(self, text='Добро пожаловать в игру быки и коровы\n')
        self.hello.config(font=('Times New Roman', 16, 'bold'))
        self.rule = Label(self, text='Если вы уже озокомились с правилами,\nто можем начать играть')
        self.btn_game = Button(text='Играть', width=15, command=self.open_game_window)
        self.btn_exit = Button(text='Выйти из игры', width=15, command=root.destroy)
        self.init_main()

    def init_main(self):
        toolbar = Frame(bg='darkgray', bd=2)
        toolbar.pack(side=TOP, fill=X)

        btn_open_dialog = Button(toolbar, text='Об игре', command=self.open_about, bg='White', bd=0, compound=TOP)
        btn_open_dialog.pack(side=LEFT)
        btn_open_dialog = Button(toolbar, text='Автор', command=self.open_author, bg='White', bd=0, compound=TOP)
        btn_open_dialog.pack(side=LEFT)
        btn_open_dialog.pack(side=LEFT)

        self.hello.pack()
        self.rule.pack()
        self.btn_game.place(x=220, y=200)
        self.btn_exit.place(x=220, y=270)

    def open_about(self):
        Chaild()

    def open_author(self):
        Author()

    def open_game_window(self):
        global comain
        comain = 0
        comain += 1
        root.destroy()


class Chaild(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_chaild()

    def init_chaild(self):
        self.title("Об игре")
        self.geometry('700x400+400+300')
        about = Label(self,
                      text='Быки и коровы — логическая игра,\n в ходе которой за несколько попыток игрок \nдолжен определить, какое число задумал компьютер.')
        about1 = Label(self,
                       text=' Копмьютер сообщает, сколько цифр угадано без совпадения с их позициями\n в тайном числе (то есть количество коров)\n и сколько угадано вплоть до позиции в тайном числе (то есть количество быков). Например:')
        about2 = Label(self,
                       text='Задумано тайное число «3219».\nПопытка: «2310».\nрезультат: две «коровы» (две цифры: «2» и «3» — угаданы на неверных позициях)\n и один «бык» (одна цифра «1» угадана вплоть до позиции). ')

        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        about.pack()
        about1.pack()
        about2.pack()


class Author(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_author()

    def init_author(self):
        self.title("Menu")
        self.geometry('700x400+400+300')
        about = Label(self,
                      text='Курсовой проект: Быки и коровы с добавлением графического интерфейса(посредственного)')
        about1 = Label(self, text='Автор: Петров Даниил Александрович\nГруппа: ИП-912')
        about2 = Label(self, text='Я надеюсь ты это оценишь, потому что повозился я тут прилично,\n но лучше, '
                                  'у меня пока что не получилось')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        about.pack()
        about1.pack()
        about2.pack()


class Graphic(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_main()
        self.word = Label(win, text='Введите ваше число: ')
        self.word.config(font=('Arial', 15, 'bold'))
        self.entry1 = Entry(win, bd=4)
        self.check = Button(win, text='Проверить', command=self.play)
        self.status = Label(win, text="*Вводить только четырехзначные числа\n из уникальных цифры", font=('Arial', 11))
        self.bulls = Label(win, text='Быки: ')
        self.bulls.config(font=('Times New Roman', 15, 'bold'))
        self.cows = Label(win, text='Коровы: ')
        self.cows.config(font=('Times New Roman', 15, 'bold'))
        self.attempt = Label(win, text="Попытка  №")
        self.attempt.config(font=('Times New Roman', 15, 'bold'))
        self.rand_num = Label(win, text='Число ещё не загадано,\n нажмите новая игра', fg='blue')
        self.rand_num.config(font=('Times New Roman', 16, 'bold'))
        self.history_one = Label(win, text="Попытка: ", font=('Ubuntu', 12, 'italic'))
        self.history_two = Label(win, text="Попытка: ", font=('Ubuntu', 12, 'italic'))
        self.history_three = Label(win, text="Попытка: ", font=('Ubuntu', 12, 'italic'))
        self.word.grid(row=2, columnspan=3, sticky=W)
        self.entry1.grid(row=3, column=0, sticky=W)
        self.check.grid(row=3, column=1, sticky=W)
        self.status.grid(row=4, columnspan=3, sticky=S)
        self.bulls.grid(row=5, column=0, sticky=W)
        self.cows.grid(row=6, column=0, sticky=W)
        self.attempt.grid(row=7, column=0, sticky=W)
        self.history_one.grid(row=8, columnspan=3, padx=10, pady=10, sticky=W)
        self.history_two.grid(row=9, columnspan=3, padx=10, pady=10, sticky=W)
        self.history_three.grid(row=10, columnspan=3, padx=10, pady=10, sticky=W)
        self.rand_num.grid(row=11, column=1, sticky=N)

    def init_main(self):
        toolbar = Frame(bg='gray', bd=2)
        toolbar.grid(row=0, column=0, sticky=W)
        btn_open_dialog = Button(toolbar, text='Новая игра', bg='White', bd=0, command=self.rand,
                                 compound=TOP)
        btn_open_dialog.grid(row=0, column=0)
        btn_open_dialog = Button(toolbar, text='Выйти из игры', command=win.destroy, bg='White', bd=0, compound=TOP)
        btn_open_dialog.grid(row=0, column=1)

    def open_dialog(self):
        Chaild()

    def rand(self):
        global number, date_num, date_bulls, date_cows, date_attempt, temp, attempt, j, count, ai, repetition
        count = 4
        ai = True
        repetition = False
        attempt = 0
        temp = 0
        date_num = list()
        date_bulls = list()
        date_cows = list()
        date_attempt = list()
        if ai:
            number = list()
            for i in range(0, count):
                if not repetition:
                    while True:
                        e = str(randint(0, 9))
                        if not e in number:
                            break
                else:
                    e = str(randint(0, 9))
                number.append(e)
        self.rand_num.config(text='Игра началась!', fg='blue')
        self.history_one.config(text="Попытка: ", font=('Ubuntu', 12, 'italic'))
        self.history_two.config(text="Попытка: ", font=('Ubuntu', 12, 'italic'))
        self.history_three.config(text="Попытка: ", font=('Ubuntu', 12, 'italic'))
        self.bulls.config(text='Быки: ')
        self.cows.config(text='Коровы: ')
        self.attempt.config(text="Попытка  №")
        self.status.config(text="*Вводить только четырехзначные числа\n из уникальных цифры", font=('Arial', 11))

    def play(self):
        global attempt, temp, j
        numb = list(self.entry1.get())
        txt = self.entry1.get()
        if NameError:
            self.status.config(text='Создайте число для игры', fg='red')
        if not txt.isdigit():
            self.status.config(text='Нужно число!', fg='red')
            return
        if len(numb) != count:
            self.status.config(text='Неправильная длина числа', fg='red')
            return
        for i in numb:
            if numb.count(i) > 1:
                self.status.config(text='Цифры не должны повторяться!', fg='red')
                return
        cows = 0
        bulls = 0
        for i in numb:
            try:
                if numb.index(i) == number.index(i):
                    bulls += 1
                else:
                    cows += 1
            except ValueError:
                pass
        if bulls == count:
            self.status.config(text='Победа!', fg='green')
            self.rand_num.config(text='Вы угадали число!!!', fg='green')
            self.status.config(font=('Times New Roman', 15, 'bold'))
            return
        else:
            attempt = int(attempt)
            attempt += 1
            if temp == 0:
                j = 0
                temp += 1
            date_num.append(txt)
            date_bulls.append(bulls)
            date_cows.append(cows)
            date_attempt.append(attempt)
            bulls = str(bulls)
            cows = str(cows)
            attempt = str(attempt)
            self.status.config(text='Попробуйте ещё раз', fg='brown', font=('Times New Roman', 13, 'bold'))
            self.bulls.config(text="Быки: " + bulls, fg='black')
            self.cows.config(text="Коровы: " + cows, fg='black')
            self.attempt.config(text="Попытка № " + attempt, fg='black')
            try:
                self.history_one.config(
                    text=' Попытка: ' + str(date_attempt[j]) + '| число: ' + str(date_num[j]) + '| быки: ' + str(
                        date_bulls[j]) + '| коровы: ' + str(
                        date_cows[j]))
                self.history_two.config(
                    text=' Попытка: ' + str(date_attempt[j + 1]) + '| число: ' + str(
                        date_num[j + 1]) + '| быки :' + str(
                        date_bulls[j + 1]) + '| коровы: ' + str(date_cows[j + 1]))
                self.history_three.config(
                    text=' Попытка: ' + str(date_attempt[j + 2]) + '| число: ' + str(
                        date_num[j + 2]) + '| быки: ' + str(
                        date_bulls[j + 2]) + '| коровы: ' + str(
                        date_cows[j + 2]))
                j += 1
            except IndexError:
                pass


if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    app.pack()
    root.title("Bulls and Cows")
    root.geometry("600x400+600+400")
    root.resizable(False, False)
    root.mainloop()
    if comain == 1:
        win = Tk()
        app2 = Graphic(win)
        win.title("Bulls and Cows")
        win.geometry("600x400+600+400")
        win.resizable(False, False)
        win.mainloop()
