from PIL import Image, ImageFilter
import pytesseract
import os
import sys
import argparse
import cv2
import numpy as np
from pdf2image import convert_from_path 


def convert_pdf(path):
    """Converts PDF to image

    Parameters:
    path: str - Path to PDF file

    Returns: None

    """

    # Store all the pages of the PDF in a variable 
    pages = convert_from_path(path, 500) 

    # Counter to store images of each page of PDF to image 
    image_counter = 1

    # Iterate through all the pages stored above 
    for page in pages: 

        # Declaring filename for each page of PDF as JPG 
        # For each page, filename will be: 
        # PDF page 1 -> page_1.jpg 
        # PDF page 2 -> page_2.jpg 
        # .... 
        # PDF page n -> page_n.jpg 

        filename = "page_"+str(image_counter)+".jpg"

        # Save the image of the page in system 
        page.save(filename, 'JPEG') 

        # Increment the counter to update filename 
        image_counter = image_counter + 1

    return 


def extract_text(img):

    pytesseract.pytesseract.tesseract_cmd = r'/bin/tesseract'  
    

    text = pytesseract.image_to_string(img)  
    

    return text

result = convert_pdf('/home/roy/Escritorio/ABREVIATURAS_EMPLEADAS_A_LA_HORA_DE_CITAR.docx.pdf')
text = extract_text(result)
print(text)