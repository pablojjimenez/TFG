#!/bin/bash

rm -R test_venv
virtualenv --python=/usr/bin/python3 --system-site-packages test_venv
. test_venv/bin/activate

#install dependencies
pip install -r requirements_test.txt
deactivate
