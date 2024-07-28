from datetime import datetime


class TimeUtil:

    @staticmethod
    def millisecond(time: datetime):
        return int(time.timestamp()) * 1000
