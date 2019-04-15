import discord
import praw
import time

client = discord.Client()
reddit = praw.Reddit("You know what you should normally put here")

subreddit = reddit.subreddit('Your Subreddit Without /R/')
distoken = "Your Discord Token"

# These must all be Voice Channels

subchannel = 1 #int of channel id for submissions
modmailchannel = 1 #int of channel id for modmail
unmoderatedchannel = 1 #int of channel id for unmoderated 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        c = 0
        for l in reddit.subreddit('deepfriedmemes').mod.modqueue(only='submissions', limit=None):
            c = c + 1
            print("Yes")
        print("Editing Channel")
        await client.get_channel(566707426972270628).edit(name=f"Mod-Queue: {str(c)}")
        c = 0
        print("Searching Modmail")

        for m in reddit.subreddit("deepfriedmemes").modmail.conversations():
            c = c + 1
            print("Yes M")
        print("Editing M Channel")
        await client.get_channel(566717121606844594).edit(name=f"Mod-Mail: {str(c)}")
        print("Finished")

        c = 0
        print("Searching U")

        for m in reddit.subreddit("deepfriedmemes").mod.unmoderated(limit=None):
            c = c + 1
            print("Yes U")
        print("Editing U Channel")
        await client.get_channel(566723802822868993).edit(name=f"Unmoderated: {str(c)}")
        print("Finished")
        await asyncio.sleep(300)

client.run(distoken)
