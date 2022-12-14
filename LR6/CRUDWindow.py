import os

from CommandGetter import CommandGetter
import sys
from psycopg2 import Error

sys.path.append('..')
from DBConnection import DataBase

class CRUDWindow():
    def __init__(self, table_name: str, insert_columns = None,
                 update_columns = None,
                 delete_columns = None,
                 select_columns = None,):
        self.help = f'Enter \n Here you can do CRUD on {table_name} \n Options: create read update delete back'

        self.db = DataBase()

        self.table_name = table_name
        self.insert_columns = insert_columns
        if self.insert_columns is not None:
            self.insert_getter = CommandGetter('Enter value to insert', names=self.insert_columns)
        else:
            self.insert_getter = None

        self.update_columns = update_columns
        if self.update_columns is not None and len(self.update_columns) >= 2:
            self.update_getter = CommandGetter('Enter value to update (last used to find row)',
                                               names=self.update_columns)
        else:
            self.update_getter = None

        self.delete_columns = delete_columns
        if self.delete_columns is not None:
            self.delete_getter = CommandGetter('Enter value to delete', names=self.delete_columns)
        else:
            self.delete_getter = None

        self.select_columns = select_columns

    def run(self, id_user) -> None:
        while True:
            print(self.help)
            command = input()
            if len(command) == 0:
                print("zero input is incorrect")
                continue
            if ((command == 'insert' and self.insert_getter == None)
                    or (command == 'update' and self.update_getter == None)
                    or (command == 'delete' and self.delete_getter == None)):
                print('this command is not available')
                continue
            if (command == 'read'):
                self.read()
            if (command == 'create'):
                self.create(id_user)
            if (command == 'update'):
                self.update(id_user)
            if (command == 'delete'):
                self.delete(id_user)

            if command == 'back':
                os.system('cls')
                break

    def read(self):
        columns = f"{', '.join(self.select_columns)}"
        query = f"""
                SELECT {columns}
                FROM {self.table_name}
                """

        try:
            self.db.cursor.execute(query)
        except Error as e:
            print("Error while reading:", e)
            self.db.connection.rollback()
            return

        records = self.db.cursor.fetchall()
        print("You have read")
        for record in records:
            print(record)

    def create(self, id_user):
        columns = f"{', '.join(self.insert_columns)}"
        if (id_user != None):
            columns += ', iduser'
        values = self.insert_getter.get()
        values = '\', \''.join(values)
        if (id_user != None):
            values = f"(\'{values}\', \'{id_user}\')"
        else:
            values = f"(\'{values}\')"
        query = f"""
                INSERT INTO {self.table_name} ({columns})
                VALUES
                {values};
                """

        try:
            self.db.cursor.execute(query)
        except Error as e:
            print("Error while creating:", e)
            self.db.connection.rollback()
            return

        print("created")
        self.db.connection.commit()

    def update(self, id_user):
        values = self.update_getter.get()
        columns = self.update_columns
        pairs = [f"{column} = \'{value}\', \n" for value, column in zip(values[:-1], columns[:-1])]

        set_body = " ".join(pairs)[:-3]
        where_body = f"{columns[-1]} = {values[-1]}"
        if (id_user == None):
            query = f"""
                    UPDATE {self.table_name}
                    SET {set_body}
                    WHERE {where_body};
                    """
        else:
            query = f"""
                    UPDATE {self.table_name}
                    SET {set_body}
                    WHERE {where_body} and iduser = {id_user};
                    """

        try:
            self.db.cursor.execute(query)
        except Error as e:
            print("Error while updating:", e)
            self.db.connection.rollback()
            return

        print("updated")
        self.db.connection.commit()

    def delete(self, id_user):
        del_list = self.delete_getter.get()
        i = 0
        where = ''
        for val in del_list:
            where = where + f'{self.delete_columns[i]} = {val}'
            i = i + 1
            if i != len(del_list):
                where = where + ' and '

        if (id_user == None):
            query = f"""
                    DELETE FROM {self.table_name}
                    WHERE {where}
                    """
        else:
            query = f"""
                    DELETE FROM {self.table_name}
                    WHERE {where} and iduser = {id_user}
                    """

        try:
            self.db.cursor.execute(query)
        except Error as e:
            print("Error while deleting:", e)
            self.db.connection.rollback()
            return

        print("deleted")
        self.db.connection.commit()