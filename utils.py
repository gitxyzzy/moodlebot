from datetime import datetime, timedelta

import pytz

tz = pytz.timezone('Asia/Kolkata')


def format_timedelta(td: timedelta) -> str:
    d = td.days
    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)

    if d != 0 and h != 0:
        return f'{d}d {h}h'
    elif d != 0:
        return f'{d}d'
    elif h != 0 and m != 0:
        return f'{h}h {m}m'
    elif h != 0:
        return f'{h}h'
    elif m != 0 and s != 0:
        return f'{m}m {s}s'
    elif m != 0:
        return f'{m}m'
    else:
        return f'{s}s'


def time_remaining(now: float, timestamp: float) -> str:
    is_neg = timestamp < now
    if is_neg:
        dur = datetime.fromtimestamp(now) - datetime.fromtimestamp(timestamp)
        return f'-{format_timedelta(dur)}'
    else:
        dur = datetime.fromtimestamp(timestamp) - datetime.fromtimestamp(now)
        return format_timedelta(dur)


def format_timestamp(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, tz).strftime('%a, %d %b, %I:%M %p')
