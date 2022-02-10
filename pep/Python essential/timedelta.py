#timedelta allows you to perform mathematical operations on date and time 

from datetime import time, date, datetime, timedelta

#a timedelta is a span of time which you can use to perform time based mathematics

#to construct a basic time date you pass values such as days, hours, minute as parameters to that class

print(timedelta(days=365, hours=5, minutes=56))


#print todays date
now = datetime.now()
print('Today is '+ str(now))

#print one year from now

print('one year from now will be: ', str(now + timedelta(days=365)))


#timedelta that accepts more than one argumemt 

print('In two days and three weeks, it will be' + str(now + timedelta(days=2, weeks = 3)))


#date one week ago

print('one week ago date and time was', str(now - timedelta(weeks=1)))

#calculate date until April fool

today = date.today()
# print('day is', today.day)
# construct a know day

afd = date(today.year, 4, 1)

if afd < today: #when day has passed
	print('April fool\'s day already went by %d days ago' %((today-afd).day))
	afd = afd.replace(year = today.year+1)

time_to_afd = afd-today
print('It\'s just', time_to_afd.days, 'days until April fool\'s day')