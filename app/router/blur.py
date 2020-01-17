"""
Blur Image enpoint api
:author Irfan Andriansyah <irfanandriansyah10@gmail.com>
"""
import os
from app import photos
from string import Template
from PIL import Image, ImageFilter
from flask import Blueprint, request
from app.utils.response import responseAPIHelper

fill_color = '#69acec'  # your background

def landscapeDimensions(size):
    width, height = size

    return width, height



mod = Blueprint('blur', __name__, url_prefix='/blur')

@mod.route('/', methods=['POST'])
def upload_images():
    try:
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            file_url = photos.url(filename)
            image_path = os.path.abspath(os.getcwd()) + '/upload/' + filename
            background = Image.open(image_path)
            im_blur = background.filter(ImageFilter.GaussianBlur(radius=5))
            
            base_filename = os.path.basename(image_path)
            template = Template('blur-image-$base_filename')
            filenameBlur = os.path.abspath(os.getcwd()) + '/upload/' + template.substitute(base_filename=base_filename)

            if im_blur.mode in ('RGBA', 'LA'):
                jpeg_blur = Image.new(im_blur.mode[:-1], im_blur.size, fill_color)
                jpeg_blur.paste(im_blur, im_blur.split()[-1])
                im_blur = jpeg_blur

            im_blur.save(filenameBlur, 'JPEG' )

            return responseAPIHelper({
                'original_image': file_url,
                'blur_image': photos.url(template.substitute(base_filename=base_filename))
            }, True), 200
        else:
            raise ValueError('Error Request')
    except BaseException as e:
        return responseAPIHelper({
            'Error': str(e)
        }, False), 200