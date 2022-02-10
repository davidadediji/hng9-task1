#read data from quabbly.com


import urllib.request

def main():
	webUrl = urllib.request.urlopen('http://google.com')
	print("status code: ", webUrl.getcode())

	data = webUrl.read()
	print(data)


if __name__ == '__main__':
	main()