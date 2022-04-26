from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
  
# Path of the pdf 

  
def pdf_to_img(PDF_file): 
    print("Converting PDF to images...") 
    pages = convert_from_path(PDF_file, 500) 
      
    image_counter = 1
      

    for page in pages: 

        filename = "page_"+str(image_counter)+".jpg"

        page.save(filename, 'JPEG') 

        image_counter = image_counter + 1

    return image_counter - 1

  
def img_to_txt(total_pages): 

    print("Converting images to text...") 

    for i in range(1, total_pages+1): 

        filename = "page_"+str(i)+".jpg"

        text = str(((pytesseract.image_to_string(Image.open(filename))))) #convert image to string

        text = text.replace('-\n', '')      #then replace hyphens with empty space

        f = open("page_"+str(i)+".txt", "w+") #create empty txt files and write extracted txt into it.

        f.write(text) 

        f.close()  
  
if __name__ == '__main__': 

    file = '/home/roy/Escritorio/ABREVIATURAS_EMPLEADAS_A_LA_HORA_DE_CITAR.docx.pdf'
    filelimit = pdf_to_img(file)      #convert first PDF page to image and save it as JPG

    img_to_txt(filelimit)                         #then extract text from that image