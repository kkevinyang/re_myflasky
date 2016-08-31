# -*- coding: utf-8 -*
from flask import Blueprint
from ..models import Permission


main = Blueprint('main', __name__)


@main.app_context_processor  # 把permission类加入模板
def inject_permissions():
    return dict(Permission=Permission)

from . import views, errors  # 虽然不符合PE8 但是必须放在尾部
