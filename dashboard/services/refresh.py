from datetime import datetime


def last_update():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
