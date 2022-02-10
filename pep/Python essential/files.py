def main():
	#open ait if it file for writing and create it if it doesn't exist

	# f = open('textfile.txt', 'w+', encoding='UTF-8')
	
	#open the file for appending text to the end
	f = open('textfile.txt', 'r')

	#write some lines of data to the file
	# for i in range(11):
	# 	f.write("This is line " + str(i) + "\r\n")

	#close the file when done
	# f.close()

	if f.mode == 'r':
		contents = f.readlines()
		for n in contents:
			n = n.strip()
			print(n)
if __name__ == '__main__':
	main()

