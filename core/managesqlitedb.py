# -*- coding: utf-8 -*-

try:
    import sqlite3 as sqlite
    from src.Colors import TextColor
    import os
except Exception as err:
    raise SystemError, TextColor.RED + str("Something is wrong with libreries " + err) + TextColor.WHITE

class DirectoryFinerDB():
    def __init__(self):
        self.dbConnection = sqlite.connect("./dbs/dirbrute.db")
        self.__create_table__()

    def __create_table__(self):
        try:
            cur = self.dbConnection.cursor()
            cur.execute("""create table if not exists tbl_dirs (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                             path varchar(100) not null);""")
            self.dbConnection.commit()
        except sqlite.Error as err:
            print TextColor.RED + str(err) + TextColor.WHITE

    def __insert_data__(self, value):
        try:
            conn = self.dbConnection.cursor()
            conn.execute("INSERT INTO tbl_dirs (path) VALUES (?);", value)
            self.dbConnection.commit()
            conn.close()
            return True
        except sqlite.Error as err:
            print TextColor.RED + str(err) + TextColor.WHITE
            return False

    def __select_data__(self, query):
        """ Selecting data from database
        :param query: you can send your query that you want
        :return: list of data
        """
        try:
            conn = self.dbConnection.cursor()
            results = conn.execute(query)
            ret_results = list()
            for row in results:
                ret_results.append(row)
            return ret_results
        except sqlite.Error as err:
            print TextColor.RED + str(err) + TextColor.WHITE

    def __delete_data__(self, ids):
        """ You can delete some records that you wannt
        :param ids: you must pass list of ids
        :return: boolean ==> if success return True then return False
        """
        try:
            cur = self.dbConnection.cursor()
            for id in ids:
                cmd = "delete from tbl_dirs where id=%s"%(id)
                cur.execute(cmd)
            self.dbConnection.commit()
            cur.close()
            return True
        except sqlite.Error:
            return False

    def __update_data__(self, id):
        """ Update data that exists in database with id
        :param id: Enter the id that you wannt update
        :return: boolean ==> if success return true then return false
        """
        try:
            cur = self.dbConnection.cursor()
            cmd = "update tbl_dirs set path=? where id=%s"%(id)
            cur.execute(cmd, id)
            self.dbConnection.commit()
            cur.close()
            return True
        except sqlite.Error:
            return False