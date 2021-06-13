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
from tkmacosx import Button


class LibrarySystem:

    def __init__(self, root):
        root.resizable(False, False)
        logo = PhotoImage(file='resources/icon.png')
        root.call('wm', 'iconphoto', root._w, logo)
        root.title("图书管理系统")
        root['bg'] = '#333'
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        s = ttk.Style()
        s.configure('black.TRadiobutton', background="white", foreground="black")
        s.configure('black.TFrame', background="black", foreground="black")
        s.configure('black.TLabelframe', background="white", foreground="black")
        s.configure('black.TLabel', foreground="black")

        frame = Frame(root, relief="flat")

        left_panel_img = ImageTk.PhotoImage(Image.open("resources/background.png"))
        left_panel_lbl = ttk.Label(frame, image=left_panel_img, borderwidth=0)
        left_panel_lbl.image = left_panel_img

        welcome_img = ImageTk.PhotoImage(Image.open("resources/welcome.png"))

        welcomelbl = ttk.Label(frame, image=welcome_img)
        welcomelbl.image = welcome_img

        name_frame = LabelFrame(frame, relief="ridge", text=" 用户名 : ", borderwidth=5)
        self.name_entry = Entry(name_frame, bd=0, bg="#EBEBEB", highlightthickness=0,font=('Monaco', '25'))

        passwd_frame = LabelFrame(frame, relief="ridge", text=" 密    码 : ", borderwidth=5)
        self.password_entry = Entry(passwd_frame, show="●", bd=0, bg="#EBEBEB", highlightthickness=0,font=('Helvetica', '25'))

        self.role = StringVar()
        self.role.set("student")
        rb_student = ttk.Radiobutton(frame, text='学生', variable=self.role, value="student", style='black.TRadiobutton')
        rb_manager = ttk.Radiobutton(frame, text='管理员', variable=self.role, value="manager", style="black.TRadiobutton")

        login = Button(frame, text="登录", background='#AE0E36', foreground='white', overbackground='#D32E5E',
                       activebackground=('#AE0E36', '#D32E5E'), command=self.login_command)
        register = Button(frame, text="注册", background='#667eea', foreground='white', overbackground='#764ba2',
                          activebackground=('#667eea', '#764ba2'), command=self.register_command)

        frame.grid(column=0, row=0, columnspan=6, rowspan=5, sticky=(N, S, E, W))
        welcomelbl.grid(column=2, row=0, columnspan=2, sticky=(N, S, E, W), padx=50)
        left_panel_lbl.grid(column=0, row=0, columnspan=1, rowspan=5)
        name_frame.grid(column=2, row=1, columnspan=2, sticky=(N, S, E, W), padx=50,pady=15)
        self.name_entry.grid(sticky=(N, S, E, W))
        passwd_frame.grid(column=2, row=2, columnspan=2, sticky=(N, S, E, W), padx=50, pady=15)
        self.password_entry.grid(sticky=(N, S, E, W))
        rb_student.grid(column=2, row=3, pady=20, sticky=E)
        rb_manager.grid(column=3, row=3, pady=20, sticky=W, padx=10)
        login.grid(column=2, row=4, columnspan=1)
        register.grid(column=3, row=4, columnspan=1)
        coordinate = '+%d+%d' % ((ws - left_panel_img.width() - welcome_img.width()) / 2,
                                 (hs - left_panel_img.height() - welcome_img.height()) / 2)
        root.geometry(coordinate)

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
        if self.name_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror(message='账户名或密码为空，请重新输入', icon="error")
        else:
            print(self.name_entry.get())
            dbo = DBOperator()
            res = dbo.register("niuniu", "123456", "manager")
            if res[0] == 1:
                messagebox.showinfo(message='恭喜你登录成功！！！', icon='info')
            else:
                messagebox.showerror(message='登录失败！！！', detail="用户名重复，或内部错误", icon="error")
            pass
        pass

    def register_command(self):
        if self.role.get() == "manager":
            messagebox.showerror(message='不允许注册管理员账户', icon="error")
        elif self.name_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror(message='账户名或密码为空，请重新输入', icon="error")
        else:
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
