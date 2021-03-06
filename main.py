import os
from modules.help_message import color_word, help_message
from modules.schedule import Schedule
from modules.save import check_save_file, save_data, get_saved_data, fix_schedule_data


if __name__ == '__main__':
    cal = Schedule()

    if check_save_file():
        data = get_saved_data()
        cal.current_year = data['current_year']
        cal.current_month = data['current_month']
        cal.current_week = data['current_week']
        cal.year_schedule = fix_schedule_data(data['year_schedule'])
        cal.month_schedule = cal.year_schedule[cal.current_month]
    else:
        save_data(cal.year_schedule, cal.current_year, cal.current_month, cal.current_week)

    display = cal.make_calendar(cal.current_month)
    page = "calendar"
    event_selected = ""
    message = ""

    while True:

        print(display)
        print(message)
        command = input("Input: ")

        if command == "":
            pass

        elif command == '.calendar':
            display = cal.make_calendar(cal.current_month)
            page = "calendar"
            message = ""

        elif command == ".week":
            if page == "calendar":
                cal.next_week()
                display = cal.make_calendar(cal.current_month)
                message = ""
            elif page == 'month_view':
                message = 'Please return to the current month to use this command'

        elif command.split()[0] == ".month":
            if len(command.split()) == 2:
                month = command.split()[1].upper()
                month_list = cal.month_list

                if month == 'current':
                    display = cal.make_calendar(cal.current_month)
                    message = ""

                elif month in month_list:
                    if month_list.index(month) != cal.current_month:
                        display = cal.view_month(month_list.index(month))
                        page = "month_view"
                        message = ""
                    else:
                        display = cal.make_calendar(cal.current_month)
                        page = "calendar"
                        message = ""
            else:
                message = f"{color_word('red', 'No Month Entered')}"

        elif command.split()[0] == ".event":
            if len(command.split()) == 2:
                event = cal.get_event(command.split()[1])
                if event is not None:
                    display = event.display()
                    message = "Confirm?"
                    page = "event"
                    event_selected = event
                else:
                    message = "Event is Unavailable"
            else:
                message = f"{color_word('red', 'No Event Entered')}"

        elif command.split()[0] == '.confirm':
            if page == "event":
                cal.enter_event(event_selected.name)
                display = cal.make_calendar(cal.current_month)
                message = ""
            else:
                message = f"{color_word('red', 'No Event Entered')}"

        elif command == '.save':
            message = ""
            save_data(cal.year_schedule, cal.current_year, cal.current_month, cal.current_week)

        elif command == ".help":
            message = ""
            display = help_message

        os.system('cls')
