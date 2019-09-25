import time
import dhooks
import praw
from config import *

while True: # Loop
    for comment in reddit.redditor(bot_name).comments.new(limit=150):
        print(f"Found comment with {comment.score} karma!"\
            f"|{'T' if comment.submission.approved else 'F'} | {comment.permalink}")
        if comment.subreddit == subreddit and not comment.submission.approved and not comment.submission.removed and not comment.submission.hidden: #  Since the bot is used for multiple subs
            if comment.score <= -3:
                comment.submission.report(f"Warning! Bot comment has reached a score of {comment.score}." \
                    "Please check the post!")
                print("Detected Negative Karma!")
                comment.submission.hide()
                discord_reported.send(f"Reported submission: https://reddit.com{comment.submission.permalink} | Comment score: {comment.score}")
            elif comment.score >= 25:
                comment.edit("What a legendary fight! Thank you so much for letting us know that this post is good." \
                            "\n\n --- \n\n I'm a bot created to make the moderation of this sub easier")
                comment.submission.mod.approve()
                comment.submission.hide()
                discord_approved.send(f"Approved submissions: https://reddit.com{comment.submission.permalink} | Comment score: {comment.score}")
    time.sleep(900)