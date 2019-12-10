#!/bin/bash

source /home/alu4240/.virtualenvs/virtual_machine/bin/activate
uwsgi --ini /home/alu4240/webapps/virtual_machine/uwsgi.ini
