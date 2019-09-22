import praw

reddit = praw.Reddit(user_agent="BOSSFIGHT BOT v1",
                     client_id="CLIENT_ID", client_secret="CLIENT_SECRET",
                     username="USERNAME", password="PASSWORD") # You know what to put here

subreddit_name = "Bossfight"
subreddit = reddit.subreddit(subreddit_name)

reply_message = "Is this bossfight epic and fit to the sub? If so, please upvote this comment! \n\n"\
                "I'm a bot created to make moderation easier :)"

bot_name = "r_tomBOT"