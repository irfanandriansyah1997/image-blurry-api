"""
Blur Image enpoint api
:author Irfan Andriansyah <irfanandriansyah10@gmail.com>
"""

from flask import Blueprint
from app.utils.response import responseAPIHelper


mod = Blueprint('blur', __name__, url_prefix='/blur')

@mod.route('/', methods=['GET'])
def upload_images():
    try:
        return responseAPIHelper({
            'hello': 'world'
        }, True), 200
    except BaseException as e:
        return responseAPIHelper({
            'Error': str(e)
        }, False), 200