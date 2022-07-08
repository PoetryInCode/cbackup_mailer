<!--
SPDX-FileCopyrightText: 2022 Solomon Wagner

SPDX-License-Identifier: LPL-1.02
-->

[![License](https://img.shields.io/badge/License-LPL%201.02-green?style=flat&logo=Open%20Source%20Initiative)](./LICENSE.txt) ![Python Version](https://img.shields.io/badge/Python-≥3-blue?style=flat&logo=python)

# CBackup Mailer

I made this project so that CBackup would send email alerts whenever certain types of logs would show up in the scheduler.

I found the built-in mailer in CBackup to be too inflexible for my purposes so I wrote this tool to fix that.

## Configuration

The program can be configured through yaml or command line.

The default config can be found here: [default.yml](./default.yml)

### Old Config Style

The script can understand old config files that have the `mail:` section, but all variables set in the mail block will be overrided by the Mailer Settings in CBackup.

## Installation

Installation is fairly simple. Use your favorite editor to create the file `/etc/systemd/system/cbackup_alert_mailer.service` and insert the following contents into the file:

```
[Unit]
Description=cbackup_alert_mailer

[Service]
Nice=5
ExecStart=/usr/bin/python3 /home/login/cbackup_alert_mail.py --config /home/login/cbackup_mailer.yml
Type=oneshot

[Install]
WantedBy=multi-user.target
```

Again, use your favorite editor to create `/etc/systemd/system/cbackup_alert_mailer.timer` and insert the following:

```
[Unit]
Description=cbackup_alert_mailer timer

[Install]
WantedBy=timers.target

[Timer]
OnCalendar=hourly
Unit=cbackup_alert_mailer.service
```

After creating the file reload the systemd daemon and list the timers to ensure that it is working
```
# systemctl daemon-reload
# systemctl list-timers --all
```

The output from `systemctl list-timers --all` should look something like this:
```
NEXT                         LEFT       LAST                         PASSED       UNIT                         ACTIVATES
Fri 2022-07-08 12:00:00 EDT  18min left n/a                          n/a          cbackup_alert_mailer.timer   cbackup_alert_mailer.service
```