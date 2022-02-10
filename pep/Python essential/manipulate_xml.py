#parsing xml file

import xml.dom.minidom

lst = list()
def main():
	
	#use the parse() function to parse the xml 
	doc = xml.dom.minidom.parse('sample_xml.xml')

	print(doc.nodeName)
	print(doc.firstChild.tagName)

	#get a list of xml tags from the document and print each one 
	skills = doc.getElementsByTagName('skill')
	print('%d skills: ' %skills.length)

	for skill in skills:
		lst.append(skill.getAttribute('name'))
	print(lst)

	#create new XML tag and add it into the document 
	newskill = doc.createElement('skill')
	newskill.setAttribute("name", "jquery")
	doc.firstChild.appendChild(newskill)
if __name__ == '__main__':
	main()