from tkinter import *
from tkinter import messagebox
import webbrowser
import random

class Application(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWideget()

    def createWideget(self):
        '''
        self.w1 = Text(root,width=70,height=12,bg="gray")
        self.w1.pack()

        self.w1.insert(1.0,"012345678\nabcdef")
        self.w1.insert(2.3,"锄禾，谁知\n")

        Button(self,text="重复插入",command=self.insertText).pack(side="left")
        Button(self, text="返回文本", command=self.returnText).pack(side="left")
        Button(self, text="添加图片", command=self.addPic).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="通过tag精确控制文本", command=self.testTag).pack(side="left")

        self.label01 = Label(self,text="用户名")
        self.label01.pack()
        v1 = StringVar()
        self.label01 = Entry(self,textvariable = v1)
        self.label01.pack()
        v1.set("admin")
        print(v1.get())

        self.label02 = Label(self,text="密码")
        self.label02.pack()
        v2 = StringVar()
        self.label02= Entry(self,textvariable = v2,show="*")
        self.label02.pack()
        v2.set("123456")
        print(v2.get())

        self.btn01 = Button(self, text="登录", command=self.login)
        self.btn01.pack()

        self.btn01 = Button(self,text ="点击送花" ,command=self.songhua,bg="blue",state=None,anchor=E)
        self.btn01.pack()
        
        self.btn01["text"] = "点击送花"         #上面的方法也是可以的；
        self.btn01["command"] = self.songhua
        
        self.btnQuit = Button(self,text="退出", command=root.destroy)
        self.btnQuit.pack()

        self.label01 = Label(self,text="xufei",width=10,height=10,bg="black",fg="red")
        self.label01.pack()

        self.label01 = Label(self, text="gaoqi", width=20, height=15, bg="black", fg="red",font=("黑体", 30))
        self.label01.pack()
        
        global photo
        photo = PhotoImage(file="./imgs/wk.gif")
        self.label03=Label(self,image=photo)
        self.label03.pack()

        self.label04 = Label(self, text="背就\n家庭\n", borderwidth=5, relief="solid", justify="right")
        self.label04.pack()

        self.v=StringVar()
        self.v.set("F")

        self.v1 = Radiobutton(root,text="男性",value="M",variable=self.v)
        self.v2 = Radiobutton(root, text="女性", value="F", variable=self.v)

        self.v2.pack(side="left")
        self.v1.pack(side="left")

        Button(root,text="config",command=self.confirm).pack(side="left")

        self.codeHobby  =IntVar()
        self.videoHobby =IntVar()
        self.c1=Checkbutton(root,text="qiao daima",variable=self.codeHobby,onvalue=1,offvalue=0)
        self.c2 = Checkbutton(root, text="kanshibing", variable=self.videoHobby, onvalue=1, offvalue=0)

        self.c1.pack(side="left")
        self.c2.pack(side="left")
        Button(root, text="config", command=self.confm).pack(side="left")


        self.canvas=Canvas(self,width=300,height=200,bg="green")
        self.canvas.pack()

        line=self.canvas.create_line(10,10,30,20,40,50)
        rect=self.canvas.create_rectangle(50,50,100,100)
        oval=self.canvas.create_oval(50,50,100,100)

        global photo
        photo=PhotoImage(file="./imgs/wk.gif")
        self.canvas.create_image(150,170,image=photo)
        Button(root, text="huajuxing", command=self.draw50recg).pack(side="left")

        self.label01=Label(self,text="name")
        self.label01.grid(row=0,column=0)
        self.entry01=Entry(self)
        self.entry01.grid(row=0,column=1)
        Label(self,text="phonenum").grid(row=0,column=2)

        Label(self, text="code").grid(row=1,column=0)
        Entry(self,show="*").grid(row=1,column=1)

        Button(self, text="denglu", command=self.confm).grid(row=2,column=1,sticky=E)
        Button(self, text="quxiao", command=self.confm).grid(row=2,column=1,sticky=W)
'''
        #计算器的界面设计
        btnText=(("MC","M+","M-","MR"),
                 ("C","+","/","X"),
                 ("7","8","9","-"),
                 ("4","5","6","+"),
                 ("1", "2", "3", "="),
                 ("0", ".") )
        Entry(self).grid(row=0,column=0,columnspan=4,pady=10)

        for rindex ,r in enumerate(btnText):
            for cindex,c in enumerate(r):
                if c == "=":
                    Button(self, text=c, width=2).grid(row=rindex+1,column=cindex,rowspan=2,sticky=NSEW)
                elif c== "0":
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex,  columnspan=2,  sticky=NSEW)
                elif c == ".":
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex+1,  sticky=NSEW)
                else:
                     Button(self,text=c,width=3).grid(row=rindex+1,column=cindex,sticky=EW)


    def draw50recg(self):
        for i in range(0 , 10):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["height"])/2)

            x2 = x1 + random.randrange(int(self.canvas["width"]) / 2)
            y2 = y1 + random.randrange(int(self.canvas["height"]) / 2)
            self.canvas.create_rectangle(x1,y1,x2,y2)
            print("xufei")

    def confm(self):
        if self.videoHobby.get() == 1:
            messagebox.showinfo("ceshi", "choise the ganhuo:videoHobby")
        if self.codeHobby.get()  == 1:
            messagebox.showinfo("ceshi", "choise the ganhuo:codeHobby")

        if self.videoHobby.get() == 1 and self.codeHobby.get()  == 1:
            messagebox.showinfo("ceshi", "choise the ganhuo:codeHobby and videoHobby")

    def confirm(self):
        messagebox.showinfo("ceshi","choise the xingbie:"+self.v.get())


    def insertText(self):
        self.w1.insert(INSERT,'Gaoqi')
        self.w1.insert(END, '[SXT]')
    def returnText(self):
        print(self.w1.get(1.2,1.6))
        self.w1.insert(1.8,"gaoqi")
        print("所有文本内容：\n"+self.w1.get(1.0,END))
    def addPic(self):
        self.photo=PhotoImage(file="./imgs/wk.gif")
        self.w1.image_create(END,image=self.photo)
        pass
    def addWidget(self):
        b1=Button(self.w1,text='xufei')
        self.w1.window_create(INSERT,window=b1)
    def testTag(self):
        self.w1.delete(1.0,END)
        self.w1.insert(INSERT,"good goot study")
        self.w1.tag_add("good",1.0,1.9)
        self.w1.tag_config("good",background="yellow",foreground="red")

        self.w1.tag_add("baidu",1.10 ,  1.17)
        self.w1.tag_config("baidu" , underline=True)
        self.w1.tag_bind("baidu" , "<Button-1>" , self.webshow)


    def webshow(self,event):
        webbrowser.open("http://www.baidu.com")

    def songhua(self):
        messagebox.showinfo("送花","送你99朵玫瑰花")
    def login(self):
        usrName = self.label01.get()
        code = self.label02.get()
        print("用户名："+self.label01.get())
        print("密码：" + self.label02.get())

        if usrName =="xufei" and code =="123":
            messagebox.showinfo("提示", "正确")
        else:
            messagebox.showinfo("提示", "错误")

if __name__ == '__main__':

    root = Tk()
    root.geometry("200x255+200+300")
    root.title("一个经典的GUI的应用程序类的测试")
    app=Application(master=root)
    root.mainloop()