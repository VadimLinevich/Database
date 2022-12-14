import os

from DBConnection import DataBase
import psycopg2
from psycopg2 import Error

class Enter():
    def __init__(self, child_windows: dict):
        self.db = DataBase()
        connection = psycopg2.connect(host='localhost',
                                      database='MetacriticAnalogDB',
                                      port="5432",
                                      user="postgres",
                                      password="Vadzim2003")
        self.db.connect(connection)
        self.child_windows = child_windows

    def run(self) -> None:
        print("Here you can login, register and quit")
        while True:
            command = input()
            if len(command) == 0:
                print("zero input is incorrect")
                continue

            if command == 'login':
                self.login()

            if command == 'register':
                self.register()

            if command == 'quit':
                self.quit()
                break

            print("Enter login, register or quit")

    def login(self):
        print("enter email")
        email = input()
        print("enter password")
        password = input()
        self.db.cursor.execute(f'''select exists (select * from users where email = '{email}');''')
        is_email = self.db.cursor.fetchall()[0][0]
        self.db.cursor.execute(f'''select exists (select * from users where password = '{password}');''')
        is_password = self.db.cursor.fetchall()[0][0]
        if (is_email and is_password):
            os.system('cls')
            self.db.cursor.execute(f'''select id from users where email = '{email}' and password = '{password}';''')
            id_user = int(self.db.cursor.fetchall()[0][0])
            self.db.cursor.execute(f'''select idrole from users where email = '{email}' and password = '{password}';''')
            id_role = int(self.db.cursor.fetchall()[0][0])
            self.db.cursor.execute(
                f'''select is_blocked from users where email = '{email}' and password = '{password}';''')
            is_blocked = bool(self.db.cursor.fetchall()[0][0])
            if (is_blocked):
                print("You are blocked")
                return
            if (id_role == 1):
                self.child_windows['admin'].run()
            if (id_role == 2):
                self.child_windows['user'].run(id_user)
            if (id_role == 3):
                self.child_windows['moder'].run()
        else:
            print("incorrect data")

    def register(self):

        print("enter name")
        name = input()
        print("enter lastname")
        lastname = input()
        while (True):
            print("enter email")
            email = input()
            self.db.cursor.execute(f'''select exists (select * from users where email = '{email}');''')
            is_email = self.db.cursor.fetchall()[0][0]
            if (is_email):
                print('this email already exists')
                continue
            break
        print("enter password")
        password = input()

        try:
            self.db.cursor.execute(f'''insert into users(idrole, name, lastname, password, email)
                                       values
                                       (2, '{name}', '{lastname}', '{password}', '{email}');''')
            print("registration completed successfully")
            self.db.connection.commit()
        except Error as e:
            print(f"Error while creating: {e}")
            self.db.connection.rollback()

    def quit(self):
        if self.db.connection is None:
            return

        self.db.cursor.close()
        self.db.connection.close()