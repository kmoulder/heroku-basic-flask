from app import app, db, models
from app.comments import get_comments
from app.video_duration import get_duration
import requests
import json
import urllib.request
import re

def videos(url):
    if '&t=' in url:
        try:
            timeshift = int(url.split('&t=')[1])
        except ValueError:
            timeshift = int(0)
    elif '?t=' in url:
        try:
            timeshift = int(url.split('?t=')[1])
        except ValueError:
            timeshift = int(0)
    else:
        timeshift = int(0)
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')



    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:

        return youtube_regex_match.group(6), timeshift



    return youtube_regex_match


def vid_info(subreddit, last_name):

    count = 4
    quota = 0
    sub_id = 1

    sub_ids = []
    ids = []
    post_ids = []
    titles = []
    num_comments = []
    permalinks = []
    thumbnail_urls = []
    durations = []
    names = []
    timeshifts = []


    sub = str(subreddit)

    while True:

        r = requests.get('https://www.reddit.com/r/' + sub + '/.json?after=' + str(last_name), headers={'User-agent': 'web:video-agg-test:1.0 by /u/ZforZardoz'})
        theJSON = json.loads(r.text)
        Children = theJSON["data"]["children"]

        for post in Children:
            if videos(post["data"]["url"]) != None:
                regex_data = videos(post["data"]["url"])
                id = regex_data[0]
                timeshift = regex_data[1]
                ids.append(id)
                titles.append(post["data"]["title"])
                post_ids.append(post["data"]["id"])
                num_comments.append(post["data"]["num_comments"])
                permalinks.append(post["data"]["permalink"])
                thumbnail_urls.append(post["data"]["thumbnail"])
                last_name = post["data"]["name"]
                names.append(last_name)
                timeshifts.append(timeshift)
                sub_ids.append(str(sub_id))
                sub_id += 1
                quota += 1

                """get video duration"""

                video_id = id
                duration = get_duration(video_id)
                durations.append(duration)

                "end video duration"

            else:
                last_name = post["data"]["name"]
                continue

        if count < 1 and quota > 15:
            break
        elif count < -100:
            break

        count -= 1

    return ids, titles, num_comments, permalinks, thumbnail_urls, sub_ids, quota, post_ids, durations, names, timeshifts


def get_quota(subreddit):
    ids, titles, num_comments, permalinks, thumbnail_urls, sub_ids, quota, post_ids, durations, names, timeshifts = vid_info(subreddit, None)
    return quota


def video_pair(subreddit, last_name):
    ids, titles, num_comments, permalinks, thumbnail_urls, sub_ids, quota, post_ids, durations, names, timeshifts = vid_info(subreddit, last_name)
    for idr, title, num_comment, permalink, thumbnail_url, sub_id, post_id, duration, name, timeshift in zip(ids, titles, num_comments, permalinks, thumbnail_urls, sub_ids, post_ids, durations, names, timeshifts):
        u = models.Video(title=title, url=idr, num_comment=num_comment, permalink=permalink,
                         thumbnail_url=thumbnail_url, subreddit=subreddit, sub_id=sub_id, post_id=post_id,
                         duration=duration, name=name, timeshift=timeshift)
        db.session.add(u)
    db.session.commit()


def get_subreddits(last_name):

    count = 1
    quota = 0

    subs = []

    while True:

        r = requests.get('https://www.reddit.com/reddits/.json?after=' + str(last_name), headers={'User-agent': 'web:video-agg-test:1.0 by /u/ZforZardoz'})
        theJSON = json.loads(r.text)
        Children = theJSON["data"]["children"]

        for post in Children:
            subs.append(post["data"]["display_name"])
            print(str(post["data"]["display_name"]))
            quota += 1


            last_name = post["data"]["name"]
            continue

        if count < 1 and quota > 100:
            break
        elif count < -100:
            break

        count -= 1

    for item in subs:
        u = models.Subreddits(name=item)
        db.session.add(u)
        db.session.commit()
