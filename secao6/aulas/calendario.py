import calendar

print(calendar.calendar(2024))


for semanas in calendar.monthcalendar(2024,1):
    print(list(enumerate(semanas)))