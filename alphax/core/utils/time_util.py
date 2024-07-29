from datetime import datetime


class TimeUtil:

    @staticmethod
    def millisecond(time: datetime):
        return int(time.timestamp()) * 1000

    @staticmethod
    def to_str(time: datetime, fmt: str = "%Y-%m-%d %H:%M:%S"):
        return time.strftime(fmt)
