import tweepy
import random
import time
from credentials import *

import tweepy
import random
import time


key_API = "mPLioqlIrkmbkVmG2Ao0Va2Qs"

secret_key_API = "uSIwhQNciHU63hY18vbcIY5PXJeB4AuEpx7bInswBFza4S0rHp"

# bearer_token = "AAAAAAAAAAAAAAAAAAAAAIsdqgEAAAAA2aMjQNNG4JwlQ%2FIuKb3%2BRrfsydQ%3Dk1BkZRayxYagKYO1YTUX13hQazMkbaEHQ9PjZIPMooopjQFPOw"

access_token = "1422523024696172544-mwmxoWvcwe36pjucP9ubitUbp5cLrI"

access_token_secret = "CUWx9L70zPVIeFn9GAoJHBhlpL02sNg1Yyn6hcRNDD4nA"

# Declaring the keys and tokens
CONSUMER_KEY = key_API
CONSUMER_SECRET = secret_key_API
ACCESS_TOKEN = access_token
ACCESS_TOKEN_SECRET = access_token_secret

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# List of quotes
quotes = [
    "The best way to predict the future is to invent it.",
    "The only way to do great work is to love what you do.",
    "If you want to achieve greatness, stop asking for permission.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
]

while True:
    # Pick a random quote
    quote = random.choice(quotes)

    # Tweet the quote
    api.update_status(quote)

    # Wait for an hour
    time.sleep(60 * 60)
