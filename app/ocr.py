import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def filter_black_text(image, threshold=50):
    """
    Keeps only the black text based on a threshold. 
    Pixels with value above the threshold will be set to white, else black.
    """
    return image.point(lambda p: 255 if p > threshold else 0)

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    
    # 1. Rescale
    image = image.resize((2*image.size[0], 2*image.size[1]), Image.LANCZOS)

    # 2. Convert to grayscale
    image = image.convert('L')

    # 3. Binary thresholding
    threshold = 127
    image = image.point(lambda p: p > threshold and 255)
    
    # 4. Noise Reduction (you can adjust the radius based on the noise level)
    image = image.filter(ImageFilter.MedianFilter(3))

    image = filter_black_text(image)

    # Display the processed image (optional)
    #image.show()

    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    image_path = "app/data/scans/DL.jpg"  # replace with your image path
    extracted_text = extract_text_from_image(image_path)
    print(extracted_text)


# if __name__ == "__main__":
#     image_path = "app/data/scans/DL.jpg"  # replace with your image path
#     extracted_text = extract_text_from_image(image_path)
#     print(extracted_text)
