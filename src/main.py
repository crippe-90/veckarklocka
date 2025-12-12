from datechecker import is_nth_weekday_now
import tomllib

from constants import WEEKDAYS
from send_email import send_emails

if __name__=="__main__":
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)
        day = config["appsettings"]["DAY"]
        nth = config["appsettings"]["NTH"]
        weekday = WEEKDAYS[day]
        
        if is_nth_weekday_now(nth,weekday):
            send_emails(f"Today is the {nth} {day} of the month!")