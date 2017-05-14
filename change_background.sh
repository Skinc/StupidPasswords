#! /bin/bash

python make_png.py passwords.txt
FILE = "'file://$(readlink -e "image.png" )'"
gsettings set org.gnome.desktop.background picture-uri "$FILE"

