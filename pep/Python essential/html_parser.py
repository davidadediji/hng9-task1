
from html.parser import HTMLParser
from importlib.resources import contents

metacount = 0
class MyHTMLParser(HTMLParser):  #inheriting a class from html.parser modeule 
	def handle_comment(self, data: str):
		print("Encountered comment: ", data)
		pos = self.getpos() #het poistion in html file
		print('\t At line:', pos[0], 'position:', pos[1])
		return super().handle_comment(data)

	def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]):
		global metacount
		#count no of metacount
		if tag == 'meta':
			metacount += 1
		print("Encountered tag: ", tag)
		pos = self.getpos() #het poistion in html file
		print('\t At line:', pos[0], 'position:', pos[1])
		#get attributes
		if attrs.__len__() > 0:
			print("\tAttributes")
			for a in attrs:
				print("\t", a[0], "=", a[1])

		return super().handle_starttag(tag, attrs)

	def handle_endtag(self, tag: str):
		print("Encountered tag: ", tag)
		pos = self.getpos() #het poistion in html file
		print('\t At line:', pos[0], 'position:', pos[1])
		return super().handle_endtag(tag)

	def handle_data(self, data: str):
		if data.isspace():
			return
		print("Encountered data: ", data)
		pos = self.getpos() #het poistion in html file
		print('\t At line:', pos[0], 'position:', pos[1])
		return super().handle_data(data)

def main():
	parser = MyHTMLParser()
	f = open("samplehtml.html")
	if f.mode == 'r':
		contents = f.read()
		parser.feed(contents)
	print('Total metacount', metacount)



if __name__ == '__main__':
	main()