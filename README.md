# veckarklocka [WORK IN PROGRESS]
This app sends reminders to selected people on a selected day of the month.
Currently, it supports email notifications through SMTP.


## Interested in trying it out?
This app was tested with https://ethereal.email/, which is a great tool for testing emails.
Clone this repo and give it a go.
Python 3.11.2 was used to develop this tool, but I suppose it should work with most Python 3 versions.
So far it has been tested on Debian 12 and 13.


## Configuration
The nt'h weekday of a month is selected in config.toml.


#### App settings
Two variables is necessary to use in the config file under the header `appsettings`.
`DAY` is the weekday the program should run on, in english and capital.
`NTH` is the nth time this weekday occur in this month. For example december 13 2025 will be DAY=SATURDAY and NTH=2.


#### Credentials
This may change if I find a better way to store these values in the future.
What is needed to add here is `HOST`, that is the SMTP server you wish to use.
`PORT` is the port number that the host uses.
`USER` is your username at the SMTP host.
`SEND_FROM` is the address from where the email should be sent.


##### Password
Setting the password is a bit more tricky.
`PASSWORD_ENV_NAME` is the name of the environment variable where the password is stored.
It should be a string containing the name of the environment variable, for example when developing `ETHEREAL_SMTP_PASSWORD=thepassword` was used.
The actual password is then saved in an environment variable with that name in a secure way.


#### Email settings
`MESSAGE` is the message to be sent, currently just supports strings.
`SUBJECT` is the subject of the message
`SEND_TO` is a list where you put the email adresses you wish to send your message to.


```
[appsettings]
DAY="SATURDAY"
NTH=2

[credentials]
HOST=""
PORT=587
USER=""
PASSWORD_ENV_NAME="" 
SEND_FROM=""

[emailsettings]
SEND_TO=[
]
MESSAGE="""
Hello from veckarklocka,
It seems to be working...
"""
SUBJECT="Test from veckarklocka"


```
 
 
## Usage
When the configuration has been setup an environment variable needs to be set in the system with the smtp password.


## Examples of how to use the program
One way is to use it with systemd timers.

These steps was tested on Debian 13.

### Step 0) Save the password as an environment variable
Login as root, then create a file called veckarklocka.env in some good location (perhaps /etc/)

Add the name of the environment variable and set the password, then save the file as veckarklocka.env

NOTE: The name of the environment variable is possible to change, but this is what was used for developing.
```ETHEREAL_SMTP_PASSWORD=thepassword```

Set suitable ownership and permissions to the file

```chown root:root <ABSOLUTEPATH>/veckarklocka.env```

```chmod 600 <ABSOLUTEPATH>/veckarklocka.env```

Run the ```ls -l``` command, and it should look like below
```-rw------ root root 34 Dec 15 19:26 <ABSOLUTEPATH>/veckarklocka.env``` 


### Step 1) Create a systemd service

Create a file with this content and save as `veckarklocka.service` in `/etc/systemd/system/`, or what it is called on the system.

```
[Unit]
Description=Run veckarklocka for reminding people...

[Service]
EnvironmentFile=<ABSOLUTEPATH>/veckarklocka.env
Type=oneshot
ExecStart=/usr/bin/python3 <ABSOLUTE PATH>/veckarklocka/src/main.py config=<ABSOLUTE PATH>/veckarklocka/src/config.toml
```

### Step 2) Create a systemd timer
Create a file with this content and save as `veckarklocka.timer` in `/etc/systemd/system/`, or what it is called on the system.

```
[Unit]
Description=Run veckarklocka regularly

[Timer]
# Examples:
OnCalendar=*-*-* 18:00:00   # daily at 18:00
# OnBootSec=30sec           # or after boot
# OnUnitActiveSec=5min      # or every 5 minutes

# Persistent=true              # run missed occurrences after reboot, may overload email service.

[Install]
WantedBy=timers.target
```

### Step 3) Enable the script & check how it is going
Run these commands

` sudo systemctl daemon-reload`
and
` sudo systemctl enable --now veckarklocka.timer`

Then check the logs

`journalctl -u veckarklocka.service -f`