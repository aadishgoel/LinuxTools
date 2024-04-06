from datetime import datetime, timezone
import config.config as config
TIMEZONE = timezone.utc

class Filter:
    def __init__(self):
        pass
    def filterFilesOnTimeRange(self, files, fromTime, toTime):

        fileredFiles = []
        fromTime = datetime.fromtimestamp(fromTime, tz=TIMEZONE)
        toTime = datetime.fromtimestamp(toTime, tz=TIMEZONE)
        for file in files:
            fileName, extension = file.key.split(".")
            fileTime = datetime.strptime(fileName, config.DateFormat + "/" + config.TimeFormat).replace(tzinfo=TIMEZONE)
            if fromTime < fileTime < toTime:
                fileredFiles += [file]

        return fileredFiles