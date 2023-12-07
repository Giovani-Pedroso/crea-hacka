from PIL import Image
import cv2
from pytesseract import pytesseract 
from dotenv import load_dotenv
import os
load_dotenv()

path_to_tesseract= os.getenv('TESSERACT_PATH')
pytesseract.tesseract_cmd = path_to_tesseract 


def rg_frente(path):
    img = cv2.imread(path)
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gry, lang="por")
    return {"text":text}

#it
def rg_costas(path):
    # img = Image.open(path) 
    print(f"getting text from the image {path}")
    img = cv2.imread(path)

    # De todos os flitros o escala de cinza é o melhor
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # text = pytesseract.image_to_string(x, lang="por")
    # print(f'text x procesing\n {text}')
    text = pytesseract.image_to_string(gry, lang="por")
    print(f'text gray procesing\n {text}')
    # text="a"
    # print(text)

    return {"text": text }
