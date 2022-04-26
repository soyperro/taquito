from PyPDF2 import PdfFileReader

reader = PdfFileReader("example.pdf")
page = reader.pages[0]
print(page.extractText())