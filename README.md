# CBackup Mailer

I made this project so that CBackup would send email alerts whenever certain types of logs would show up in the scheduler.

## Configuration

The program can be configured through yaml or command line.

The default config can be found here: [default.yml](./default.yml)

### Old Config Style

The script can understand old config files that have the `mail:` section, but all variables set in the mail block will be overrided by the Mailer Settings in CBackup.

[![License](https://img.shields.io/badge/License-LPL%201.02-blue?style=flat&logo=Open%20Source%20Initiative)](./LICENSE.txt)