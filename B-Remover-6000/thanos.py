import praw
import time
from dhooks import Webhook, Embed

hook = Webhook("WEBHOOK")
reddit = praw.Reddit(Yada yada)
subreddit = reddit.subreddit('deepfriedmemes')

emojis = ["🆔","🅰","🅱","🆎","🆑","🅾","🆘","🆚","🆖","🆗","🅿"]
emoji_use = 671

print("Starting Search!")
for submission in reddit.subreddit('deepfriedmemes').new(limit=100):
    for comment in submission.comments:
        if any(ext in comment.body for ext in emojis) and comment.removed == False and comment.distinguished == None and comment.stickied == False:
            comment.mod.remove() 
            reddit.redditor(str(comment.author)).message('Comment Removed from /r/DeepFriedMemes!', "We have decided to ban the B-emoji and similar [See here: https://old.reddit.com/r/DeepFriedMemes/comments/aj4rvt/the_emoji_is_now_banned/ ] (Comment: https://www.reddit.com" + str(comment.permalink)+ " )")
            emoji_use = emoji_use + 1
            print("Found")
            try:
                embed = Embed(
                description=str(comment.body),
                color=0xff242b
                )
                embed.set_author(name='Comment', icon_url="http://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-11/256/b-button-blood-type.png")
                embed.add_field(name='Number:', value=str(emoji_use))
                embed.add_field(name='Permalink:', value=f"https://reddit.com{str(comment.permalink)}")
                embed.set_footer(text='Prepare for the modmail!', icon_url="https://cdn.discordapp.com/emojis/531057128136507412.png?v=1")
                hook.send(embed=embed)
            except:
                print("OHHHHH SHITTTT")
            time.sleep(0.25)
        else:
            print("Nope")
    if any(ext in submission.title for ext in emojis) and submission.approved == False and submission.removed == False and submission.distinguished == None and submission.approved == False:
        submission.mod.remove() 
        reddit.redditor(str(submission.author)).message('submission Removed from /r/DeepFriedMemes!', "We have decided to ban the B-emoji and similar [See here: https://old.reddit.com/r/DeepFriedMemes/comments/aj4rvt/the_emoji_is_now_banned/ ] (Comment: https://www.reddit.com" + str(submission.permalink)+ " )")
        emoji_use = emoji_use + 1
        print("Found2")
        try:
            embed = Embed(
            description=str(submission.title),
            color=0xfc14ff
            )
            embed.set_author(name='Submission', icon_url="http://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-11/256/b-button-blood-type.png")
            embed.add_field(name='Number:', value=str(emoji_use))
            embed.add_field(name='Permalink:', value=f"https://reddit.com{str(submission.permalink)}")
            embed.set_footer(text='Prepare for the modmail!', icon_url="https://cdn.discordapp.com/emojis/531057128136507412.png?v=1")
            hook.send(embed=embed)
        except:
            print("OHHHHH SHITTTT2")
        time.sleep(0.25)
    else:
        print("Nope2")

            