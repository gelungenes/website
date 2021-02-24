import frontmatter
from twitter import *
import datetime
import os

auth = OAuth(
    os.environ["TWITTER_AUTH_TOKEN"],
    os.environ["TWITTER_AUTH_SECRET"],
    os.environ["TWITTER_CONSUMER_KEY"],
    os.environ["TWITTER_CONSUMER_SECRET"]
)
twitter = Twitter(auth=auth)
twitter_upload = Twitter(domain='upload.twitter.com', auth=auth)

date = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).strftime("%Y-%m-%d")

with open("content/posts/%s.md" % date) as f:
    post = frontmatter.load(f)

with open("static/images/%s.png" % date, "rb") as imagefile:
    imagedata = imagefile.read()

image = twitter_upload.media.upload(media=imagedata)
twitter_upload.media.metadata.create(media_id=image["media_id_string"], text=post["title"])

post = twitter.statuses.update(
    status="#gelungenes: \"%s\" (%s) auf https://gelungen.es/%s" % (post["title"], post["found_url"], date),
    media_ids=image["media_id_string"]
)
print("tweeted https://twitter.com/gelungenes/status/%s" % post["id_str"])
