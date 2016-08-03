from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views   # 只有把其他的包导进来才能将他们跟蓝本关联起来。注：forms不需要关联
