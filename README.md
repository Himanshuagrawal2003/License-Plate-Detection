# License Plate Detection using OpenCV and Tesseract OCR

This project detects and reads vehicle license plate numbers from an image using **OpenCV** for image processing and **Tesseract OCR** for text recognition.

---

## 📖 Overview

The program:
1. Reads an image of a vehicle.
2. Detects the **license plate area** using contour detection.
3. Extracts the plate region.
4. Applies **Optical Character Recognition (OCR)** using Tesseract to read the text.
5. Displays and saves the processed images and detected plate text.

---

## 🧠 Technologies Used

- **Python 3.x**
- **OpenCV** – for image processing  
- **pytesseract** – for text extraction (OCR)
- **Tesseract OCR Engine** – must be installed separately

---

## 🛠️ Installation and Setup

### 1️⃣ Clone or Download the Project

```bash
git clone https://github.com/Himanshuagrawal2003/License-Plate-Detection.git
cd license-plate-detection
```

*(Or simply copy the `.py` file into your working directory.)*

---

### 2️⃣ Install Required Libraries

```bash
pip install opencv-python pytesseract
```

---

### 3️⃣ Install Tesseract OCR

Download from the official source:  
🔗 [Tesseract OCR for Windows (UB Mannheim Build)](https://github.com/UB-Mannheim/tesseract/wiki)

During installation, **note the path** (usually):
```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Then, update this line in your Python file:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

### 4️⃣ Add Your Image

Place your image (e.g. `car.jpg`) in the same directory as the script, or give the full path:
```python
img = cv2.imread(r"C:\path\to\your\car.jpg")
```

---

### 5️⃣ Run the Program

In your terminal or PowerShell:

```bash
python licenseplate.py
```

---

## 🧩 Output Files

After running, the following images are generated and saved automatically:

| File | Description |
|------|--------------|
| `grayscale.jpg` | Grayscale version of the original image |
| `canny.jpg` | Edge-detected image |
| `contour.jpg` | Image with detected contours |
| `licenseplate.jpg` | Cropped license plate area |
| `final.jpg` | Final extracted plate (same as licenseplate.jpg) |

The detected license plate number is printed in the terminal.

---

## 🧰 Code Structure

```
licenseplate.py      # Main Python script
car.jpg              # Input image
README.md            # Project documentation
```

---

## 🖼️ Example Output

| Step | Description |
|------|-------------|
| 1️⃣ | Image converted to grayscale |
| 2️⃣ | Edges detected using Canny |
| 3️⃣ | Contours drawn around detected plates |
| 4️⃣ | Extracted license plate and OCR text displayed |

---

## 👨‍💻 Author

**Developed by:** Himanshu Agrawal  
📧 Email: [himanshuagrawal7766@gmail.com](mailto:himanshuagrawal7766@gmail.com)  
💼 GitHub: [@Himanshuagrawal2003](https://github.com/Himanshuagrawal2003)  

---

## 📜 License

This project is licensed under the **MIT License** — free to use and modify.

---

⭐ If you like this project, consider giving it a **star** on GitHub!

