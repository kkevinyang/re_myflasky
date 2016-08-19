#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import create_app, db
from app.models import User, Role, Permission, Post, Comment
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from flask import current_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=current_app, db=db, User=User, Role=Role, Permission=Permission, Post=Post, Comment=Comment)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""  # 启动单元测试
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
