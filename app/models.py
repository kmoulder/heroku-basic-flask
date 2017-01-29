from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_id = db.Column(db.String(64), index=True, unique=False)
    subreddit = db.Column(db.String(64), index=True, unique=False)
    title = db.Column(db.String(120), index=True, unique=False)
    url = db.Column(db.String(64), index=True, unique=False)
    num_comment = db.Column(db.String(64), index=True, unique=False)
    permalink = db.Column(db.String(120), index=True, unique=False)
    thumbnail_url = db.Column(db.String(120), index=True, unique=False)
    post_id = db.Column(db.String(64), index=True, unique=False)
    duration = db.Column(db.String(64), index=True, unique=False)
    name = db.Column(db.String(64), index=True, unique=False)
    timeshift = db.Column(db.String(64), index=True, unique=False)
    def __repr__(self):
        return '<Video %r>' % (self.subreddit)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(64), index=True, unique=False)
    user = db.Column(db.String(120), index=True, unique=False)
    comment = db.Column(db.String(1200), index=True, unique=False)
    def __repr__(self):
        return '<Comments %r>' % (self.comment)


class Subreddits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    def __repr__(self):
        return '<Subreddits %r>' % (self.name)
