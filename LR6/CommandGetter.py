

class CommandGetter:
    def __init__(self, help_desc: str,
                 names = None):
        self.help = help_desc
        self.names = names

    def get(self):
        print(self.help)
        return self._get_multiline()

    def _get_multiline(self):
        result = []
        i = -1
        try:
            while True:
                i += 1
                if i >= len(self.names):
                    break
                print(f"Enter {self.names[i]}:", end=' ')
                user_input = input()

                if user_input == '':
                    break

                result.append(user_input)

        except ValueError:
            print("Invalid input")
            result = []

        return result