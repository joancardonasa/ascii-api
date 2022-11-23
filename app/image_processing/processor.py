from PIL import Image

def check_image_size(filename: str) -> None:
    im = Image.open(filename)
    print("Successfully loaded image!")
    print(f"Image size: {im.size[0]}x{im.size[1]}")
