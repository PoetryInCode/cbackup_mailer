import pytest
from cbackup_alert_mail import Log, LogSeverity, LogAction, generate_mail


log = Log((1, 12, "2022-06-17 13:15:47", LogSeverity.WARNING, "scheduled", 12, 53, LogAction.TASK_START, "Test log"))

def test_htmlify():
    print(log.htmlify())
    assert log.htmlify == ""

if __name__ == "__main__":
    print(log.htmlify())