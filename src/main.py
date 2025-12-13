import tomllib
import sys

from datechecker import is_nth_weekday_now
from constants import WEEKDAYS, load_constants_from_config
from send_email import send_emails

if __name__=="__main__":
    config_path = "config.toml"
    if len(sys.argv) > 1 and sys.argv[1] and sys.argv[1].startswith("config="):
        arg = sys.argv[1]
        config_path = arg.split('=')[1]
    else:
        print("No config path provided, using default 'config.toml'")
    
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
        day = config["appsettings"]["DAY"]
        nth = config["appsettings"]["NTH"]
        load_constants_from_config(config)
        weekday = WEEKDAYS[day]
        
        if is_nth_weekday_now(nth,weekday):
            send_emails(message=f"Today is the {nth} {day} of the month!", email_addresses=config["emailsettings"]["SEND_TO"])
