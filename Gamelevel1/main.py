import praw
import random
import time
from discord_webhook.webhook import DiscordWebhook

reddit = praw.Reddit("Fill it yourself ;P")

subreddit = reddit.subreddit('game')

def redditisgay():
    for submission in reddit.subreddit('game').new(limit=100):
        if submission.approved == False:
            normalized_title = submission.title.lower()
            if submission.subreddit == "game":
                if "i\'m" in normalized_title and "and i" in normalized_title or "i\'m" in normalized_title and "and my" in normalized_title or "im" in normalized_title and "and my" in normalized_title or "im" in normalized_title and "and i" in normalized_title:
                    reddit.subreddit('gamelevel2').contributor.add(submission.author)
                    submission.mod.approve()
                    authorgame = "Added " + str(submission.author) + " to level 2!"
                    try:
                        DiscordWebhook(url='your link', content=authorgame).execute()
                    except:
                        pass
                    submission.hide()
                else:
                    submission.report("I couldn't detect what this post is about")
                    submission.hide()

while True:
    redditisgay()
    print("I sleep")
    time.sleep(300)