import tkinter
import time
import random
import check
import gosper


class Mass:

    def __init__(self, m):
        self.value = m
        self.start = m


def game(m):
    for x in range(len(m[0])):
        for y in range(len(m)):
            if m[y][x] == 1:
                canv.create_rectangle(
                    y * 10, x * 10, (y * 10) + 10, (x * 10) + 10, tag='rect', fill='#333', outline='#FFFCCC')


def start(root):
    obj.b = True
    while obj.b:
        canv.delete('rect')
        game(check.check(obj.value))
        obj.value = check.check(obj.value)
        canv.update()
        time.sleep(0.01)


def stop(root):
    obj.b = False


def again(root):
    canv.delete('rect')
    obj.value = obj.start
    game(obj.value)
    canv.update()


def rand(root):
    p = [[random.randint(0, 1) for x in range(50)] for y in range(50)]
    obj.value = p
    game(obj.value)


def create_grid():
    for x in range(0, 500, 10):
        canv.create_line(0, x, 500, x, fill='#FFF')
    for x in range(0, 500, 10):
        canv.create_line(x, 0, x, 500, fill='#FFF')


root = tkinter.Tk()
root.title('Life')
root.resizable(False, False)

canv = tkinter.Canvas(root, width=500, height=500, bg='#CCC')
canv.pack()
create_grid()

button = tkinter.Button(root, text='Start', width=10)
button.bind('<Button-1>', start)
button.pack(side='right')

button = tkinter.Button(root, text='Stop', width=10)
button.bind('<Button-1>', stop)
button.pack(side='right')

button = tkinter.Button(root, text='Again', width=10)
button.bind('<Button-1>', again)
button.pack(side='right')

button = tkinter.Button(root, text='Random', width=10)
button.bind('<Button-1>', rand)
button.pack(side='right')

obj = Mass(gosper.p)
game(obj.start)

root.mainloop()
