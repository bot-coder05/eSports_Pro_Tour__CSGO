from year_constructor import construct_year
from colored import fg, attr


class Schedule:
    def __init__(self):
        self.month_list = [
            'JANUARY',
            'FEBRUARY',
            'MARCH',
            'APRIL',
            'MAY',
            'JUNE',
            'JULY',
            'AUGUST',
            'SEPTEMBER',
            'OCTOBER',
            'NOVEMBER',
            'DECEMBER'
        ]
        self.current_month = 11
        self.current_week = 3
        self.current_year = 0
        self.count = 0

        self.year_schedule = construct_year()
        self.month_schedule = construct_year()[self.current_month]

    @staticmethod
    def decorate_event_name(name, color):
        return f"{fg(color)}{attr('bold')}{name}{attr('reset')}"

    @staticmethod
    def get_decorated_week(week):
        decorated_week = []
        for event in week:
            if event != 0:
                decorated_week.append(f"{fg(event.color) + event.name + attr('reset')}")
            else:
                decorated_week.append(0)

        return decorated_week

    def get_decorated_month(self):
        return attr('bold') + " ".join(self.month_list[self.current_month]) + attr('reset')

    def get_decorated_year(self):
        return attr('bold') + "YEAR " + str(self.current_year) + attr('reset')

    def make_calendar(self):
        calendar = f"""{self.get_decorated_month()} - {self.get_decorated_year()}\n\n"""

        for index, week in enumerate(self.month_schedule):
            if index == self.current_week:
                decor = 'bold'
            else:
                decor = 'dim'

            week_display = f"""{attr(decor)}WEEK {index + 1}:{attr('reset')} """
            decorated_week = self.get_decorated_week(week)
            for event in decorated_week:
                if event != 0:
                    week_display = week_display + f"[ {event} ]"
                else:
                    week_display = week_display + f"[     ]"

            calendar = calendar + week_display + '\n'

        return calendar

    def next_week(self):
        if self.current_week != 3:
            self.current_week += 1
        else:
            self.current_week = 0
            self.next_month()

    def next_month(self):
        if self.current_month != 11:
            self.current_month += 1
            self.month_schedule = self.year_schedule[self.current_month]
        else:
            self.current_month = 0
            self.next_year()

    def view_month(self, val):
        self.current_month = val
        self.month_schedule = self.year_schedule[self.current_month]

    def next_year(self):
        self.current_year += 1
        self.year_schedule = construct_year()
        self.month_schedule = self.year_schedule[self.current_month]

    def select_event(self, val):
        for event in self.month_schedule[self.current_week]:
            if event != 0 and val.lower() in event.lower():
                print('Here')


if __name__ == '__main__':
    x = Schedule()
