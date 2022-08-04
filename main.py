import os
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# img = cv2.imread("book1\\" + "book1_page-0036.jpg")
#
# text = pytesseract.image_to_string(img, lang="rus")
# print(text)

f = open('book2_291-299.txt', 'w')

for a in range(291 ,300):
    print(f"Страница №{a}")
    if a < 10:
        n = f"00{a}"
    elif a < 100:
        n = f"0{a}"
    else:
        n = f"{a}"

    img = cv2.imread("book2\\" + f"book2_00{n}.jpg")
    text = pytesseract.image_to_string(img, lang="rus")

    f.write(text + '\n')

f.close()

