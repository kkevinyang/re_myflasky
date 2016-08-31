# -*- coding: utf-8 -*
from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

#检查用户权限


def permission_required(permission):
    def decorator(f):
        @wraps(f)  # 消除装饰的副作用，能保留原有函数的名称和docstring
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)