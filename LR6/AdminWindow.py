import os

from DBConnection import DataBase
from psycopg2 import Error

class AdminWindow():
    def __init__(self, child_windows: dict):
        self.windows = child_windows
        self.help = f"Available commands: {', '.join(self.windows.keys())}, change, logs, block, unblock, back"
        self.db = DataBase()

    def run(self, id_user = None) -> None:

        while True:
            print(self.help)
            command = input()
            if len(command) == 0:
                print("zero input is incorrect")
                continue

            if command == 'back':
                os.system('cls')
                break
            if command == 'change':
                self.change()
                continue
            if command == 'logs':
                self.logs()
                continue
            if command == 'block':
                self.block()
                continue
            if command == 'unblock':
                self.unblock()
                continue
            if command not in self.windows:
                print(f"no such window {command}")
                continue
            else:
                self.windows[command].run(id_user)

    def change(self):
        print("Here you can change user role")
        print("Enter userid")
        user_id = input()
        print("Enter roleid")
        role_id = input()
        try:
            self.db.cursor.execute(f"""
                                CALL change_role({user_id}, {role_id});
                                """
                               )
            print("role changed successfully")
            self.db.connection.commit()
        except Error as e:
            print(f"Error during proc: {e}")
            self.db.connection.rollback()

    def block(self):
        print("Here you can block user")
        print("Enter userid")
        user_id = input()
        try:
            self.db.cursor.execute(f"""
                                CALL block_user({user_id});
                                """
                               )
            print("user blocked successfully")
            self.db.connection.commit()
        except Error as e:
            print(f"Error during proc: {e}")
            self.db.connection.rollback()

    def unblock(self):
        print("Here you can unblock user")
        print("Enter userid")
        user_id = input()
        try:
            self.db.cursor.execute(f"""
                                        CALL unblock_user({user_id});
                                        """
                                   )
            print("user unblocked successfully")
            self.db.connection.commit()
        except Error as e:
            print(f"Error during proc: {e}")
            self.db.connection.rollback()

    def logs(self):
        query = """
                SELECT *
                FROM logs;
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