from flask.cli import with_appcontext
import click

from src.ext import db
from src.models.admin import Admin


@click.command('init_db')
@with_appcontext
def init_db():
    db.create_all()
    click.echo('Database initialized')


@click.command('populate_db')
@with_appcontext
def populate_db():

    admin = Admin.query.filter_by(
        name='admin'
    ).first()

    if not admin:
        admin = Admin(
            name='admin',
            password='admin123'
        )
        admin.create()

    click.echo('Admin created')
