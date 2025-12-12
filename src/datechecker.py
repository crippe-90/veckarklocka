from datetime import datetime, timedelta

def nth_weekday_of_month(year, month, weekday, n):
    """
    weekday: Monday=0 ... Sunday=6
    n: 1=first, 2=second, 3=third, etc.
    Returns a datetime.date of the nth weekday.
    Raises ValueError if nth weekday does not exist.
    """

    # First day of the month
    first_day = datetime(year, month, 1)

    # Offset from the first day to the first target weekday
    offset = (weekday - first_day.weekday()) % 7

    # First occurrence of that weekday in the month
    first_occurrence = first_day + timedelta(days=offset)

    # Nth occurrence
    nth_occurrence = first_occurrence + timedelta(days=(n - 1) * 7)

    # Validate it's still in the same month
    if nth_occurrence.month != month:
        raise ValueError("That nth weekday does not exist this month")

    return nth_occurrence.date()

def is_nth_weekday_now(n, weekday):
    """
    weekday: Monday=0 ... Sunday=6
    n: 1=first, 2=second, 3=third, etc.
    Returns True if today is the nth weekday of the month.
    Otherwise False.
    """
    now = datetime.now()
    try:
        target = nth_weekday_of_month(now.year, now.month, weekday, n)
        return now.date() == target
    except ValueError:
        return False
