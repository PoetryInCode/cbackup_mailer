# CBackup Mailer

I made this project so that CBackup would send email alerts whenever certain types of logs would show up in the scheduler.

## Default Config

The default config is as follows:

```yml
# Default config for the cbackup alert mailer script
# Fill all `null` values, if applicable

database:
  host: "localhost" # host url or ip of database
  port:  3306
  user: "cbackup"
  password: null # (Optional) Your database may require a password
  # It is HIGHLY recommended that you have a password on your database
  name: "cbackup" # This is the name of the sql database that contains all of the cbackup data

mail:
  host: null # (Required) The host that the script connects to when sending mail
  port: 25
  from_email: null # The email address that the email is sent from
  from: "CBackup" # The name that appears as the sender
  to: null # (Required) The email address that mail is sent to

  security:
    ssl: No # mail not encrypted by default
    keyfile: null # Optional, may be required if ssl is set to `Yes`
    certfile: null # Optional, may be required if ssl is set to `Yes`

  # These are the levels of logs that the mailer will report in emails
  # Comment out the levels of logs that you don't want alerts about
  send_on:
    - EMERG
    - CRITICAL
    - ERROR
    - ALERT
    - WARNING
    - NOTICE
#    - DEBUG
#    - INFO
```