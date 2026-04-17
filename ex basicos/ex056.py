import datetime

date= datetime.date(2026,5,6)
today= datetime.date.today()

time=datetime.time(20,37,0)
now=datetime.datetime.now()

now=now.strftime("%H:%M %d-%m-%Y")

print(date)
print(today)
print(time)
print(now)