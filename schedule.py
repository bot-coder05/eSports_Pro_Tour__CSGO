from tournaments import tournaments, Tournament
from colored import fg, attr
import random


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
        self.current_month = 0
        self.current_week = 0
        self.current_year = 0
        self.month_schedule = self.make_month_schedule()

    @staticmethod
    def decorate_event_name(name, color):
        return f"{fg(color)}{attr('bold')}{name}{attr('reset')}"

    def decorate_month(self):
        return attr('bold') + " ".join(self.month_list[self.current_month]) + attr('reset')

    @staticmethod
    def make_weekly_events():
        events = random.sample(tournaments, random.randint(2, 4))
        return events

    def make_week_schedule(self):
        week = [0, 0, 0, 0, 0, 0, 0]
        events = self.make_weekly_events()
        rand = random.sample(range(0, 6), len(events))
        for index, event in enumerate(events):
            week[rand[index]] = self.decorate_event_name(event.name, event.color)

        return week

    def make_month_schedule(self):

        month = [self.make_week_schedule(), self.make_week_schedule(),
                 self.make_week_schedule(), self.make_week_schedule()]

        if self.current_month == 10:
            major = Tournament('MJR', 'red', 'SSS')
            month[0][1] = self.decorate_event_name(major.name, major.color)

        return month

    def make_calendar(self):
        calendar = f"""{self.decorate_month()} - {attr('bold')}YEAR {self.current_year}{attr('reset')}\n\n"""

        for index, week in enumerate(self.month_schedule):
            if index == self.current_week:
                decor = 'bold'
            else:
                decor = 'dim'

            week_display = f"""{attr(decor)}WEEK {index + 1}:{attr('reset')} """
            for event in week:
                if event != 0:
                    week_display = week_display + f'[ {event} ]'
                else:
                    week_display = week_display + f'[     ]'

            calendar = calendar + week_display + '\n'

        return calendar

    def next_week(self):
        if self.current_week != 3:
            self.current_week += 1
        else:
            self.current_week = 0

            if self.current_month == 11:
                self.current_month = 0
                self.current_year += 1
            else:
                self.current_month += 1

            self.month_schedule = self.make_month_schedule()

    def select_event(self, val):
        for event in self.month_schedule[self.current_week]:
            if event != 0 and val.lower() in event.lower():
                print('Here')
