import frontmatter
import datetime
import random
import glob
import csv

used = set()

for path in glob.glob("content/posts/*.md"):
    with open(path) as f:
        post = frontmatter.load(f)
        used.add(post["title"])

gelungenes = []

with open('data/gelungenes.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         gelungenes.append(row)

possible = [entry for entry in gelungenes if entry["content"] not in used]

selected = random.choice(possible)
print(selected)

now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

with open("content/posts/%s.md" % now.strftime("%Y-%m-%d"), 'w') as file_object:
    file_object.write(frontmatter.dumps(frontmatter.Post("", None, **{
    "title": selected["content"],
    "found_url": selected["source_url"],
    "found_at": selected["visit_date"],
    "date": now.isoformat(),
})))
