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
    xtime = time.time() - 300
    print('We have logged in as {0.user}'.format(client))

    while True:
        if time.time() >= (xtime + 300):
            c = 0
            xtime = time.time()
            for l in subreddit.mod.modqueue(only='submissions', limit=None):
                c = c + 1 # Len doesn't work with ListingGenerators apperently so just fuck it and count like the good old days kek
                print("Yes")
            print("Editing Channel")
            await client.get_channel(subchannel).edit(name=f"Mod-Queue: {str(c)}")
            c = 0
            print("Searching Modmail")

            for m in subreddit.modmail.conversations(): # Has no limit
                c = c + 1
                print("Yes M")
            print("Editing M Channel")
            await client.get_channel(modmailchannel).edit(name=f"Mod-Mail: {str(c)}")
            print("Finished")

            c = 0
            print("Searching U")

            for m in subreddit.mod.unmoderated(limit=None):
                c = c + 1
                print("Yes U")
            print("Editing U Channel")
            await client.get_channel(unmoderatedchannel).edit(name=f"Unmoderated: {str(c)}")
            print("Finished")

client.run(distoken)