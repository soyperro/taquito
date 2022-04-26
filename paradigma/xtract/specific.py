from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = 'Unknown.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfFileReader(pdf_file_path)

pages = [0, 2, 4] # page 1, 3, 5
pdfWriter = PdfFileWriter()

for page_num in pages:
    pdfWriter.addPage(pdf.getPage(page_num))

with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
    pdfWriter.write(f)
    f.close()