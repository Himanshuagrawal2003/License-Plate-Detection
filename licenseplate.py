import cv2
import pytesseract

# configuring pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read your actual image file
img = cv2.imread(r"C:\Users\himan\OneDrive\Desktop\Web Development\Python Program\FirstCode\car.jpg")

# Image Processing 
imgray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(imgray1, 316, 483)
contours, p = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:20]

# Detect License Plate 
for i in contours:
    area = cv2.contourArea(i)
    approx = cv2.approxPolyDP(i, 0.01*cv2.arcLength(i, True), True)
    if len(approx) == 4 and cv2.contourArea(i) > 700:
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(i)
        img4 = imgray1[y:y+h, x:x+w]
        break 

# OCR (Text Detection) 
licenseplate = pytesseract.image_to_string(img4)
cv2.putText(img, licenseplate.strip(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Save outputs 
cv2.imwrite('final.jpg', img4)
cv2.imwrite('grayscale.jpg', imgray1)
cv2.imwrite('canny.jpg', canny)
cv2.imwrite('contour.jpg', img)
cv2.imwrite('licenseplate.jpg', img4)

print("Detected License Plate:", licenseplate)

# Show images 
cv2.imshow('Grayscale', imgray1)
cv2.imshow('Canny', canny)
cv2.imshow('Detected Plate', img4)
cv2.imshow('Final Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
