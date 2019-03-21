# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: commands.py
# @Date:   2019-03-15 18:29:36
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-21 10:51:46
import click

from app import app, db
from .models import User, Weidian


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

