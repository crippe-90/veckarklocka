

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

EMAIL= {}

EMAIL_ADRESSES = []


def load_constants_from_config(config):
    global EMAIL_CREDENTIALS
    global EMAIL_ADRESSES
    global EMAIL

    EMAIL_CREDENTIALS["HOST"] = config["credentials"]["HOST"]
    EMAIL_CREDENTIALS["PORT"] = config["credentials"]["PORT"]
    EMAIL_CREDENTIALS["USER"] = config["credentials"]["USER"]
    EMAIL_CREDENTIALS["PASSWORD"] = config["credentials"]["PASSWORD"]
    EMAIL_CREDENTIALS["PASSWORD_ENV_NAME"] = config["credentials"]["PASSWORD_ENV_NAME"]

    EMAIL_ADRESSES.extend(config["emailsettings"]["SEND_TO"])

    EMAIL["MESSAGE"]=config["emailsettings"]["MESSAGE"]
    EMAIL["SUBJECT"]=config["emailsettings"]["SUBJECT"]