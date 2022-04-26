import cv2
import pdf2image
from pdf2image import convert_from_path
import pytesseract
import os
import PIL



def pdftoimg(fic,output_folder, poppler_path):
    # Store all the pages of the PDF in a variable 
    pages = convert_from_path(fic, dpi=500,output_folder=output_folder,thread_count=9, poppler_path=poppler_path) 

    image_counter = 0

    # Iterate through all the pages stored above 
    for page in pages: 
        filename = "page_"+str(image_counter)+".jpg"
        page.save(output_folder+filename, 'JPEG') 
        image_counter = image_counter + 1
        
    for i in os.listdir(output_folder):
        if i.endswith('.ppm'):
            os.remove(output_folder+i)

def crop_img(fic, output_folder):
    img = cv2.imread(fic)
    shape = img.shape
    crop_img = img[new_head:new_bottom, 0:shape[1]]
    cv2.imwrite(output_folder+name, crop_img)

def imgtotext(img, tesseract_path):
    # Recognize the text as string in image using pytesserct 
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    text = str(((pytesseract.image_to_string(PIL.Image.open(img))))) 
    text = text.replace('-\n', '')
    
    return text