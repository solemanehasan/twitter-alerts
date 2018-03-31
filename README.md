# twitter-alerts
Scan tweets for keywords and alert


1) Confirm that you have Python, install it if you don't have it
----------------------------------------------------------------
```
python -V
```

2) Confirm that you have pip, install it if you don't have it
```
> pip -V
```

3) Set Env Variables
```
export AWS_APP_KEY= <key> 
export AWS_APP_SECRET= <key> 
export AWS_TOPIC_ARN= <key> 
export TWITTER_CONSUMER_KEY= <key> 
export TWITTER_CONSUMER_SECRET= <key> 
export TWITTER_ACCESS_TOKEN= <key> 
export TWITTER_ACCESS_TOKEN_SECRET= <key> 
```

4) Confirm that Env Variables have been set
```
printenv AWS_APP_KEY
printenv AWS_APP_SECRET
printenv AWS_TOPIC_ARN
printenv TWITTER_CONSUMER_KEY
printenv TWITTER_CONSUMER_SECRET
printenv TWITTER_ACCESS_TOKEN
printenv TWITTER_ACCESS_TOKEN_SECRET
```


5) Install all required python modules
```
pip install -r requirements.txt
```


6) Create a virtual environment
```
`virtualenv -p /path/to/python3 .env'
```



Use `python3 consumer.py` to start streaming listener, or use supervisor to keep the process running.

```

Each account you want to follow should be added to `consumer.py` through its ID. The ID should be a string.
Use an online tool to look up a twitter handle's ID, and then map that to a variable with the name of the handle.

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
