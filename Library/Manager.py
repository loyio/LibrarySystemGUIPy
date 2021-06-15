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

        yscrollbar = ttk.Scrollbar(frame, orient='vertical')  # 右边的滑动按钮
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
        self.book_edit_book = BookEditWindow(self.m_window, 0)

    def delete_book_in_library(self):
        pass


class BookEditWindow:
    def __init__(self, master, is_edit, *args):
        top = self.top = Toplevel(master)
        top.title("编辑书籍" if is_edit else "新增书籍")
        ws = top.winfo_screenwidth()
        hs = top.winfo_screenheight()

        top.resizable(False, False)
        top.grab_set()
        label_name = ttk.Label(top, text="名称: ")
        self.entry_name = ttk.Entry(top)

        label_author = ttk.Label(top, text="作者: ")
        self.entry_author = ttk.Entry(top)

        label_press = ttk.Label(top, text="出版社: ")
        self.entry_press = ttk.Entry(top)

        label_quantity = ttk.Label(top, text="数量: ")
        self.entry_quantity = ttk.Entry(top)

        self.btn_ensure = ttk.Button(top, text="确认", command=self.ensure_command)
        self.btn_cancel = ttk.Button(top, text="取消", command=self.cancel_command)

        label_name.grid(column=0, row=0, columnspan=1, sticky=(N, S, W, E), padx=20)
        self.entry_name.grid(column=1, row=0, columnspan=1, sticky=(N, S, W, E))
        label_author.grid(column=0, row=1, columnspan=1, sticky=(N, S, W), padx=20)
        self.entry_author.grid(column=1, row=1, columnspan=1, sticky=(N, S, E))
        label_press.grid(column=0, row=2, columnspan=1, sticky=(N, S, W), padx=20)
        self.entry_press.grid(column=1, row=2, columnspan=1, sticky=(N, S, E))
        label_quantity.grid(column=0, row=3, columnspan=1, sticky=(N, S, W), padx=20)
        self.entry_quantity.grid(column=1, row=3, columnspan=1, sticky=(N, S, E))
        self.btn_ensure.grid(column=0, row=4, columnspan=1, sticky=(N, S, E, W), pady=20)
        self.btn_cancel.grid(column=1, row=4, columnspan=1, sticky=(N, S, W, E))

        coordinate = '+%d+%d' % (ws / 2, hs / 2)
        top.geometry(coordinate)

    def ensure_command(self):
        pass

    def cancel_command(self):
        self.top.grab_release()
        self.top.destroy()


if __name__ == '__main__':
    Manager()
