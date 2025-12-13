

WEEKDAYS = {
    "MONDAY":0,
    "TUESDAY":1,
    "WEDNESDAY":2,
    "THURSDAY":3,
    "FRIDAY":4,
    "SATURDAY":5,
    "SUNDAY":6
    }

EMAIL_CREDENTIALS = {
    "HOST": "",
    "PORT": 587,
    "USER": "",
    "PASSWORD": ""
}

EMAIL_ADRESSES = []

def load_constants_from_config(config):
    global EMAIL_CREDENTIALS
    global EMAIL_ADRESSES

    EMAIL_CREDENTIALS["HOST"] = config["credentials"]["HOST"]
    EMAIL_CREDENTIALS["PORT"] = config["credentials"]["PORT"]
    EMAIL_CREDENTIALS["USER"] = config["credentials"]["USER"]
    EMAIL_CREDENTIALS["PASSWORD"] = config["credentials"]["PASSWORD"]

    EMAIL_ADRESSES.append(config["emailsettings"]["SEND_TO"])