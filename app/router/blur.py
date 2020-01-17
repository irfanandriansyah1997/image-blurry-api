"""
Blur Image enpoint api
:author Irfan Andriansyah <irfanandriansyah10@gmail.com>
"""

from flask import Blueprint, request
from app import photos
from app.utils.response import responseAPIHelper


mod = Blueprint('blur', __name__, url_prefix='/blur')

@mod.route('/', methods=['POST'])
def upload_images():
    try:
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            file_url = photos.url(filename)

            return responseAPIHelper({
                'image': file_url
            }, True), 200
        else:
            raise ValueError('Error Request')
    except BaseException as e:
        return responseAPIHelper({
            'Error': str(e)
        }, False), 200