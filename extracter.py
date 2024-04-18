# pip install easyocr --user 
import easyocr

# Initialize EasyOCR with the desired language(s)
reader = easyocr.Reader(['en'])

# Read text from an image file
result = reader.readtext('imgsForTesting/nycilpowerincredient.jpg')
# Print the extracted text
for detection in result:
    print(detection[1])
