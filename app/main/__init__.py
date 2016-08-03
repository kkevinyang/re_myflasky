from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors  # 虽然不符合PE8 但是必须放在尾部
