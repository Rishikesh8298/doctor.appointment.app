import datetime as dt


def get_date_list(day_name):
    date_list = []
    today = dt.date.today()

    if day_name == "All Days":
        while True:
            today = today + dt.timedelta(1)
            date_list.append(str(today))
            if today.weekday() == 6:
                break
    elif day_name == "Weekends":
        while True:
            today += dt.timedelta(1)
            if today.weekday() == 5 or today.weekday() == 6:
                date_list.append(str(today))
            if today.weekday() == 6:
                break
    elif day_name == "Weekdays":
        while True:
            today += dt.timedelta(1)
            if today.weekday() == 5 or today.weekday() == 6:
                break
            date_list.append(str(today))
    elif day_name == None or day_name == "" or day_name == "None":
        pass
    else:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        days.index(day_name)
        while True:
            today += dt.timedelta(1)
            if today.weekday() == days.index(day_name):
                date_list.append(str(today))
                break
    return date_list


def this_week():
    today = dt.date.today()
    thisWeek = list()
    while True:
        thisWeek.append(today)
        if today.weekday() == 6:
            break
        today = today + dt.timedelta(1)
    return thisWeek


def next_week():
    """ Return all the dates of upcoming week."""
    date = max(this_week())
    nextWeek = list()
    for i in range(0, 7):
        date = date + dt.timedelta(1)
        nextWeek.append(date)
    return nextWeek


def whole_week():
    """Return all the dates of current week"""
    today = dt.date.today()
    date = today - dt.timedelta(today.isoweekday())
    weekDate = []
    for _ in range(0, 7):
        date = date + dt.timedelta(1)
        weekDate.append(date)
    return weekDate
