#!/usr/bin/env python3

import time

from urllib.request import urlopen


server = 'http://localhost:8080'
urls   = [
    '/',
    '/static/css/default.css',
    '/static/JavaScript/angular.js',
    '/static/appPublishedPhotos.js',
    '/links/data',
    '/versionPython',
    '/versionSQLite',
]
for x in range(0, 75):
    start_time = time.time()
    for url in urls:
        urlopen(server + url).read()
    end_time = time.time()
    print('It took {0} seconds'.format(end_time - start_time), flush = True)
    time.sleep(10)
