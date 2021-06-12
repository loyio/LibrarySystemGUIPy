"""
 @Project: LibrarySystemGUIPy
 @Author: loyio
 @Date: 6/11/21
"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from DBOperator import *


class LibrarySystem:

    def __init__(self, root):
        root.title("图书管理系统")
        root.resizable(False, False)
        root.iconbitmap("resources/icon.ico")
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        coordinate = '+%d+%d' % ((ws - 426) / 2, (hs - 371) / 2)
        root.geometry(coordinate)
        frame = ttk.Frame(root, borderwidth=5, relief="ridge", padding=(3, 3, 12, 12))

        welcome_img = ImageTk.PhotoImage(Image.open("resources/welcome.png").resize((300, 133)))

        welcomelbl = ttk.Label(frame, image=welcome_img)
        welcomelbl.image = welcome_img

        name_lbl = ttk.Label(frame, text="用户名: ")
        self.name_entry = ttk.Entry(frame)

        passwd_lbl = ttk.Label(frame, text="密    码: ")
        self.password_entry = ttk.Entry(frame)

        self.role = StringVar()
        self.role.set("student")
        rb_student = ttk.Radiobutton(frame, text='学生', variable=self.role, value="student")
        rb_manager = ttk.Radiobutton(frame, text='管理员', variable=self.role, value="manager")

        login = ttk.Button(frame, text="登录", command=self.login_command)
        register = ttk.Button(frame, text="注册", command=self.register_command)

        frame.grid(column=0, row=0, columnspan=6, rowspan=5, sticky=(N, S, E, W))
        welcomelbl.grid(column=2, row=0, columnspan=2, sticky=(N, S, E, W), padx=50)
        name_lbl.grid(column=2, row=1, columnspan=1, sticky=E, padx=50, pady=20)
        self.name_entry.grid(column=3, row=1, columnspan=1, sticky=W, pady=20)
        passwd_lbl.grid(column=2, row=2, columnspan=1, sticky=E, padx=50)
        self.password_entry.grid(column=3, row=2, columnspan=1, sticky=W)
        rb_student.grid(column=2, row=3, pady=20)
        rb_manager.grid(column=3, row=3, pady=20)
        login.grid(column=2, row=4, columnspan=1)
        register.grid(column=3, row=4, columnspan=1)

        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)
        # frame.columnconfigure(0, weight=6)
        # frame.columnconfigure(1, weight=6)
        # frame.columnconfigure(2, weight=6)
        # frame.columnconfigure(3, weight=6)
        # frame.columnconfigure(4, weight=6)
        # frame.columnconfigure(5, weight=6)
        # frame.rowconfigure(1, weight=5)
        # frame.rowconfigure(2, weight=5)
        # frame.rowconfigure(3, weight=5)
        # frame.rowconfigure(4, weight=5)
        # frame.rowconfigure(5, weight=5)

    def login_command(self):
        print(self.name_entry.get())
        print(self.role.get())
        pass

    def register_command(self):
        print(self.name_entry.get())
        dbo = DBOperator()
        res = dbo.register("niuniu", "123456", "manager")
        if res[0] == 1:
            messagebox.showinfo(message='恭喜你注册成功！！！', icon='info')
        else:
            messagebox.showerror(message='很遗憾，注册失败！！！', detail="用户名重复，或内部错误", icon="error")
        pass


if __name__ == '__main__':
    root = Tk()
    LibrarySystem(root)
    root.mainloop()
