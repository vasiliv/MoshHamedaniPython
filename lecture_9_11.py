from datetime import datetime, timedelta

#datetime object
dt1 = datetime(2018,1,1) + timedelta(days=1, minutes=15)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print(duration.days)