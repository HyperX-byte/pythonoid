import random
from threading import Timer
from tkinter import *
from tkinter import messagebox as tm

from pygame import mixer


class ShowGame:
    click = 0
    sum = 0

    def show_game_algo(self, btn, cbtn):
        numbers = [1, 2, 3, 4, 5]
        btn.set(random.choice(numbers))
        cbtn.configure(fg='white', bg='white')
        if int(btn.get()) in numbers:
            cbtn.config(state="disabled")
            self.click += 1
            self.sum += int(btn.get())
        if self.click == 2:
            if self.sum == 10:
                self.check_win_lose(True)
        elif self.click == 3:
            if self.sum == 10:
                self.check_win_lose(True)
            else:
                self.check_win_lose(False)

    def check_win_lose(self, decision):
        global res
        if decision:
            res = "You Win!"
            comp.configure(bg='lightgreen', font=('Helvetica', 10, 'bold'))
            t = Timer(0.2, self.restart_game)
            t.start()
        else:
            res = "Sorry! Better Luck Next Time!"
            comp.configure(bg='yellow', font=('Helvetica', 10, 'bold'))
            t = Timer(0.2, self.restart_game)
            t.start()

    def restart_game(self):
        button_1.destroy()
        button_2.destroy()
        button_3.destroy()
        button_4.destroy()
        button_5.destroy()
        button_6.destroy()
        button_7.destroy()
        button_8.destroy()
        button_9.destroy()
        computer_response.set(res)
        comp.pack(pady=100)
        restart = Button(screen, width=15, height="2", bg='white', text="Restart", cursor='hand2',
                         command=lambda: self.restart(restart))
        restart.pack()

    def restart(self, r):
        r.destroy()
        Start.destroy()
        mixer.music.rewind()
        self.show_game_gui()

    def show_game_gui(self):
        global button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9
        comp.pack_forget()
        Start.destroy()
        ins.destroy()
        self.click = 0
        self.sum = 0
        btn_1.set('?')
        btn_2.set('?')
        btn_3.set('?')
        btn_4.set('?')
        btn_5.set('?')
        btn_6.set('?')
        btn_7.set('?')
        btn_8.set('?')
        btn_9.set('?')

        button_1 = Button(screen, width=6, textvar=btn_1, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_1, button_1))
        button_1.grid(row=1, column=1)
        button_2 = Button(screen, width=6, textvar=btn_2, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_2, button_2))
        button_2.grid(row=1, column=2)
        button_3 = Button(screen, width=6, textvar=btn_3, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_3, button_3))
        button_3.grid(row=1, column=3)
        button_4 = Button(screen, width=6, textvar=btn_4, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_4, button_4))
        button_4.grid(row=2, column=1)
        button_5 = Button(screen, width=6, textvar=btn_5, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_5, button_5))
        button_5.grid(row=2, column=2)
        button_6 = Button(screen, width=6, textvar=btn_6, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_6, button_6))
        button_6.grid(row=2, column=3)
        button_7 = Button(screen, width=6, textvar=btn_7, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_7, button_7))
        button_7.grid(row=3, column=1)
        button_8 = Button(screen, width=6, textvar=btn_8, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_8, button_8))
        button_8.grid(row=3, column=2)
        button_9 = Button(screen, width=6, textvar=btn_9, height='2', font=("bold", 25), cursor='hand2', fg="white",
                          bg=random.choice(colors),
                          command=lambda: obj.show_game_algo(btn_9, button_9))
        button_9.grid(row=3, column=3)
        screen.grid_rowconfigure(0, weight=1)
        screen.grid_rowconfigure(4, weight=1)
        screen.grid_columnconfigure(0, weight=1)
        screen.grid_columnconfigure(4, weight=1)

    def start(self):
        global comp, Start,ins
        comp = Label(screen, textvar=computer_response, width=150, height='2', font=('Helvetica', 8, 'bold'))
        comp.pack(pady=100)
        computer_response.set("B\tO\tX\tB\tE\tH\tI\tN\tD")
        Start = Button(screen, width=15, text="Let's Start!", height="2", cursor='hand2',
                       command=lambda: self.show_game_gui())
        Start.pack()
        ins = Label(screen, text=" q - quit |  i - How to Play ?", fg='white', bg='black')
        ins.pack(pady=30)
        mixer.init()
        mixer.music.load('./bin/start.mp3')
        mixer.music.play()

    def key_press(self, event):
        key = event.char
        if key == 'q':
            screen.destroy()
        elif key == 'i':
            tm.showinfo("How to Play ?",
                        "Click on ? to check the number behind, you get 3 chances to check, if the sum of"+
                        " two or three  ? boxes is equal to 10. \n You Win! ")

    def center_window(self, window, w=200, h=300):
        # get screen width and height
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == "__main__":
    screen = Tk()
    obj = ShowGame()
    obj.center_window(screen, 440, 350)
    screen['bg'] = 'black'
    screen.title('Box Behind')
    screen.iconbitmap('./bin/boxbehind.ico')
    screen.bind('<Key>', lambda a: obj.key_press(a))
    res = ""
    colors = ['red', 'lightgreen', 'skyblue', 'yellow', 'pink']
    computer_response = StringVar()
    btn_1 = StringVar()
    btn_2 = StringVar()
    btn_3 = StringVar()
    btn_4 = StringVar()
    btn_5 = StringVar()
    btn_6 = StringVar()
    btn_7 = StringVar()
    btn_8 = StringVar()
    btn_9 = StringVar()
    obj.start()
    screen.mainloop()
