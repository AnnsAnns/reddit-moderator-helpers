from shared import *
import time

def repost():
    for submission in reddit.subreddit('deepfriedmemes').mod.modqueue(only='submissions', limit=None):
        if submission.locked == True or submission.distinguished == True or submission.approved == True:
            continue
        else:
            for comment in submission.comments:
                if comment.author == "RepostSentinel":
                    print("Found " + comment.permalink)
                    if "100%" in comment.body.lower():
                        print("100percent same " + comment.permalink)
                        taken_action()
                        submission_r(submission, "Repost")
                        ban(submission, "Reposting", 7)
                        discord_webhook(submission, "s", "Repost", 7)
                        continue

hook.send("ModQueue Moderation Started!")
while True:
    try: 
        repost()
        time.sleep(90)
    except:
        print("Shit")