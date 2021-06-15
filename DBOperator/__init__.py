"""
 @Project: LibrarySystemGUIPy
 @Author: loyio
 @Date: 6/12/21
"""
import pymysql
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


class DBOperator:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='123456',
                                    database='library',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def login(self, username, passwd):
        with self.conn:
            with self.conn.cursor() as cursor:
                sql = "SELECT * FROM `users` where u_name = %s and u_passwd = %s"
                try:
                    res = [int(cursor.execute(sql, (username, passwd)))]
                    if res[0] == 1:
                        res.append(cursor.fetchone()["u_role"])
                except Exception as e:
                    logging.error(e)
                    res = [0]
            self.conn.commit()
        return res

    def register(self, username, passwd, role):
        with self.conn:
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO `users` (`u_name`, `u_passwd`, `u_role`) VALUES (%s, %s, %s)"
                try:
                    res = [int(cursor.execute(sql, (username, passwd, role))), "success"]
                except Exception as e:
                    logging.error(e)
                    res = [0, e]
            self.conn.commit()
        return res

    def books_multi_condition_search(self, book_key):
        with self.conn:
            with self.conn.cursor() as cursor:
                sql = "SELECT * FROM `book` where concat(IFNULL(book_id, ''),IFNULL(book_name, ''), IFNULL(book_author, ''), IFNULL(book_press, '')) like concat ('%"+book_key+"%')"
                try:
                    res = [int(cursor.execute(sql))]
                    if res[0] == 1:
                        res.append(cursor.fetchall())
                except Exception as e:
                    logging.error(e)
                    res = [0]
            self.conn.commit()
        return res
