#reading from json objects and file


import urllib.request
import json

def printResults(data):
	theJson = json.loads(data)
	

	if "title" in theJson['metadata']:
		print(theJson['metadata']['title'])


	#get count 
	print('The count for the earthquake event is', str(theJson['metadata']['count']))

	#get minimun longitude 
	print(theJson['bbox'][0])
	print(theJson['bbox'][1])
	print(theJson['bbox'][2])
	print(theJson['bbox'][3])

	#for each event print the place it occured
	# for i in theJson['features']:
	# 	print(i['properties']['place'])

	#pint the events that have only the magnitude greater than 4
	for i in theJson['features']:
		if i['properties']['mag'] > 4:
			print(i['properties']['mag'], i['properties']['place'])

	#print only the events where atleast one person reported feeling something

	for i in theJson['features']:
		if i['properties']['felt'] != None:
			print('the events where atleast one person felt something is:' + str(
				i['properties']['place'] + 'total reported cases is ' +  str(i['properties']['felt'])
			))

def main():
	urldata = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
	webUrl = urllib.request.urlopen(urldata)
	print('Status code: ', str(webUrl.getcode()))

	if(webUrl.getcode() == 200):
		data = webUrl.read()
		printResults(data)
	else:
		print('Received error, cannot parse results')


if __name__ == '__main__':
	main()


