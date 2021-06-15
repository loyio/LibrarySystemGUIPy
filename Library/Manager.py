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
        m_window = Tk()
        m_window.title("图书管理系统-管理端")
        m_window['bg'] = '#333'
        ws = m_window.winfo_screenwidth()
        hs = m_window.winfo_screenheight()

        m_window.mainloop()
