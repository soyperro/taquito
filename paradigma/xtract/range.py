from PyPDF2 import PdfFileReader, PdfFileWriter

# Note: index starts at 1 and is inclusive of the end. 
# The following will extract page 3 of the pdf file.
pdfs = {'BMC PP template.pdf': ({'start': 3, 'end': 3},)}  

for pdf, segments in pdfs.items():
    pdf_reader = PdfFileReader(open(pdf, 'rb'))
    for segment in segments:
        pdf_writer = PdfFileWriter()
        start_page = segment['start']
        end_page = segment['end']
        for page_num in range(start_page - 1, end_page):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        output_filename = f'{pdf}_{start_page}_page_{end_page}.pdf'
        with open(output_filename,'wb') as out:
            pdf_writer.write(out)