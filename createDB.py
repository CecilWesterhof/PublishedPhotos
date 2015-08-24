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
    ('Album',                 'https://plus.google.com/collection/MuwPX'),
    ('Heron Sunbathing',      'https://plus.google.com/+CecilWesterhof/posts/bHvSzBGobEj'),
    ('Heron Fishing',         'https://plus.google.com/+CecilWesterhof/posts/TY3asc5oCnB'),
    ('Water Lily',            'https://plus.google.com/+CecilWesterhof/posts/AtTwhL8SdnH'),
    ('Tree at Pond',          'https://plus.google.com/+CecilWesterhof/posts/TyiZbUWdnrm'),
    ('Fish',                  'https://plus.google.com/+CecilWesterhof/posts/MoQ7vXs8HqP'),
    ('Fountain',              'https://plus.google.com/+CecilWesterhof/posts/BDYkPKSMUwZ'),
    ('Digitalis',             'https://plus.google.com/+CecilWesterhof/posts/ed3ZGNzb8kM'),
    ('Sunset',                'https://plus.google.com/+CecilWesterhof/posts/DPbHHSFXBY4'),
    ('Digitalis 2',           'https://plus.google.com/+CecilWesterhof/posts/ZZtSUwNb6RC'),
    ('Water Lilies',          'https://plus.google.com/+CecilWesterhof/posts/LY62DqLEJhG'),
    ('Flower',                'https://plus.google.com/+CecilWesterhof/posts/XFKyTcoakcy'),
    ('Waterfalls',            'https://plus.google.com/+CecilWesterhof/posts/bfg5irDAn2T'),
    ('Frogs',                 'https://plus.google.com/+CecilWesterhof/posts/jKr5B6EQyo1'),
    ('Flowers',               'https://plus.google.com/+CecilWesterhof/posts/iPQbBrTbcnm'),
    ('Sheep',                 'https://plus.google.com/+CecilWesterhof/posts/3a2mBo7om4H'),
    ('Beetle',                'https://plus.google.com/+CecilWesterhof/posts/KnNtis2Gqxf'),
    ('Dove',                  'https://plus.google.com/+CecilWesterhof/posts/XA5RcC2Cxbv'),
    ('City Walk',             'https://plus.google.com/+CecilWesterhof/posts/R9me9AKQC6n'),
    ('Boar',                  'https://plus.google.com/+CecilWesterhof/posts/9bfpBiQPYen'),
    ('Bird',                  'https://plus.google.com/+CecilWesterhof/posts/X6gFE3oxXLY'),
    ('Goose',                 'https://plus.google.com/+CecilWesterhof/posts/H4w6JvnQkcU'),
    ('On Mothers Wings',      'https://plus.google.com/+CecilWesterhof/posts/PY4Nm1TASvx'),
    ('Flowers',               'https://plus.google.com/+CecilWesterhof/posts/9o1i2NgoSfV'),
    ('Trees',                 'https://plus.google.com/+CecilWesterhof/posts/ATXhirU6wGd'),
    ('The Heron Again',       'https://plus.google.com/+CecilWesterhof/posts/9jP4ypcH2L4'),
    ('Bicycle Ride',          'https://plus.google.com/+CecilWesterhof/posts/agjezPNjoht'),
    ('Water Lilies 2',        'https://plus.google.com/+CecilWesterhof/posts/hkE9KRv59BF'),
    ('I Took a Bicycle Ride', 'https://plus.google.com/+CecilWesterhof/posts/agjezPNjoht'),
    ('Water Lilies 2',        'https://plus.google.com/+CecilWesterhof/posts/hkE9KRv59BF'),
    ('Cows',                  'https://plus.google.com/+CecilWesterhof/posts/j6oPfiVjtiz'),
]
select_url = '''SELECT year
                ,      month
                ,      description
                FROM   LINKS
                WHERE  URL = ?'''
year    = 2015
month   = 8
for link in links:
    description = link[0]
    url         = link[1]
    url_values  = c.execute(select_url, [url]).fetchall()
    if len(url_values) == 0:
        print('Adding {0}'.format(link))
        c.execute('''INSERT INTO links
                     (year, month, description, URL)
                     VALUES
                     (?, ?, ?, ?)
                  ''',
                  [year, month, description, url])
    else:
        to_insert   = (year, month, description)
        found       = url_values[0]
        if found != to_insert:
            print('For {0} found {1} instead of {2}'.format(url, found, to_insert))
conn.commit()
conn.close()
