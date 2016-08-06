from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)  # 因为是在蓝本中的，必须加main，但是由于想让它在全局错误中都能发挥作用，所以用app_errorhandler
def internal_server_error(e):
    return render_template('500.html'), 500


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

