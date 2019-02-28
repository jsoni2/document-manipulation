import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

print(pdfReader.isEncrypted)

pdfReader.decrypt('rosebud')

# print(pdfReader.isEncrypted) //True

pageObj = pdfReader.getPage(0)

print(pageObj.extractText)