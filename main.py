import os
from modules.help_message import color_word, help_message
from modules.schedule import Schedule


if __name__ == '__main__':
    cal = Schedule()
    display = cal.make_calendar(cal.current_month)

    page = "calendar"

    while True:
        message = ""

        print(display)
        print(message)
        command = input("Input: ")

        if command == '.calendar':

            display = cal.make_calendar(cal.current_month)
            page = "calendar"

        elif command == ".week":

            if page == "calendar":
                cal.next_week()
                display = cal.make_calendar(cal.current_month)
            elif page == 'month_view':
                message = 'Please return to the current month to use this command'

        elif command.split()[0] == ".month":

            if len(command.split()) == 2:
                month = command.split()[1].upper()
                month_list = cal.month_list

                if month == 'current':
                    display = cal.make_calendar(cal.current_month)

                elif month in month_list:
                    if month_list.index(month) != cal.current_month:
                        display = cal.view_month(month_list.index(month))
                        page = "month_view"
                    else:
                        display = cal.make_calendar(cal.current_month)
                        page = "calendar"
            else:
                message = f"{color_word('red', 'No Month Entered')}"

        elif command.split()[0] == ".event":

            if len(command.split()) == 2:
                event = cal.get_event(command.split()[1])
                if event is not None:
                    display = event.display()
                    message = "Confirm?"
                    page = "event"
                else:
                    message = "Event is Unavailable"
            else:
                message = f"{color_word('red', 'No Event Entered')}"

        elif command == '.confirm':

            if page == "event":
                cal.select_event(command.split()[1])
                display = cal.make_calendar(cal.current_month)
            else:
                message = f"{color_word('red', 'No Event Entered')}"

        elif command == ".help":
            display = help_message

        os.system('cls')
