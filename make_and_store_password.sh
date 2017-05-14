#! /bin/bash

python make_password.py | tee tempfile.txt
pwString=`cat tempfile.txt | tail -n 1`
rm tempfile.txt
python make_png.py passwords.txt
linkString=`python upload_to_imgur.py`
python pw-maker.py "$pwString" "$linkString"
