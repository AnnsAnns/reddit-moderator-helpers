from config import *
import praw

sub = reddit.subreddit("srotd_archives")
srotd = reddit.subreddit("subredditoftheday")

for submission in srotd.stream.submissions():
    if submission.created_utc > 1548594000:
        sub.submit(title=submission.title, selftext=submission.selftext).reply("https://reddit.com" + submission.permalink)
        