# pip install easyocr --user 
__package__ 
import easyocr

# Initialize EasyOCR with the desired language(s)
reader = easyocr.Reader(['en'])

# Read text from an image file
result = reader.readtext('imgsForTesting/nycilpowerincredient.jpg')
# Print the extracted text
file = open("ingrediant.md", "w")
ingrediant = ""
for detection in result:   
    print(detection[1])
    file.write(detection[1])
    ingrediant = ingrediant + detection[1]
print(ingrediant)
