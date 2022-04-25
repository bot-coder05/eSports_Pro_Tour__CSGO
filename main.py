import os
from calendar import Calendar

if __name__ == '__main__':
    calendar = Calendar()
    display = calendar.make_calendar()
    while True:
        print(display)
        command = input("Input: ")

        if command == ".week":
            calendar.next_week()
            display = calendar.make_calendar()

        os.system('cls')

# month change
# move current week
