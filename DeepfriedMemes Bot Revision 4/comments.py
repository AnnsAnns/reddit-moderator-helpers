from shared import *

def com_mod():
    for comment in subreddit.stream.comments():
        if any(ext in comment.body for ext in emojis) and comment.removed == False and comment.distinguished == None and comment.stickied == False: 
            comment_letters = len(comment.body) - comment.body.count(" ")
            comment_bad = 0

            for c in comment.body:
                if c in emojis:
                    comment_bad = comment_bad + 1
                    print("yes")

            print(str(comment_letters))
            print(str(comment_bad))
            print(str(comment_bad * (100 / comment_letters)))

            if comment_bad * (100 / comment_letters) < 20:
                continue

            comment.mod.remove() 
            reddit.redditor(str(comment.author)).message('Comment Removed from /r/DeepFriedMemes!', "We have decided to ban the B-emoji and similar [See here: https://old.reddit.com/r/DeepFriedMemes/comments/ajszxq/a_revision_on_banning/ ] (Comment: https://www.reddit.com" + str(comment.permalink)+ " )")
            taken_action()
            print("Deleted6")
            discord_webhook(comment, "c", "B-Emoji Comment", 0)
            continue

hook.send("Comments Moderation Started!")

while True:
    try:
        com_mod()
    except:
        print("Sad Hours!")

