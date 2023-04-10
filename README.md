# Transliteration-using-image-processing
Transliteration of hindi script to english, using hindi text images.

This code performs Hindi to English text transliteration using Image processing and transliteration.

**Installation**
1) Install Tesseract-OCR-hin and libtesseract-dev by running the following command:

```
!apt install tesseract-ocr-hin
!apt install libtesseract-dev
```
2) Install pytesseract and indicate packages by running the following commands:
```
!pip install pytesseract
!pip install indicate
```
**Usage**

- Load the image by changing the range of the loop (in this code, it loops from 1 to 100) and setting the path of the images in the 's' variable.

- Convert the image to grayscale, apply adaptive thresholding and morphological operations to remove noise and smooth the image.

- Apply contour detection and use bounding boxes to isolate text.

- Recognize the text in the image using Tesseract.

- Transliterate the recognized Hindi text to English using Indicate Transliteration.

- The final output will be displayed on the screen.

Note: The image used in this code is in Hindi, and the language can be changed by changing the value of the 'lang' parameter in the pytesseract.image_to_string method.

**Requirements**

-Tesseract-OCR-hin

-libtesseract-dev

-pytesseract

-[indicate](Chintalapati, R., & Sood, G. (2022). Indicate: Transliterate Indic Languages to English (Version 0.1.0) [Computer software]. https://github.com/in-rolls/indicate)

-cv2

-random

-PIL


**Contribution**

Feel free to contribute to this project by forking and creating a pull request. If you find any issues, please open an issue in the GitHub repository.

**License**


This project is licensed under the [MIT License](https://github.com/mahik2604/Transliteration-using-image-processing/blob/main/LICENSE).
