import json
import os
from modules.schedule import Schedule
from modules.events import Event, FixedEvent

abs_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


def check_save_file():
    if os.path.exists(os.getcwd() + '/data.json'):
        return True


def save_data(year_schedule, current_year, current_month, current_week):
    schedule = []
    for month in year_schedule:
        month_schedule = []
        for week in month:
            week_schedule = []
            for day in week:
                if day != 0:
                    week_schedule.append(day.encode())
                else:
                    week_schedule.append(0)
            month_schedule.append(week_schedule)
        schedule.append(month_schedule)

    data = {
        'current_year': current_year,
        'current_month': current_month,
        'current_week': current_week,
        'year_schedule': schedule
    }

    with open(os.getcwd() + '/data.json', 'w') as f:
        f.write(json.dumps(data))


def get_saved_data():
    with open(os.getcwd() + '/data.json', 'r') as f:
        data = json.load(f)

    return data


def fix_schedule_data(data):
    schedule = []
    for month in data:
        month_schedule = []
        for week in month:
            week_schedule = []
            for event in week:
                if event != 0:
                    if event['tier'] in ['S', 'A']:
                        week_schedule.append(FixedEvent(
                                                 event['name'],
                                                 event['color'],
                                                 event['tier'],
                                                 event['length'],
                                                 event['prize_pool'],
                                                 event['matches'],
                                                 event['month'],
                                                 event['week'],
                                                 event['day']
                        ))
                    else:
                        week_schedule.append(Event(
                            event['name'],
                            event['color'],
                            event['tier'],
                            event['length'],
                            event['prize_pool'],
                            event['matches']
                        ))

                else:
                    week_schedule.append(0)
            month_schedule.append(week_schedule)
        schedule.append(month_schedule)

    return schedule


if __name__ == '__main__':
    pass
