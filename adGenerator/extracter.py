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
    file.write(detection[1])
    ingrediant = ingrediant + detection[1] + "\n"
print(ingrediant)
