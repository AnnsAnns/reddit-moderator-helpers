import time
import praw
from config import *

while True: # Loop
    for comment in reddit.redditor(bot_name).comments.new(limit=150):
        if comment.subreddit.name == subreddit_name and comment.score <= -3: # Since the bot is used for multiple subs
            comment.submission.report(f"Warning! Bot comment has reached a score of {comment.score}." \
                "Please check the post!")
            print("Detected Negative Karma!")
    time.sleep(900)