# twitter-alerts
Scan tweets for keywords and alert
Run this on a Linux Machine (whether it be an AWS EC2 Linux Server or Local Linux VM).


## Setup

1) Keys Retrieval
```
#Create Twitter Developer Account
Go to https://apps.twitter.com/ and create new app
Click on the “Users” tab
Create new user
Retrieve Twitter API Keys
Consumer Key (API Key) == TWITTER_CONSUMER_KEY
Consumer Secret (API Secret) == TWITTER_CONSUMER_SECRET
Access Token == TWITTER_ACCESS_TOKEN
Access Token Secret == TWITTER_ACCESS_TOKEN_SECRET

#Create AWS Development Account
Go to https://console.aws.amazon.com/iam/home#/home
Generate Access Key
Access Key ID == AWS_APP_KEY
Secret Access Key == AWS_APP_SECRET

Create Topic
Topic ARN == AWS_TOPIC_ARN
```


2) Set Env Variables
```
export AWS_APP_KEY= <key> 
export AWS_APP_SECRET= <key> 
export AWS_TOPIC_ARN= <key> 
export TWITTER_CONSUMER_KEY= <key> 
export TWITTER_CONSUMER_SECRET= <key> 
export TWITTER_ACCESS_TOKEN= <key> 
export TWITTER_ACCESS_TOKEN_SECRET= <key> 
```

3) Confirm that Env Variables have been set
```
printenv AWS_APP_KEY
printenv AWS_APP_SECRET
printenv AWS_TOPIC_ARN
printenv TWITTER_CONSUMER_KEY
printenv TWITTER_CONSUMER_SECRET
printenv TWITTER_ACCESS_TOKEN
printenv TWITTER_ACCESS_TOKEN_SECRET
```

4) Confirm that you have Python, install it if you don't have it

```
python -V
```

5) Confirm that you have pip, install it if you don't have it
```
pip -V
```

6) Install virtualenv
```
pip install virtualenv
```

7) Install all required python modules
```
pip install -r requirements.txt
```


8) Create a virtual environment
```
virtualenv -p /path/to/python3 .env
```


## Test Whether it Works

1) Replace every reference of “brothaakhee” with your own Twitter Handle and ID in the "accounts.py" file
   Use http://gettwitterid.com/?user_name=BobJohn68918112&submit=GET+USER+ID to get the Twitter ID for your Twitter Handle/Username.

Use `python3 consumer.py` to start streaming listener, or use supervisor to keep the process running.

```

Each account you want to follow should be added to `consumer.py` through its ID. The ID should be a string.
Use an online tool(http://gettwitterid.com/?user_name=BobJohn68918112&submit=GET+USER+ID ) to look up a twitter handle's ID, and then map that to a variable with the name of the handle.

`brothaakhee = '123456'`

That variable should then be mapped to the keywords you want to alert on through a dict.

```
{
    brothaakhee: {
        'all': ['keywords', 'that', 'should', 'all', 'be', 'present'],
        'any': ['keywords', 'that', 'will alert', 'even if', 'one is present']
    }
}
```

2) 