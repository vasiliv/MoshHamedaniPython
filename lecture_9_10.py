from datetime import datetime
#datetime object
dt1 = datetime(2018,1,1)
dt2 = datetime.now()
print(dt2)

#various attributes of datetime object
dt1.year
dt1.month
dt1.day
dt1.date()

#print formated datetime object
print(f"{dt2.year}:{dt2.month}")

print(dt1 > dt2)