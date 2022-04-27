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

        elif command.split()[0] == ".month":

            month = command.split()[1].upper()
            month_list = cal.month_list
            if month in month_list:
                cal.view_month(month_list.index(month))
                display = cal.make_calendar()

        elif command == ".help":
            display = """
.calendar: changes display to the calendar
    .week: proceeds to the next week

            """

        os.system('cls')
