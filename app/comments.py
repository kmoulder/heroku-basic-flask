from app import app, db, models
import requests
import json
import re
from html.parser import HTMLParser

def get_comments(subreddit, post_id):

    comments = []
    parser = HTMLParser()

    r = requests.get('https://www.reddit.com/r/' + subreddit + '/comments/' + post_id + '.json', headers={'User-agent': 'web:video-agg-test:1.0 by /u/ZforZardoz'})
    theJSON = json.loads(r.text)
    Children = theJSON[1]["data"]["children"]

    for number in list(range(0, len(Children)-1)):

        user_name = Children[number]["data"]["author"]

        user_comment = Children[number]["data"]["body_html"]
        user_comment = parser.unescape(user_comment)

        replies = []
        reply_1 = []

        replies_data = Children[number]["data"]["replies"]

        # This loop parses and displays the comments

        # if there is reply data
        if "data" in replies_data:
            # for each item in the reply data
            for item in replies_data["data"]["children"]:
                # clear reply_2
                reply_2 = []
                # clear reply_3
                reply_3 = []
                # clear reply_4
                reply_4 = []
                # grab the first reply item's data
                first_reply_data = item["data"]

                # if there's an actual reply in the data
                if "body_html" in first_reply_data:
                    # grab the first-level reply (first_reply)
                    body = first_reply_data["body_html"]
                    first_reply = parser.unescape(body)
                    # add the first-level reply to initial replies list
                    reply_1.append(first_reply)
                    # store the user of first-level reply
                    user_1 = first_reply_data["author"]

                    # if there is reply data for the first reply
                    if "data" in first_reply_data["replies"]:
                        # for each item in the first reply's data
                        for item_2 in first_reply_data["replies"]["data"]["children"]:
                            # clear reply_2
                            reply_2 = []
                            # grab the second reply item's data
                            second_reply_data = item_2["data"]

                            # if there's an actual reply to the first reply data
                            if "body_html" in second_reply_data:
                                # grab the second-level reply (second_reply)
                                body_2 = second_reply_data["body_html"]
                                second_reply = parser.unescape(body_2), second_reply_data["author"]
                                # add the second-level reply to secondary replies list
                                reply_2.append(second_reply)

                                # if there is reply data for the second reply
                                if "data" in second_reply_data["replies"]:
                                    # for each item in the second reply's data
                                    for item_3 in second_reply_data["replies"]["data"]["children"]:
                                        # clear reply_3
                                        reply_3 = []
                                        # grab the second reply item's data
                                        third_reply_data = item_3["data"]

                                        # if there's an actual reply to the second reply data
                                        if "body_html" in third_reply_data:
                                            # grab the third-level reply (third_reply)
                                            body_3 = third_reply_data["body_html"]
                                            third_reply = parser.unescape(body_3), third_reply_data["author"]
                                            # add the third-level reply to tertiary replies list
                                            reply_3.append(third_reply)

                                            # if there is reply data for the third reply
                                            if "data" in third_reply_data["replies"]:
                                                # for each item in the third reply's data
                                                for item_4 in third_reply_data["replies"]["data"]["children"]:
                                                    # grab the second reply item's data
                                                    fourth_reply_data = item_4["data"]

                                                    # if there's an actual reply to the second reply data
                                                    if "body_html" in fourth_reply_data:
                                                        # grab the fourth-level reply (third_reply)
                                                        body_4 = fourth_reply_data["body_html"]
                                                        # check if there are more comments in the thread
                                                        if "data" in fourth_reply_data["replies"]:
                                                            comment_id = fourth_reply_data["id"]
                                                        else:
                                                            comment_id = 0
                                                        fourth_reply = parser.unescape(body_4), fourth_reply_data["author"], comment_id
                                                        # add the third-level reply to tertiary replies list
                                                        reply_4.append(fourth_reply)

                    reply_list = [first_reply, user_1, reply_2, reply_3, reply_4]

                    replies.append(reply_list)

        comment_list = [user_comment, user_name, replies]
        comments.append(comment_list)

    return comments

"""
    for user, comment in zip(users, comments):
        u = models.Comments(user=user, comment=comment, post_id=post_id)
        db.session.add(u)
    db.session.commit()
"""
