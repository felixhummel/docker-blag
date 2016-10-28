#!/usr/bin/env python
# vim: set fileencoding=utf-8 filetype=python :
"""Live reloader for docs"""
import glob2
from livereload import Server

import conf  # from sphinx

server = Server()


def watch(filepath):
    server.watch(filepath, 'make html')


watch('conf.py')
# TODO: watch('_static/default.css') and tell sphinx to update default.css
# include all source files
for filepath in glob2.glob('**/*{0}'.format(conf.source_suffix)):
    watch(filepath)

import socket
guessed_ip = socket.gethostbyname(socket.gethostname())

server.serve(root='_build/html', host=guessed_ip)
