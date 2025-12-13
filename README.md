# veckarklocka [WORK IN PROGRESS]
This app sends reminders to selected people on a selected day of the month.


## Configuration
The day is selected in config.toml.
Two variables is necessary to use in the config file


```
[appsettings]
DAY="FRIDAY"
NTH=2
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
ExecStart=/usr/bin/python3 <ABSOLUTE PATH>/veckarklocka/src/main.py
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