'''from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()'''



'''from tkinter import *
import ttkcalendar
import tkSimpleDialog

class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection

# Demo code:
def main():
    root = Tkinter.Tk()
    root.wm_title("CalendarDialog Demo")

    def onclick():
        cd = CalendarDialog(root)
        print(cd.result)

    button = Tkinter.Button(root, text="Click me to see a calendar!", command=onclick)
    button.pack()
    root.update()

    root.mainloop()


if __name__ == "__main__":
    main()'''




import time
import sys

def name():
    name = input("What is your name? ")
    while name.isdigit():
        print("Make sure to enter an actual name.")
        name = input("What is your name? ")
    return name

def user_input():
    while True:
        age = input("What is your age? ")
        try:
            return int(age)
            break
        except ValueError:
            try:
                return float(age)
                break
            except ValueError:
                print("Make sure to enter a real age.")

def again():
    while True:
        again = input("Play again? Yes/No ").lower()
        if again == "no":
            sys.exit(0)
        elif again == "yes":
            break
        else:
            print("That was not an option.")

while True:
    the_name = name()
    age = user_input()
    Days = age * 365
    Hours = Days * 24
    Minutes = Hours * 60
    print("Ok {}, I have your results.".format(the_name))
    time.sleep(2)
    print("If you are {} years of age....".format(age))
    time.sleep(2)
    print("You are {} days old.".format(Days))
    time.sleep(2)
    print("You are {} hours old.".format(Hours))
    time.sleep(2)
    print("You are {} minutes old!".format(Minutes))

    again()