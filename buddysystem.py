#!/usr/bin/python3

import os
import click
from flask_migrate import Migrate
from app import create_app
from app import db
from app.models import Role
from app.models import User
# calls for app creation and migrates to db once complete
app = create_app('default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict (db=db, User=User, Role=Role)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
