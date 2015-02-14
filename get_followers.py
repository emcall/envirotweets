"""
An edit to the lovely program to utilize Tweepy.

This takes in a username, grabs the first 5000 followers, then places their IDs in a .txt file.



Twitter Dev. REST API               https://dev.twitter.com/docs/api/1.1
Tweepy, a python Twitter package    https://pypi.python.org/pypi/tweepy/
                                    http://pythonhosted.org/tweepy/html/
                                    https://github.com/tweepy/tweepy

Twitter REST search     https://dev.twitter.com/docs/api/1.1/get/search/tweets
Tweepy search docs      http://pythonhosted.org/tweepy/html/api.html#help-methods

@auth dpb
@date 10/20/2013
"""

import tweepy

# Authorization keys. Always use OAuth! (Also, can fetch the access token in code if you want)
# To make: go to dev.twitter.com, log in, create an "application", and request an access token
consumer_key = "jkfdo86uCmN7hUzNT7RAQ"
consumer_secret = "w946MDv1ETOKT9oDzq1PmL8QVBY8soqSes43b4mcv7w"
access_token = "2187306338-LzbyxAjMINSvxUu1KBHTrRgo3QKxV6T6S6AQa7Q"
access_secret = "FsQ9zp8mBbL572P6ufF8e5DIxsqdPwI29Qq1cArrX3d6B"


# Set up OAuth via tweepy's handler object, and create an instance of the Tweepy API with auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


#taking in the twitter account we want to go through
un = raw_input("username: ");

#open a txt file with the username as the filename
follower_list = open((un + ".txt"), "w");

search_cursor = tweepy.Cursor(api.followers_ids, screen_name=un);
ids = [];

for follower in search_cursor.items(5000):
		follower_list.write(str(follower) + "\n");
		
follower_list.close();
print("All done.");