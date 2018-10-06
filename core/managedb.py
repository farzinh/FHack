# -*- coding: utf-8 -*-

try:
    import sqlite3 as sqlite
    from src.Colors import TextColor
except Exception as err:
    raise SystemError, TextColor.RED + str("Something is wrong with libreries " + err) + TextColor.WHITE

class FHackDB(object):
    def __init__(self, dbFilePath):
        self.dbConnection = self.connection_init(dbFilePath)

    @staticmethod
    def connection_init(dbFilePath):
        try:
            connection = sqlite.connect(dbFilePath)
            return connection
        except Exception:
            return None

    # @classmethod
    # def InsertToDb():
    #     pass
    