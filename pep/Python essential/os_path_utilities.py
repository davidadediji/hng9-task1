import os
from os import path

import datetime
from datetime import time, date, datetime
import time


def main():
	#to print name of os
	print(os.name)

	#check existence of an item
	print('Item exists: ' + str(path.exists('textfile.txt')))
	print('Item is a file: ' + str(path.isfile('textfile.txt')))
	print('Item is a dir: ' + str(path.isdir('textfile.txt')))

	#work with file path
	print('Item path: ' + str(path.realpath('textfile.txt')))
	print('Item path and name: ' + str(path.split(path.realpath('textfile.txt'))))

	#Get modification time 
	t = time.ctime(path.getmtime('textfile.txt'))
	print(t)
	print(datetime.fromtimestamp(path.getmtime('textfile.txt')))

	#calculate how long it was modified
	td = datetime.now() - datetime.fromtimestamp(
		path.getmtime("textfile.txt")
	)
	print("It has been " + str(td) + 'seconds the file was last modified')
	print(td.total_seconds())
if __name__ == '__main__':
	main()