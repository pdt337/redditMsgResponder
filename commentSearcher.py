import praw
import time
import random

def comments():
    USER_AGENT="Comment responder by /u/badpokerface12 for /u/PM_ME_YOUR_TITS_GIRL" #describes what the bot does 
    USER_NAME=" " #insert user name here
    PASS_WD=" " #insert password here 
    
    reddit=praw.Reddit(USER_AGENT) #creats the bot
    reddit.login(USER_NAME,PASS_WD)
    print reddit.is_logged_in()
    
    checked=set()

    while True:
        print "Geting your inbox"
        messages=reddit.get_inbox()
        for msg in messages:
            if ((name(msg.body)) & (msg.id not in checked)):
                checked.add(msg.id)
                msg.reply(replyPicker())
            if ((msg=="the hero that reddit deserves") & (msg.id not in checked)):
                checked.add(msg.id)
                msg.reply("[Thank You](http://blogs.discovery.com/.a/6a00d8341bf67c53ef0167688d833a970b-800wi)")
            if ((msg=="doing gods work son") & (msg.id not in checked)):
                msg.reply("[Thank You](http://i.imgur.com/vNfRI.jpg)")
                checked.add(msg.id)
            if ((msg=="I don't know what I expected") & (msg.id not in checked)):
                checked.add(msg.id)
                msg.reply("[Well...](http://www.lolbrary.com/content/74/well-said-sloth-43074.jpg)")
            if ((nameM(msg)) & (msg.id not in checked)):
                checked.add(msg.id)
                msg.reply("Anyone who sends moobs, dick pic, or gore is put on my ignore list and banned from the subreddit. A few have, but not many.")
	    if(msg=="Okay."):
		msg.reply("Test Reply")
            else:
                msg.mark_as_unread()
            sleep_time= timePicker()
            print "Going to sleep for {0} seconds".format(sleep_time)
            time.sleep(sleep_time)



def timePicker():
	times=[60,120,30,200,300,250,100,75,175]
        return random.choice(times)


def replyPicker():
    replies=["/r/PM_ME_YOUR_TITS_GIRL is my subreddit. With permission from the sender and age verification, I post their pic here. No permission and verification, no post. Let’s keep this about Rampart people. (More FAQ)",
             "You may check my “link” history to see what I have posted. /r/PM_ME_YOUR_TITS_GIRL is my subreddit. With permission from the sender and age verification, I post their pic here. No permission and verification, no post. (More FAQ)",
             "/r/PM_ME_YOUR_TITS_GIRL is my subreddit. With permission from the sender and age verification, I post their pic here. No permission and verification, no post. Let’s keep this about Rampart people. (More FAQ)",
             "/r/PM_ME_YOUR_TITS_GIRL is my subreddit. With permission from the sender and age verification, I post their pic here. No permission and verification, no post. You can check my “link” history to see what I have posted. (More FAQ)",
             "I do get PM’s of boobies. /r/PM_ME_YOUR_TITS_GIRL is my subreddit. With permission from the sender and age verification, I post their pic here. No permission and verification, no post. (More FAQ)"]
    return random.choice(replies)
	

def nameM(msg):
    notTits=["No manboobs?","Of those few, how many are man-boobs?","Your the one username that probably everybody will remember. Btw has any guy ever pm'd his moobs?","I'll send you a picture of my dick.",
             "how many dick pics do you get?","You said that you probably get about double the pics that you post on your subreddit, but how many dick pics do you get?"]
    return msg in notTits
            


def name(msg):
    questions=["has the username worked?","But your user name. Im curious.... Has it ever worked?","Does anyone pm you tits?","Does anyone ever send you tits?","Does your username actually work?","Does your username ever work?",
               "Does your name ever work?","Does your username work?","Does your username really work?","Does your UN ever work?","Do you get many pictures of tits?","Does that account work. I usually get nothing",
               "does your username ever got you some tits?","....so has that username ever worked for you?","I'm genuinely curious; Has anyone PM'd you their tits?","Has your username worked yet?","Has your username ever worked?",
               "Has your username worked out for you?","has that username ever worked for you?","Has anyone ever PMed you their tits?","The real question is, has anyone ever PM'd you their tits?",
               "How often does your user name work?","So I've been pondering... has your name worked yet?","Just out of curiosity, has anyone ever actually pm'd you their their tits?",
               "Just out of curiosity, have you ever been PM'ed boobs?","Have you ever got any tits pm'd to you?","Have you recieved any PM's of tits?","have people ever obeyed your username?","Does this work?",
               "How many times have you actually been PM'd with a pair of tits?","Off topic, and probably the millionth time you've been asked, are you ever pm'd tits?",
               "Off topic: but does your username work? I am curious...","Have you had any luck in regards to your username? I'd like to know for science.","Unrelated question... Have you actually gotten any pms with tits?",
               "Your username... Has it worked?","You probably get asked this a lot, but does it work?"]
    return msg in questions





def main():
    print "Getting ready to check your inbox for specific comments"
    comments()

main()
