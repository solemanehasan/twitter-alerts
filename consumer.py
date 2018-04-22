import os
import json
import boto3
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

from accounts import KEYWORDS_MAP


twitter_credentials = {
    'consumer_key': os.getenv('TWITTER_CONSUMER_KEY'),
    'consumer_secret': os.getenv('TWITTER_CONSUMER_SECRET'),
    'access_token': os.getenv('TWITTER_ACCESS_TOKEN'),
    'access_token_secret': os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
}


aws_creds = {
    'key': os.getenv('AWS_APP_KEY'),
    'secret': os.getenv('AWS_APP_SECRET'),
    'topic_arn': os.getenv('AWS_TOPIC_ARN')
}


class TweetListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print('')
        try:
            list_data = json.loads(data)
            print('Fetched JSON Data')
            username = list_data['user']['screen_name']
            user_id = list_data['user']['id_str']
            tweet = list_data['text'].lower()
            print('Username: '+username)
            print('Tweet: '+tweet)

            tweet_url = 'https://twitter.com/{}/status/{}'.format(
                username,
                list_data['id_str']
            )
			# Have the bot output the overall 
            # print('Printing Tweet Data')
            # print(list_data)
            
			#print('Fetching Tweet ID Data')			
            #tweet_id = list_data['entities']['id_str']
            #print('Fetched Tweet ID Data')
            #retweet_count = list_data['entities']['retweet_count']
            #print('Fetched Retweet Count Data')
            #print('Retweet Count: '+retweet_count)
            #print('Tweet ID: '+tweet_id)
            #print('Tweet ID: '+list_data['entities']['id_str'])
			
			# This damn block of code keeps causing the "except" to be thrown
			# ---------------------------------------------------------------
            # print('Fetching Retweet Count Data')
            # retweet_count = list_data['user']['retweet_count']
            # print('Retweet Count: '+retweet_count)

        except:
            print(list_data)
            print('ERROR: Something went wrong with that tweet.')
            return

        user_keywords = KEYWORDS_MAP.get(user_id)

        if not user_keywords:
            print('Do Not have user for user id: '+user_id)
            print('Returning')
            return

        if (user_keywords['any'] and any(keyword.lower() in tweet for keyword in user_keywords['any'])) or \
                (user_keywords['all'] and all(keyword.lower() in tweet for keyword in user_keywords['all'])):
            client = boto3.client(
                "sns",
                aws_access_key_id=aws_creds['key'],
                aws_secret_access_key=aws_creds['secret'],
                region_name='us-east-1'
            )
            print('SUCCESS: tweet matched keyword')
            msg = '{} tweeted: {} ---- {}'.format(
                username,
                tweet,
                tweet_url,
            )
            print('Sending Tweet to AWS SNS Service to send texts to recipients')
            client.publish(Message=msg, TopicArn=aws_creds['topic_arn'])

    def on_error(self, status):
        print('error: ')
        print(status)


if __name__ == '__main__':
    print(twitter_credentials)

	
    auth = OAuthHandler(
        twitter_credentials['consumer_key'],
        twitter_credentials['consumer_secret']
    )
    auth.set_access_token(
        twitter_credentials['access_token'],
        twitter_credentials['access_token_secret'],
    )
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Welcome to "Twitter-Bot".  This bot will receive incoming Tweets.  If it catches a Tweet with special keywords, the recipients will be notified immediately via AWS SNS (SMS).  Starting Listener Now')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    listener = TweetListener()

    stream = Stream(auth=auth, listener=listener)
    print('authenticated')
    stream.filter(follow=KEYWORDS_MAP.keys())
	
    tweet = twitter.show_status(id='987769125924728832')
    print(tweet['text'])
