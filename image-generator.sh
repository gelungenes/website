time convert \
    -interline-spacing -20 \
    -border 20 \
    -bordercolor white \
    -background white \
    -fill black \
    -size 760x560 \
    -gravity west \
    -font fonts/bevan.ttf \
    caption:"Man(n) gerät immer wieder in Situationen, wo es auf zuverlässigen Halt ankommt." \
    static/images/2021-02-19.png;
time convert \
    static/images/2021-02-19.png \
    -font fonts/pt-sans.ttf \
    -pointsize 16 \
    -fill black -gravity SouthWest -annotate +43+5 "Gelungenes" \
    -fill grey -gravity SouthWest -annotate +128+5 "Die Kunst des schönen Satzes" \
    -fill grey -gravity SouthEast -annotate +20+5 "gard.de @ 2014-12-09" \
    static/favicon.ico -gravity SouthWest -geometry +20+8 -composite  \
    static/images/2021-02-19.png
