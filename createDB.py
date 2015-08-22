#!/usr/bin/env python3

import os
import sqlite3
import sys


os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
conn = sqlite3.connect('links.sqlite')
c = conn.cursor()
tables = c.execute('''SELECT name
                      FROM sqlite_master
                      WHERE type = 'table' AND name = 'links'
                   ''').fetchall()
if len(tables) == 0:
    c.execute('''CREATE TABLE links (
                 ID          integer PRIMARY KEY AUTOINCREMENT,
                 year        integer NOT NULL,
                 month       integer NOT NULL,
                 description text    NOT NULL,
                 URL         text    NOT NULL UNIQUE
                 )''')
links = [
    ('Album',            'https://plus.google.com/collection/MuwPX'),
    ('Heron Sunbathing', 'https://plus.google.com/+CecilWesterhof/posts/bHvSzBGobEj'),
    ('Heron Fishing',    'https://plus.google.com/+CecilWesterhof/posts/TY3asc5oCnB'),
    ('Water Lily',       'https://plus.google.com/+CecilWesterhof/posts/AtTwhL8SdnH'),
    ('Tree at Pond',     'https://plus.google.com/+CecilWesterhof/posts/TyiZbUWdnrm'),
    ('Fish',             'https://plus.google.com/+CecilWesterhof/posts/MoQ7vXs8HqP'),
    ('Fountain',         'https://plus.google.com/+CecilWesterhof/posts/BDYkPKSMUwZ'),
    ('Digitalis',        'https://plus.google.com/+CecilWesterhof/posts/ed3ZGNzb8kM'),
    ('Sunset',           'https://plus.google.com/+CecilWesterhof/posts/DPbHHSFXBY4'),
    ('Digitalis 2',      'https://plus.google.com/+CecilWesterhof/posts/ZZtSUwNb6RC'),
    ('Water Lilies',     'https://plus.google.com/+CecilWesterhof/posts/LY62DqLEJhG'),
    ('Flower',           'https://plus.google.com/+CecilWesterhof/posts/XFKyTcoakcy'),
    ('Waterfalls',       'https://plus.google.com/+CecilWesterhof/posts/bfg5irDAn2T'),
    ('Frogs',            'https://plus.google.com/+CecilWesterhof/posts/jKr5B6EQyo1'),
    ('Flowers',          'https://plus.google.com/+CecilWesterhof/posts/iPQbBrTbcnm'),
    ('Sheep',            'https://plus.google.com/+CecilWesterhof/posts/3a2mBo7om4H'),
    ('Beetle',           'https://plus.google.com/+CecilWesterhof/posts/KnNtis2Gqxf'),
    ('Dove',             'https://plus.google.com/+CecilWesterhof/posts/XA5RcC2Cxbv'),
    ('City Walk',        'https://plus.google.com/+CecilWesterhof/posts/R9me9AKQC6n'),
    ('Boar',             'https://plus.google.com/+CecilWesterhof/posts/9bfpBiQPYen'),
    ('Bird',             'https://plus.google.com/+CecilWesterhof/posts/X6gFE3oxXLY'),
    ('Goose',            'https://plus.google.com/+CecilWesterhof/posts/H4w6JvnQkcU'),
    ('On mothers wings', 'https://plus.google.com/+CecilWesterhof/posts/PY4Nm1TASvx'),
    ('Flowers',          'https://plus.google.com/+CecilWesterhof/posts/9o1i2NgoSfV'),
    ('Trees',            'https://plus.google.com/+CecilWesterhof/posts/ATXhirU6wGd'),
    ('The heron again',  'https://plus.google.com/+CecilWesterhof/posts/9jP4ypcH2L4'),
]
for link in links:
    urls = c.execute('SELECT URL FROM LINKS WHERE URL = ?', [link[1]]).fetchall()
    if len(urls) == 0:
        print('Adding {0}'.format(link))
        c.execute('''INSERT INTO links
                     (year, month, description, URL)
                     VALUES
                     (2015, 8, ?, ?)
                  ''',
                  link)
conn.commit()
conn.close()
