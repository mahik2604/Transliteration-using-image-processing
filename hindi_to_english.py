!apt install tesseract-ocr-hin
!apt install libtesseract-dev
!pip install pytesseract
!pip install indicate

from google.colab.patches import cv2_imshow
import pytesseract
from pytesseract import Output
from indicate import transliterate
import cv2
import random
try:
 from PIL import Image
except ImportError:
 import Image

#load the image
for i in range(1,101):
  num = str(i)
  s = '/content/' +  num + '.JPG'
  image = cv2.imread(s)

  # Convert the image to grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply adaptive thresholding
  thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

  # Apply morphological operations to remove noise and smooth the image
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
  morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

  # Apply contour detection
  contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Use bounding boxes to isolate text
  for c in contours:
    # Compute the bounding box for the contour
    (x, y, w, h) = cv2.boundingRect(c)
      
    # Draw the bounding box on the image
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
      
    # Crop the text region from the image
    text_region = image[y:y + h, x:x + w]

  # Recognize the text in the image using Tesseract
  text = pytesseract.image_to_string(image, lang='hin',
      config='--psm 11 --oem 3')

  #print(text)
  hindi = text.split()
  print(hindi)

  for j in hindi:
    english_translated = transliterate.hindi2english(j)
    print(english_translated)
  print("\n")
