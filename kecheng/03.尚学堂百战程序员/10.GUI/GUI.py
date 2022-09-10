from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("我的第一个GUI的程序")
root.geometry("800x400+500+200")
btn01 = Button(root)
btn01["text"] = "点我就送花"

btn01.pack()


def songhua(e):
    messagebox.showinfo("提示", "送你一朵玫瑰花，新新我吧")


btn01.bind("<Button-1>", songhua)

root.mainloop()
