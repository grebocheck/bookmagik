# import module
from pdf2image import convert_from_path

print("start")
# Store Pdf with convert_from_path function
images = convert_from_path('book1.pdf',
                           poppler_path="C:\\Users\\vadim\\PycharmProjects\\bookmagik\\poopler\\poppler-21.09.0"
                                        "\\Library\\bin")

print("for")
for i in range(len(images)):
    print(i)
    # Save pages as images in the pdf
    images[i].save('book1\\page' + str(i) + '.jpg', 'JPEG')

input("finish")
