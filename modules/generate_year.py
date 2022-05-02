import random
from modules.events import monthly_events, weekly_events, fixed_events


def get_s_event(month, week):
    for event in fixed_events:
        if event.month == month and event.week == week:
            return event

    return None


def construct_week(month, week, monthly_event):
    s_event = get_s_event(month, week)

    events = random.sample(weekly_events, random.randint(1, 3))

    week_schedule = [0, 0, 0, 0, 0, 0, 0]

    if s_event is not None:
        if len(events) == 3:
            events.pop(random.randint(0, 2))

        day = s_event.day
        week_schedule[day] = s_event
        events.append(monthly_event)
        rand = random.sample([i for i in range(0, 7) if i != s_event.day], len(events))
    else:
        events.append(monthly_event)
        rand = random.sample(range(0, 7), len(events))

    for ind, event in enumerate(events):
        week_schedule[rand[ind]] = event

    return week_schedule


def construct_month(m: int):
    month_events = random.sample(monthly_events, 4)
    month = [construct_week(m, 0, month_events[0]),
             construct_week(m, 1, month_events[1]),
             construct_week(m, 2, month_events[2]),
             construct_week(m, 3, month_events[3])
             ]

    return month


def construct_year():
    year = [
        construct_month(0),
        construct_month(1),
        construct_month(2),
        construct_month(3),
        construct_month(4),
        construct_month(5),
        construct_month(6),
        construct_month(7),
        construct_month(8),
        construct_month(9),
        construct_month(10),
        construct_month(11)
    ]

    return year


if __name__ == '__main__':
    pass
