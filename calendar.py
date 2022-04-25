from tournaments import tournaments
from colored import fg, attr
import random


class Calendar:
    def __init__(self):
        self.current_month = 'JANUARY'
        self.current_week = 1

    @staticmethod
    def decorate_event_name(name, color):
        return f"{fg(color)}{attr('bold')}{name}{attr('reset')}"

    def decorate_month(self):
        return attr('bold') + " ".join(self.current_month) + attr('reset')

    @staticmethod
    def make_events():
        selected = random.sample(tournaments, random.randint(2, 4))
        return selected

    def fill_week(self):
        week = [0, 0, 0, 0, 0, 0, 0]
        events = self.make_events()
        rand = random.sample(range(0, 6), len(events))
        for index, event in enumerate(events):
            week[rand[index]] = self.decorate_event_name(event.name, event.color)

        return week

    def make_calendar(self):
        month = [self.fill_week(), self.fill_week(), self.fill_week(), self.fill_week()]
        calendar = f"""                         {self.decorate_month()}\n\n"""

        for index, week in enumerate(month):
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


if __name__ == '__main__':
    x = Calendar()
