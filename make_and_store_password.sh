#! /bin/bash

passwordString=`python make_password.py | tail -n 1`
python make_png.py passwords.txt
linkString=`python upload_to_imgur.py`
python pw-maker.py "$passwordString" "$linkString"
