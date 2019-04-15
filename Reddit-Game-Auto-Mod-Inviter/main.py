import praw

reddit = you know what you should put here

# This is dirty code, if you see this - Dont share or you will ruin my rep lol

def normallevels():
    global naam
    x = 1 # Starting level
    naam = "Timmymac1000" # User

    while x != 36: # Ugly I know, 2lazy2change - This has to be 1 level of the target level!
        if x == 6:
            try:
                reddit.subreddit("gameievei6").moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        elif x == 14:
            try:
                reddit.subreddit("gamelevel0").moderator.invite(naam)
                reddit.subreddit("gamelevel14").moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        elif x == 15:
            try:
                reddit.subreddit("gamelevel1").moderator.invite(naam)
                reddit.subreddit("gamelevel15").moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        elif x == 19:
            try:
                reddit.subreddit("gamelevel6").moderator.invite(naam)
                reddit.subreddit("gamelevel19").moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        elif x == 22:
            try:
                reddit.subreddit("gamelavel22").moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        elif x == 27:
            try:
                reddit.subreddit("gamelevel27").moderator.invite(naam)
                reddit.subreddit("gameleveltwentyseven").moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        elif x == 31:
            try:
                reddit.subreddit("gamelevelXXXI").moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        elif x == 1:
            try:
                reddit.subreddit("game").moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        else:
            try:
                reddit.subreddit("gamelevel" + str(x)).moderator.invite(naam)
            except:
                print("Failed at level " + str(x))
        x = x + 1

def speciallevels():
    naam = "Wizarduss" # Username
    reddit.subreddit("gamelevelgamma").moderator.invite(naam)
    reddit.subreddit("gamelevelalpha").moderator.invite(naam)
    reddit.subreddit("gamelevelbeta").moderator.invite(naam)

normallevels()