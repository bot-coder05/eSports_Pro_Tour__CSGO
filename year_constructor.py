import random
from events import events_b, events_c


def construct_week_events():
    events = random.sample(events_c, random.randint(1, 4))
    return events


def construct_month():
    month = [construct_week_events(), construct_week_events(), construct_week_events(), construct_week_events()]
    monthly_events = random.sample(events_b, 4)
    for ind, week in enumerate(month):
        if len(week) == 4:
            week[random.randint(0, 3)] = monthly_events[ind]
        elif len(week) < 4:
            week.append(monthly_events[ind])

        new_week = [0, 0, 0, 0, 0, 0, 0]
        rand = random.sample(range(0, 6), len(week))
        for inds, event in enumerate(week):
            new_week[rand[inds]] = event

        month[ind] = new_week

    return month


def construct_year():
    year = [
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month(),
        construct_month()
    ]

    return year


if __name__ == '__main__':
    years = construct_year()
    print(len(years))
    print(years[0][0][0])
    print(years[1][0][0])
