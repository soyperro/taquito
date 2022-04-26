import glob
import sys
import os
import pytesseract
from PIL import Image 
from pdf2image import convert_from_path 

def ocrpdf(path):
    pages = convert_from_path(path, 500) 
    image_counter = 1
    for page in pages: 
        filename = "page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG') 
        image_counter = image_counter + 1
    return 0

def i2t(total_pages): 
    pytesseract.pytesseract.tesseract_cmd = r'/bin/tesseract'  
    print("Converting images to text...") 
    for i in range(1, total_pages+1): 
        filename = "page_"+str(i)+".jpg"
        text = str(((pytesseract.image_to_string(Image.open(filename))))) #convert image to string
        text = text.replace('-\n', '')      #then replace hyphens with empty space
        f = open("page_"+str(i)+".txt", "w+") #create empty txt files and write extracted txt into it.
        f.write(text) 
        f.close()

def mergefiles():
    read_files = glob.glob("*.txt")
    with open("merge/result.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

file = '/home/roy/Descargas/M. Ethan Katsh - Law in a Digital World (1995, Oxford University Press) - libgen.lc.pdf'
ocr = ocrpdf(file)
i2t(ocr)
mergefiles()