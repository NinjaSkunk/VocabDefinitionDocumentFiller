import PyPDF2
import requests
extract = ""
finisheddoc = ""
pdf = "studyguide3.pdf"
pdfFileObj = open(pdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
for i in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(i)
	extract += pageObj.extractText()
split_list = extract.split(",")
for i in split_list:
	res = requests.get('https://www.dictionary.com/browse/' + i)
	searchforstart = (res.text).find('definition,') + 11
	searchforend = (res.text[searchforstart:]).find(':') + searchforstart
	searchforend2 = (res.text[searchforstart:]).find('.') + searchforstart
	if searchforend > searchforend2:
		finisheddoc += "\n" + i + ": " + str((res.text)[searchforstart:searchforend2])
	else:
		finisheddoc += "\n" + i + ": " + str((res.text)[searchforstart:searchforend])
print(finisheddoc)