import os


class Calendar:
    def __init__(self):
        self.current_month = 'January'
        self.display = f"""{self.current_month}"""


if __name__ == '__main__':
    cal = Calendar()
    while True:
        print(cal.display)
        inp = input(': ')
        cal.current_month = inp
        os.system('cls')
