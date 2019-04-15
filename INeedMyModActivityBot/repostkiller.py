import praw
import time

reddit = praw.Reddit(#LALLALAA)

subreddit = reddit.subreddit('deepfriedmemes')

x = "- **Rule 5**: Reposts will be removed at the moderators discretion, this includes but is not limited to reposts with the same title as previous submissions. We allow some images to recirculate if a period of time has passed, or if it previously did not receive much attention. If your post is part of a cluster of submissions of the same image it will be removed."

while True:
    for submission in reddit.subreddit('Bossfight').mod.modqueue(only='submissions', limit=None):
        if submission.locked == True or submission.distinguished == True or submission.approved == True:
            continue
        else:
            for comment in submission.comments:
                if comment.author == "RepostSentinel":
                    print("Found" + comment.permalink)
                    if "100%" in comment.body.lower():
                        print("100percent same " + comment.permalink)
                        submission.reply("Hello /u/" + str(submission.author) + ", thanks for posting to /r/Bossfight. Unfortunately your post has been removed for the following reason(s): \n \n"
                                        + str(x) + "\n \n *If you feel that your post was removed in error or are unsure about why this post was removed then please contact us through [modmail](https://www.reddit.com/message/compose?to=%\2Fr%\2Bossfight).*").mod.distinguish(how="yes", sticky=True)
                        submission.mod.lock()
                        submission.mod.remove()
                        print("**Repost** - Automatically removed https://www.reddit.com" + str(submission.permalink))
    print("Sleeping")
    time.sleep(900)