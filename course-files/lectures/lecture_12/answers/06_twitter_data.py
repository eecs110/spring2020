import urllib.request
import json
import ssl
import pprint

# write a program that:
# 1. Prompts the user for a search term
# 2. Queries Twitter for status updates based on the search term
# 3. Iterates through the resulting data dictionary and
# 4. Prints the text of the status and the number of times it has been retweeted

# necessary for accessing data via https protocol:
context = ssl._create_unverified_context()

search_term = input('Please enter a search term: ')
search_term = search_term.replace(' ', '+')
url = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json?q='
url += search_term
response = urllib.request.urlopen(url, context=context)
statuses = json.loads(response.read().decode())
# print(type(statuses))
tweet_count = 0
tweet_text = ''
for status in statuses:
    if status.get('retweet_count') > tweet_count:
        tweet_count = status.get('retweet_count')
        tweet_text = status.get('text')

print('Most Popular:')
print(tweet_count, tweet_text)
