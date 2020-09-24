#!/bin/bash
if [ -n "$1" ]
    then
        source env/bin/activate;
        youtube-dl -xic --yes-playlist --audio-format mp3 -o "Musicas/%(channel)s/%(title)s.%(ext)s" $1;
    else
        source env/bin/activate;
        python3 interface.py;
fi
