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

        yscrollbar = ttk.Scrollbar(frame, orient='vertical')  # 右边的滑动按钮
        self.book_tree = ttk.Treeview(frame, columns=('1', '2', '3', '4', '5'), show="headings", yscrollcommand=yscrollbar.set)
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
        keyword_label.grid(column=1, row=0, columnspan=1, sticky=(N, S, E, W), padx=50)
        keyword_entry.grid(column=2, row=0, columnspan=1, sticky=(N, S, E, W), pady=15)
        search_btn.grid(column=3, row=0, columnspan=1, sticky=(N, S, E, W), padx=50, pady=15)
        self.book_tree.grid(column=1, row=1, columnspan=3, sticky=(N, S, E, W), padx=50)
        coordinate = '+%d+%d' % (ws / 2, hs / 2)
        s_window.geometry(coordinate)

        s_window.mainloop()

    def search_in_library(self):
        dbo = DBOperator()
        res = dbo.books_multi_condition_search(self.keyword.get())
        if res[0] == 0:
            pass
        else:
            for i in (0, len(res[1])-1):
                self.book_tree.insert('', i, values=(res[1][i]))
        print(str(res))
