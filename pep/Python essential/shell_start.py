import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
	#make file duplicate
	if path.exists("textfile.txt"):
		#get the path to the file in the current directory
		src = path.realpath('textfile.txt')

		#make a backup copy
		dst = src + ".bak"

		#copy over the permissions, modification times and other info
		# shutil.copy(src, dst)
		# shutil.copystat(src, dst)

		#rename the original file
		# os.rename("textfile.txt", "newfile.txt")

		#put in a zip archive 
		# root_dir, tail = path.split(src)
		# shutil.make_archive("archive", "zip", root_dir)

		with ZipFile("testzip.zip", 'w') as newzip:
			newzip.write('textfile.txt')
			newzip.write('textfile.txt.bak')
			newzip.write('readme.md')



if __name__ == '__main__':
	main()