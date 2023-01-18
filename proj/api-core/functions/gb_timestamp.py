from datetime import datetime, timezone, timedelta

# Time zone in Thailand UTC+7
tz = timezone(timedelta(hours=7))

format_iso = "%Y-%m-%d %H:%M:%S.%f%z"


def timestamp():

    # Create a date object with given timezone
    time_str = datetime.now(tz=tz).isoformat(sep=" ")

    return time_str


# print(timestamp())
def format_unix(timestamp):
    date_format = datetime.strptime(timestamp, format_iso)
    unix_time = datetime.timestamp(date_format)
    return unix_time
