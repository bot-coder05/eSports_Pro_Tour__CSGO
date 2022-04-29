import random
from events import events_b, events_c, events_s


def get_s_event(month, week):
    for event in events_s:
        if event.month == month and event.week == week:
            return event
        else:
            return None


def construct_week_events(month, week, monthly_event):
    s_event = get_s_event(month, week)

    events = random.sample(events_c, random.randint(1, 3))
    events.append(monthly_event)

    week_schedule = [0, 0, 0, 0, 0, 0, 0, 0]

    if s_event is not None:
        day = s_event.day
        week_schedule[day] = s_event
        rand = random.sample([i for i in range(0, 6) if i != s_event.day], len(events))
    else:
        rand = random.sample(range(0, 6), len(events))

    for ind, event in enumerate(events):
        week_schedule[rand[ind]] = event

    return week_schedule


def construct_month(m: int):
    monthly_events = random.sample(events_b, 4)
    month = [construct_week_events(m, 0, monthly_events[0]),
             construct_week_events(m, 1, monthly_events[1]),
             construct_week_events(m, 2, monthly_events[2]),
             construct_week_events(m, 3, monthly_events[3])
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
    years = construct_year()
    print(len(years))
    print(years[0][0][0])
    print(years[1][0][0])
