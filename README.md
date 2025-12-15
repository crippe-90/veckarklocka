# veckarklocka [TESTED ON DEBIAN 13]
This app sends reminders to selected people on a selected day of the month.
Currently, it supports email notifications through SMTP.


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
`USER` and `PASSWORD` is your username and password at the SMTP host.
`SEND_FROM` is the address from where the email should be sent.


#### Email settings
`SEND_TO` is a list where you put the email adresses you wish to send your message to.


```
[appsettings]
DAY="SATURDAY"
NTH=2

[credentials]
HOST=""
PORT=587
USER=""
PASSWORD="" 
SEND_FROM=""

[emailsettings]
SEND_TO=[
]

```
 

## Usage
The main idea is to use it with systemd timers

### Step 1) Create a systemd service

Create a file with this content and save as `veckarklocka.service` in `/etc/systemd/system/`, or what it is called on the system.

```
[Unit]
Description=Run veckarklocka for reminding people...

[Service]
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