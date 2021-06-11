"""
 @Project: LibrarySystemGUIPy
 @Author: loyio
 @Date: 6/11/21
"""
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class LibrarySystem:

    def __init__(self, root):
        root.title("图书管理系统")
        root.resizable(False, False)
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        coordinate = '+%d+%d' % ((ws-300)/2, (hs-300)/2)
        root.geometry(coordinate)
        frame = ttk.Frame(root, borderwidth=5, relief="ridge", padding=(3, 3, 12, 12))

        welcome_img = ImageTk.PhotoImage(Image.open("resources/welcome.png").resize((300, 133)))

        welcomelbl = ttk.Label(frame, image=welcome_img)
        welcomelbl.image = welcome_img

        namelbl = ttk.Label(frame, text="用户名: ")
        name = ttk.Entry(frame)

        passwdlbl = ttk.Label(frame, text="密 码: ")
        passwd = ttk.Entry(frame)

        role = StringVar()
        role.set("student")
        rb_student = ttk.Radiobutton(frame, text='学生', variable=role, value="student")
        rb_manager = ttk.Radiobutton(frame, text='管理员', variable=role, value="manager")

        login = ttk.Button(frame, text="登录")
        register = ttk.Button(frame, text="注册")

        frame.grid(column=0, row=0, columnspan=6, rowspan=5, sticky=(N, S, E, W))
        welcomelbl.grid(column=2, row=0, columnspan=2, sticky=(N, S, E, W))
        namelbl.grid(column=2, row=1, columnspan=1, sticky=(N, S, E, W), padx=5)
        name.grid(column=3, row=1, columnspan=1, sticky=(N, S, E, W), padx=5)
        passwdlbl.grid(column=2, row=2, columnspan=1, sticky=(E, W), padx=5)
        passwd.grid(column=3, row=2, columnspan=1, sticky=(E, W), padx=5)
        rb_student.grid(column=2, row=3)
        rb_manager.grid(column=3, row=3)
        login.grid(column=2, row=4, columnspan=1)
        register.grid(column=3, row=4, columnspan=1)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=6)
        frame.columnconfigure(1, weight=6)
        frame.columnconfigure(2, weight=6)
        frame.columnconfigure(3, weight=6)
        frame.columnconfigure(4, weight=6)
        frame.columnconfigure(5, weight=6)
        frame.rowconfigure(1, weight=5)
        frame.rowconfigure(2, weight=5)
        frame.rowconfigure(3, weight=5)
        frame.rowconfigure(4, weight=5)
        frame.rowconfigure(5, weight=5)

    def calculate(self):
        pass


if __name__ == '__main__':
    root = Tk()
    LibrarySystem(root)
    root.mainloop()