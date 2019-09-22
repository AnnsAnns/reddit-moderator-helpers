import praw
from config import *

for submission in subreddit.stream.submissions(): # Live Feed
    SKIP = False
    if submission.approved or submission.distinguished or submission.locked or submission.stickied:
        continue # Skip
    
    #Check through comments for important infos
    for comment in submission.comments:
        if comment.author == "r_tomBOT" or comment.stickied:
            SKIP = True
            break
    
    if SKIP:
        continue # Skip
    
    submission.reply(reply_message).mod.distinguish(how="yes", sticky=True)
    print("Added note to submission")
