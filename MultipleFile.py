import cv2
import pytesseract
import os
import re

# Path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the folder containing images
folder_path = "./Output16/"

# Get a sorted list of filenames
filenames = sorted(os.listdir(folder_path))

# Iterate over each file in the sorted order
for filename in filenames:
    # Construct the full path to the image file
    image_path = os.path.join(folder_path, filename)

    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to perform OCR on the grayscale image
    text = pytesseract.image_to_string(gray_image)

    # Define a regular expression pattern to match lines starting with digits and a space
    pattern = r'\b\d+\s'

    # Extract lines using the regular expression
    digit_lines = re.findall(pattern, text)

    # Initialize a variable to store the extracted text
    extracted_text = ""

    # Flag to check if the line should be added to the extracted text
    add_to_extracted_text = False

    # Iterate through the lines
    for line in text.split('\n'):
        # Check if the line matches the pattern
        if any(line.startswith(digit_line) for digit_line in digit_lines):
            # Set the flag to start adding lines to the extracted text
            add_to_extracted_text = True

        # Check if the line is not empty and the flag is set
        if add_to_extracted_text and line.strip():
            # Add the line to the extracted text
            extracted_text += line + ' '

        # Check if the line is empty (end of the block)
        if add_to_extracted_text and not line:
            # Break the loop if the block has ended
            break

    # Remove trailing spaces and newlines from the extracted text
    result_text = extracted_text.strip()
    print(result_text)
