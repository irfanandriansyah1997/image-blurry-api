"""
Geocoder Module
@author Irfan Andriansyah <irfan@99.co>
"""
import os
from string import Template
from PIL import Image, ImageFilter


class BlurModules:
    """
    Blur Module
    """

    IMAGE = ''
    BACKGROUND = None
    INDEX = 5

    def __init__(self, images, index):
        """
        Constructor
        :param images: Str
        """
        self.IMAGE: str = os.path.abspath(os.getcwd()) + '/upload/' + images
        self.BACKGROUND = self.setterBackground()
        self.INDEX = index
    
    def setterBackground(self):
        """
        Setter background image
        """
        return Image.open(self.IMAGE)
    
    def setterBlur(self, image):
        """
        Setter background image
        """
        return image.filter(ImageFilter.GaussianBlur(radius=self.INDEX))
    
    def setterPath(self):
        base_filename = os.path.basename(self.IMAGE)
        template = Template('blur-image-$base_filename')
        path = template.substitute(base_filename=base_filename)

        return {
            "path": path,
            "full_path": os.path.abspath(os.getcwd()) + '/upload/' + path,
        }
    
    def run(self):
        blurImage = self.setterBlur(self.BACKGROUND)

        if blurImage.mode in ('RGBA', 'LA'):
            jpeg_blur = Image.new(blurImage.mode[:-1], blurImage.size, '#ffffff')
            jpeg_blur.paste(blurImage, blurImage.split()[-1])
            blurImage = jpeg_blur
        
        blurImage.save(self.setterPath().get('full_path'), 'JPEG')

        return self.setterPath().get('path')
