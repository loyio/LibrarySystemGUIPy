"""
 @Project: LibrarySystemGUIPy
 @Author: loyio
 @Date: 6/11/21
"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DBOperator import *


class Manager:

    def __init__(self):
        self.m_window = Tk()
        self.m_window.title("图书管理系统-管理端")
        ws = self.m_window.winfo_screenwidth()
        hs = self.m_window.winfo_screenheight()

        frame = ttk.Frame(self.m_window, relief="flat", padding="3 3 12 12")

        keyword_label = ttk.Label(frame, text="关键词搜索 : ")
        self.keyword = StringVar()
        keyword_entry = ttk.Entry(frame, textvariable=self.keyword)

        add_btn = ttk.Button(frame, text="新增书籍", command=self.add_book_to_library)
        delete_btn = ttk.Button(frame, text="删除书籍", command=self.delete_book_in_library)

        yscrollbar = ttk.Scrollbar(frame, orient='vertical')
        self.book_tree = ttk.Treeview(frame, columns=('1', '2', '3', '4', '5'), show="headings",
                                      yscrollcommand=yscrollbar.set)
        self.book_tree.column('1', width=150, anchor='center')
        self.book_tree.column('2', width=150, anchor='center')
        self.book_tree.column('3', width=150, anchor='center')
        self.book_tree.column('4', width=150, anchor='center')
        self.book_tree.column('5', width=150, anchor='center')
        self.book_tree.heading('1', text='书号')
        self.book_tree.heading('2', text='书名')
        self.book_tree.heading('3', text='作者')
        self.book_tree.heading('4', text='出版社')
        self.book_tree.heading('5', text='数量')

        frame.grid(column=0, row=0, columnspan=5, rowspan=2, sticky=(N, S, E, W))
        keyword_label.grid(column=1, row=0, columnspan=1, sticky=(N, S, E), padx=50)
        keyword_entry.grid(column=2, row=0, columnspan=1, sticky=(E, W), pady=15)
        add_btn.grid(column=3, row=0, columnspan=1, sticky=(N, S, E), padx=50, pady=15)
        delete_btn.grid(column=4, row=0, columnspan=1, sticky=(N, S, W), pady=15)
        self.book_tree.grid(column=1, row=1, columnspan=4, sticky=(N, S, E, W), padx=50)
        self.book_tree.bind("<Double-1>", self.edit_book_in_library)

        self.m_window.columnconfigure(0, weight=1)
        self.m_window.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=6)
        frame.columnconfigure(1, weight=6)
        frame.columnconfigure(2, weight=6)
        frame.columnconfigure(3, weight=6)
        frame.columnconfigure(4, weight=6)
        frame.columnconfigure(5, weight=6)
        frame.rowconfigure(0, weight=2)
        frame.rowconfigure(1, weight=2)

        keyword_entry.bind("<Return>", lambda event: self.search_in_library())

        coordinate = '+%d+%d' % (ws / 2, hs / 2)
        self.m_window.geometry(coordinate)

        self.m_window.mainloop()

    def search_in_library(self):
        for row in self.book_tree.get_children():
            self.book_tree.delete(row)
        dbo = DBOperator()
        res = dbo.books_multi_condition_search(self.keyword.get())
        if res[0] == 0:
            messagebox.showerror(message='没有找到你想查找的书籍！！', icon="error")
        else:
            for i in range(0, len(res[1])):
                values = list(res[1][i].values())
                self.book_tree.insert('', i, values=values)

    def add_book_to_library(self):
        book_add_window = BookEditWindow(self.m_window, 0)
        self.m_window.wait_window(book_add_window)
        self.search_in_library()

    def edit_book_in_library(self, event):
        book_edit_window = BookEditWindow(self.m_window, 1, self.book_tree.item(self.book_tree.selection()[0])["values"])
        self.m_window.wait_window(book_edit_window)
        self.search_in_library()

    def delete_book_in_library(self):
        if len(self.book_tree.selection()) == 0:
            messagebox.showerror(message='请选择你要删除的书籍！！', icon="error")
        else:
            dbo = DBOperator()
            dbo.delete_book_in_library(self.book_tree.item(self.book_tree.selection()[0])["values"][0])
            self.search_in_library()


class BookEditWindow(Toplevel):
    def __init__(self, master, is_edit, *args, **kw):
        super().__init__(master, **kw)
        self.is_edit = is_edit
        self.title("编辑书籍" if is_edit else "新增书籍")
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        self.b_name = StringVar()
        self.b_author = StringVar()
        self.b_press = StringVar()
        self.b_quantity = StringVar()

        self.resizable(False, False)
        self.grab_set()

        self.setup_UI()

        if self.is_edit:
            print(args[0])
            self.book_id = args[0][0]
            self.b_name.set(args[0][1])
            self.b_author.set(args[0][2])
            self.b_press.set(args[0][3])
            self.b_quantity.set(args[0][4])

        coordinate = '+%d+%d' % (ws / 2, hs / 2)
        self.geometry(coordinate)

    def setup_UI(self):
        label_name = ttk.Label(self, text="名称: ")
        entry_name = ttk.Entry(self, textvariable=self.b_name)

        label_author = ttk.Label(self, text="作者: ")
        entry_author = ttk.Entry(self, textvariable=self.b_author)

        label_press = ttk.Label(self, text="出版社: ")
        entry_press = ttk.Entry(self, textvariable=self.b_press)

        label_quantity = ttk.Label(self, text="数量: ")
        entry_quantity = ttk.Entry(self, textvariable=self.b_quantity)

        btn_ensure = ttk.Button(self, text="确认", command=self.ensure_command)
        btn_cancel = ttk.Button(self, text="取消", command=self.window_exit)

        label_name.grid(column=0, row=0, columnspan=1, sticky=(N, S, W, E), padx=20)
        entry_name.grid(column=1, row=0, columnspan=1, sticky=(N, S, W, E))
        label_author.grid(column=0, row=1, columnspan=1, sticky=(N, S, W), padx=20)
        entry_author.grid(column=1, row=1, columnspan=1, sticky=(N, S, E))
        label_press.grid(column=0, row=2, columnspan=1, sticky=(N, S, W), padx=20)
        entry_press.grid(column=1, row=2, columnspan=1, sticky=(N, S, E))
        label_quantity.grid(column=0, row=3, columnspan=1, sticky=(N, S, W), padx=20)
        entry_quantity.grid(column=1, row=3, columnspan=1, sticky=(N, S, E))
        btn_ensure.grid(column=0, row=4, columnspan=1, sticky=(N, S, E, W), pady=20)
        btn_cancel.grid(column=1, row=4, columnspan=1, sticky=(N, S, W, E))

    def ensure_command(self):
        dbo = DBOperator()
        if self.is_edit:
            if self.b_name.get() == "" or self.b_author.get() == "" or self.b_press.get() == "" or self.b_quantity.get() == "":
                messagebox.showinfo(message="请检查输入框是否填入相应的值！！！", icon="error")
            else:
                res = dbo.update_book_in_library(self.b_name.get(), self.b_author.get(),
                                                 self.b_press.get(), self.b_quantity.get(), self.book_id)
                if res[0]:
                    messagebox.showinfo(message="修改成功！！！", icon="info")
                    self.window_exit()
                else:
                    messagebox.showinfo(message="修改失败！！！", icon="error")
        else:
            if self.b_name.get() == "" or self.b_author.get() == "" or self.b_press.get() == "" or self.b_quantity.get() == "":
                messagebox.showinfo(message="请检查输入框是否填入相应的值！！！", icon="error")
            else:
                res = dbo.add_new_book(self.b_name.get(), self.b_author.get(),
                                       self.b_press.get(), self.b_quantity.get())
                if res[0]:
                    self.window_exit()
                    messagebox.showinfo(message="添加成功！！！", icon="info")
                else:
                    messagebox.showinfo(message="添加失败！！！", icon="error")

    def window_exit(self):
        self.grab_release()
        self.destroy()


if __name__ == '__main__':
    Manager()
