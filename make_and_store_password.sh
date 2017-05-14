#! /bin/bash

python make_password.py
python make_png.py passwords.txt
python upload_to_imgur.py
