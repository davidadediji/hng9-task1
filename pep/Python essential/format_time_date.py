from datetime import datetime 


def main():
	now = datetime.now()
	print(now.strftime('%d'))
#formatting current time and date
	"""
	%y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of the month
	"""
#locale date and time
	print(now.strftime('%x'))

#time formatting 
	print('The current time is', now.strftime('%I:%M:%S'))
if __name__ == '__main__':
	main()