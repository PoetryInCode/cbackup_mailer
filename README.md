<!--
SPDX-FileCopyrightText: 2022 Solomon Wagner

SPDX-License-Identifier: LPL-1.02
-->

[![License](https://img.shields.io/badge/License-LPL%201.02-green?style=flat&logo=Open%20Source%20Initiative)](./LICENSE.txt) ![Python Version](https://img.shields.io/badge/Python-≥3-blue?style=flat&logo=python) [![REUSE status](https://api.reuse.software/badge/github.com/PoetryInCode/cbackup_mailer)](https://api.reuse.software/info/github.com/PoetryInCode/cbackup_mailer)


# CBackup Mailer

I made this project so that CBackup would send email alerts whenever certain types of logs would show up in the scheduler.

I found the built-in mailer in CBackup to be too inflexible for my purposes so I wrote this tool to fix that.

### Old Config Style

The script can understand old config files that have the `mail:` section, but all variables set in the mail block will be overrided by the Mailer Settings in CBackup.

## Installation

Installation is fairly simple. Use your favorite editor to create the file `/etc/systemd/system/cbackup_alert_mailer.service` and insert the following contents into the file:

```
[Unit]
Description=cbackup_alert_mailer

[Service]
Nice=5
ExecStart=/usr/bin/python3 {PATH_TO_SCRIPT} --config {PATH_TO_CONFIG}
Type=oneshot

[Install]
WantedBy=multi-user.target
```

Make sure that you replace `{PATH_TO_SCRIPT}` and `{PATH_TO_CONFIG}` with your respective paths to the script and config. They should both be absolute paths because the script is run by systemd.

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

## Configuration

The default config can be found here: [default.yml](./default.yml)

However most of the configuration happens within CBackup itself under the **Mailer Settings** inside of the **System Settings** tab. This script will not work unless the **Mailer Type** is set to **SMTP** and all of the required fields are filled out.