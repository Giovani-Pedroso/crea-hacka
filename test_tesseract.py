from PIL import Image
from pytesseract import pytesseract 
from dotenv import load_dotenv
import os
load_dotenv()

path_to_tesseract= os.getenv('TESSERACT_PATH')

print("testing tese")

img_path = "./static/texto-de-teste.png"

img = Image.open(img_path) 

pytesseract.tesseract_cmd = path_to_tesseract 

text = pytesseract.image_to_string(img, lang='por') 
  
# Displaying the extracted text 
print(text[:-1])

