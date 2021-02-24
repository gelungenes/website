import frontmatter
import datetime
from urllib.parse import urlparse

now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
date = now.strftime("%Y-%m-%d")

with open("content/posts/%s.md" % date) as f:
    post = frontmatter.load(f)

print(f"""
#!/bin/sh
time convert \
    -interline-spacing -20 \
    -border 20 \
    -bordercolor white \
    -background white \
    -fill black \
    -size 760x560 \
    -gravity west \
    -font fonts/bevan.ttf \
    caption:"{post["title"].replace('"','""')}" \
    static/images/{date}.png;
time convert \
    static/images/{date}.png \
    -font fonts/pt-sans.ttf \
    -pointsize 16 \
    -fill black -gravity SouthWest -annotate +43+5 "Gelungenes" \
    -fill grey -gravity SouthWest -annotate +128+5 "Die Kunst des schönen Satzes" \
    -fill grey -gravity SouthEast -annotate +20+5 "{urlparse(post["found_url"]).netloc.lstrip("www.")} @ {post["found_at"]}" \
    static/favicon.ico -gravity SouthWest -geometry +20+8 -composite  \
    static/images/{date}.png
""")
