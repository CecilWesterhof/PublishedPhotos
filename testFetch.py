#!/usr/bin/env python3

from utilDecebal import time_fetchURLs


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

time_fetchURLs(server, urls, 75, 10)
