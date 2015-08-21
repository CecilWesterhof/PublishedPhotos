#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('links.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE links (
             ID          integer PRIMARY KEY AUTOINCREMENT,
             year        integer,
             month       integer,
             description text,
             URL         text
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
              ]
c.executemany('INSERT INTO links (year, month, description, URL) VALUES (2015, 8, ?, ?)', links)
conn.commit()
conn.close()
