from flask import render_template, redirect, flash, jsonify, request
from app import app, db, models
from app.data import video_pair, get_quota, get_subreddits
from app.comments import get_comments
from datetime import datetime
from .forms import LoginForm

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route('/test')
def index():
    return render_template('index.html')

@app.route('/r/<subreddit>/<idx>', methods=['GET', 'POST'])
def id_render(idx=1, subreddit='videos'):

    form = LoginForm()
    if form.validate_on_submit():
        field = form.openid.data
        return redirect('/r/'+field)


    vids = models.Video.query.filter_by(sub_id=idx, subreddit=subreddit).first()
    try:
        url = vids.url
    except AttributeError:
        video_pair(subreddit, None)
        vids = models.Video.query.filter_by(sub_id=idx, subreddit=subreddit).first()
        url = vids.url
    post_id = vids.post_id
    title = vids.title
    timeshift = vids.timeshift
    if len(title) == 120:
        title = str(title) + "..."
    num_comment = vids.num_comment
    permalink = vids.permalink
    duration = vids.duration
    name = vids.name

    urls = []
    titles = []
    durations = []
    timeshifts = []
    thumb_urls = []
    info = models.Video.query.filter_by(subreddit=subreddit).all()
    count = list(range(int(idx), int(idx)+20))

    for inf in info:
        urls.append(inf.url)
        titles.append(inf.title)
        durations.append(inf.duration)
        timeshifts.append(inf.timeshift)

    for item in count:
        try:
            thumb_id = urls[item]
        except IndexError:
            video_pair(subreddit, name)
            thumb_id = urls[item]
        thumb_link = item+1
        thumb_duration = durations[item]
        thumb_title_full = titles[item]
        thumb_title = thumb_title_full[:60]
        if len(thumb_title) < len(thumb_title_full):
            thumb_title = str(thumb_title) + "..."
        thumb_tup = thumb_id, thumb_link, thumb_title, thumb_duration, thumb_title_full
        thumb_urls.append(thumb_tup)

    top_subreddits = ["videos", "deepintoyoutube", "woahtube", "youtubehaiku", "artisanvideos"]
    if subreddit in top_subreddits:
        top_subreddits.remove(subreddit)

    """popular subreddit thumbs"""

    popular_subs = ["videos", "deepintoyoutube", "youtubehaiku"]
    if subreddit in popular_subs:
        popular_subs.remove(subreddit)
    pop_subs = []

    for sub in popular_subs:
        sub_urls = []
        sub_titles = []
        sub_durations = []
        sub_thumb_urls = []
        sub_info = models.Video.query.filter_by(subreddit=sub).all()
        count = list(range(20))

        for inf in sub_info:
            sub_urls.append(inf.url)
            sub_titles.append(inf.title)
            sub_durations.append(inf.duration)

        for item in count:
            sub_thumb_id = sub_urls[item]
            sub_thumb_link = item+1
            sub_thumb_duration = sub_durations[item]
            sub_thumb_title = sub_titles[item]
            sub_thumb_title = sub_thumb_title[:75]
            if len(sub_thumb_title) == 75:
                sub_thumb_title = str(sub_thumb_title) + "..."
            sub_thumb_tup = sub_thumb_id, sub_thumb_link, sub_thumb_title, sub_thumb_duration
            sub_thumb_urls.append(sub_thumb_tup)
        pop_subs_tuple = sub, sub_thumb_urls
        pop_subs.append(pop_subs_tuple)

    """comments"""

    comments = get_comments(subreddit, post_id)

    subreddit_list = [];
    subreddits = models.Subreddits.query.all();
    for sub in subreddits:
        subreddit_list.append(sub.name)

    return render_template('index.html', subreddit=subreddit, url=url, idx=int(idx), next=int(idx)+1, prev=int(idx)-1, title=title,
                           num_comment=num_comment, permalink=permalink, thumb_urls=thumb_urls, pop_subs=pop_subs,
                           top_subreddits=top_subreddits, comments=comments, duration=duration, form=form, subreddits=subreddit_list, timeshift=timeshift)


@app.route('/topload')
def topload():
    top_subreddits = ["videos", "deepintoyoutube", "woahtube", "youtubehaiku", "artisanvideos", "cringe", "cookingvideos", "documentaries", "asmr"]
    for sub in top_subreddits:
        vids = models.Video.query.filter_by(subreddit=sub).all()
        for v in vids:
            db.session.delete(v)
        db.session.commit()
        video_pair(sub, None)
    return 'done.'
