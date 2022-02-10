from datetime import date, time, datetime
#manipulate date and time 

def main():
	today = date.today()
	print("Today's date is", today)

	" print date component"
	print(today.day)
	print(today.month)
	print(today.year)

	#get the weekday
	weekday =today.weekday()

	days_of_week = [ 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
	print(days_of_week[weekday])

def datetime1():
	now = datetime.now()
	print(now)
#get current time
	t = datetime.time(now)
	print(t)
if __name__ == '__main__':
	# main()
	datetime1()

