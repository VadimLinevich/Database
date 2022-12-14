import os

from DBConnection import DataBase

class ModerWindow():
    def __init__(self, child_windows: dict):
        self.windows = child_windows
        self.help = f"Available commands: {', '.join(self.windows.keys())}, back"
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
            if command not in self.windows:
                print(f"no such window {command}")
                continue
            else:
                self.windows[command].run(id_user)