import tweepy
from tweepy import OAuthHandler

consumer_key = 'od25OAmyH1OXYqnRYowGsvfq0'
consumer_secret = 'HQLIUsVuZCyj0r4OtmjlWQEBuWPg2DuNVtBZTcoEFftGCBAewu'
access_token = '713900746874429442-k3q3OUqnisvAQmGxegMRBOITWKfbarz'
access_secret = '34OGl7y2M2lsbzYerGn1TUSoKiceyje39xj65whnqA5gw'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

common_followers=[]
followers1=[]
followers2=[]

name1= str(raw_input("Dwste to screen name tou prwtou xrhsth: @"))
for user in tweepy.Cursor(api.followers, screen_name=name1, count = 200).items():
    followers1.append(user.screen_name)

name2= str(raw_input("Dwste to screen name tou defterou xrhsth: @"))
for user in tweepy.Cursor(api.followers, screen_name=name2, count = 200).items():
    followers2.append(user.screen_name)

common_followers=list(set(followers1).intersection(followers2))
print "Oi koinoi followers einai:\n"
print u', '.join(common_followers)
