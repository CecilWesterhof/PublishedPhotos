#!/usr/bin/env python3

import bottle
import json
import os
import sqlite3
import sys

from bottle     import get, route, static_file
from contextlib import contextmanager
from platform   import python_version


@contextmanager
def open_db():
    db = sqlite3.connect('links.sqlite')
    cs = db.cursor()
    try:
        yield cs
    finally:
        db.close()

def read_links():
    with open_db() as cs:
        return cs.execute('SELECT description, url FROM links;').fetchall()

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root = 'static')

@route('/')
def main_page():
    return static_file('index.html', root = 'static')

@route('/links/data')
def links_as_json():
    bottle.response.content_type = 'application/json'
    return json.dumps([
        { 'desc': desc, 'url': url }
        for desc, url in read_links()], indent = 4)

@route('/versionPython')
def versionPython():
    bottle.response.content_type = 'text/plain'
    return python_version()

@route('/versionSQLite')
def versionSQLite():
    bottle.response.content_type = 'text/plain'
    return sqlite3.sqlite_version


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    bottle.run(host = 'localhost', port = 8080)
