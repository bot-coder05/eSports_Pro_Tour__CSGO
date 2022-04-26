import os
from schedule import Schedule

if __name__ == '__main__':
    cal = Schedule()
    display = cal.make_calendar()

    while True:

        print(display)
        command = input("Input: ")

        if command == '.calendar':
            display = cal.make_calendar()
        elif command == ".week":
            cal.next_week()
            display = cal.make_calendar()
        elif command == ".help":
            display = """
                .calendar: changes display to thr calendar
                          .week: proceeds to the next week

            """

        os.system('cls')
