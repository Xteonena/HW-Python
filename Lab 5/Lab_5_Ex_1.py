import requests
from io import BytesIO
from PIL import Image
import easygui


def get_cat_image():
    """
    Gets a random cat image from cataas.com and returns it as a PIL.Image object.

    :return: PIL.Image object with cat image
    :rtype: PIL.Image.Image
    :raises Exception: if an error occurs while getting the image
    """
    url = "https://cataas.com/cat"
    response = requests.get(url)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception("Error while getting image")


def main():
    """
    The main function requests an image of a cat and displays it with PIL.Image.show().
    In case of an error, show an error message with easygui.msgbox().
    """
    try:
        cat_image = get_cat_image()
        cat_image.show()  # Display image with Pillow

    except Exception as e:
        easygui.msgbox(str(e), "Error")  # Display error message with easygui


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
