import time
import praw
from config import *

while True: # Loop
    for comment in reddit.redditor(bot_name).comments.new(limit=150):
        print(f"Found comment with {comment.score} karma!")
        if comment.subreddit.name == subreddit_name:
            if comment.score <= -3: # Since the bot is used for multiple subs
                comment.submission.report(f"Warning! Bot comment has reached a score of {comment.score}." \
                    "Please check the post!")
                print("Detected Negative Karma!")
        elif comment.score >= 25:
            comment.edit("What a legendary fight! Thank you so much for letting us know that this post is good." \
                         "\n\n --- \n\n I'm a bot created to make the moderation of this sub easier")
            comment.submission.mod.approve()
            print("Approved submission")
    time.sleep(900)