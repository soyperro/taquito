import os 
from PIL import Image 
import pytesseract 

def main(): 
	#variable donde se encuentran las imagenes 
    path = 'C://Users//usuario//Documents//ocr//imagenes//'

    #cargamos todos los archivos de la carpeta en una lista  
    dirs = os.listdir( path )

    #recorremos la lista para extraer el texto de cada imagen 
    for file in dirs: 

    	#asignamos la ruta completa del archivo a la variable img 
        img = path+file 

        #convertimos la imagen a escala de grises y leemos el texto de la imagen mediante pytesseract 
        text = pytesseract.image_to_string(Image.open(img), lang='spa')

        #eliminamos los espacios en blanco que aparecen antes y después del texto y lo imprimimos por consola 
        print(text.strip())
        
if __name__ == "__main__": 
	main()