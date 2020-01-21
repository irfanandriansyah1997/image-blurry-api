"""
Blur Image enpoint api
:author Irfan Andriansyah <irfanandriansyah10@gmail.com>
"""
import os
from app import photos
from flask import Blueprint, request
from app.utils.response import responseAPIHelper
from app.modules.blur_modules import BlurModules


mod = Blueprint('blur', __name__, url_prefix='/blur')

@mod.route('/', methods=['POST'])
def upload_images():
    try:
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            file_url = photos.url(filename)
            blur_images = BlurModules(
                filename,
                int(request.form.get('radius'))
            ).run()

            return responseAPIHelper({
                'original_image': file_url,
                'blur_image': photos.url(blur_images)
            }, True), 200
        else:
            raise ValueError('Error Request')
    except BaseException as e:
        print(e)
        return responseAPIHelper({
            'Error': str(e)
        }, False), 200