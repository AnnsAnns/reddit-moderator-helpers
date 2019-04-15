from shared import *

def sub_mod():
    for submission in subreddit.stream.submissions():
        # B Emoji
        if any(ext in submission.title for ext in emojis) and not submission.approved:
            taken_action()
            submission_r(submission, "B")
            discord_webhook(submission, "s", "B-Emoji Submission", 0)
            continue
        
        for upvote_question in upvote_removal:
            if upvote_question in submission.title.lower():
                taken_action()
                submission_r(submission_r, "Shitpost")
                discord_webhook(submission, "s", "Upvote Meme", 0)
                continue
        
        for sleep in sleeping_mods:
            if sleep in submission.title.lower():
                taken_action()
                submission_r(submission, "Shitpost")
                ban(submission, "Shitpost", 3)
                discord_webhook(submission, "s", "Mods Sleeping", 3)
            continue

        for upquestion in upvote_asking:
            if upquestion in submission.title.lower():
                taken_action()
                submission.report("Possible Up-/Downvote Meme")
                submission.hide()
                discord_webhook(submission, "s", "Possible Up-/Downvote Meme", 0)
                continue
        # Other

hook.send("Submission Moderation Started!")
while True:
    try:
        sub_mod()
    except:
        print("Sub Failed!")