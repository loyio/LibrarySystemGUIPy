"""
 @Project: LibrarySystemGUIPy
 @Author: loyio
 @Date: 6/11/21
"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DBOperator import *


class Student:

    def __init__(self):
        s_window = Tk()
        s_window.title("图书管理系统-学生端")
        ws = s_window.winfo_screenwidth()
        hs = s_window.winfo_screenheight()

        frame = ttk.Frame(s_window, relief="flat", padding="3 3 12 12")

        keyword_label = ttk.Label(frame, text="关键词 : ")
        self.keyword = StringVar()
        keyword_entry = ttk.Entry(frame, textvariable=self.keyword)

        search_btn = ttk.Button(frame, text="搜索", command=self.search_in_library)

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
        search_btn.grid(column=3, row=0, columnspan=1, sticky=(N, S, W), padx=50, pady=15)
        self.book_tree.grid(column=1, row=1, columnspan=3, sticky=(N, S, E, W), padx=50)

        s_window.columnconfigure(0, weight=1)
        s_window.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=5)
        frame.columnconfigure(1, weight=5)
        frame.columnconfigure(2, weight=5)
        frame.columnconfigure(3, weight=5)
        frame.columnconfigure(4, weight=5)
        frame.rowconfigure(0, weight=2)
        frame.rowconfigure(1, weight=2)

        keyword_entry.bind("<Return>", lambda event: self.search_in_library())

        coordinate = '+%d+%d' % (ws / 2, hs / 2)
        s_window.geometry(coordinate)

        s_window.mainloop()

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


if __name__ == '__main__':
    student = Student()
