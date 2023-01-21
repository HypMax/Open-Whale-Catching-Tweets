
import tweepy
import re
import datetime
import pandas as pd
import pytz
import hiddenAPI

def whale_catching_tweets(): 
    # Set up authentication for tweepy
    auth = tweepy.OAuthHandler(hiddenAPI.consumer_key, hiddenAPI.consumer_secret)
    auth.set_access_token(hiddenAPI.access_token, hiddenAPI.access_token_secret)

    # Set up tweepy API
    api = tweepy.API(auth)

    # Set the user to extract tweets from
    username = "whale_alert"

    # Get the user's timeline tweets up to max of 50
    timeline = api.user_timeline(screen_name=username, count=50)

    # Create two lists from the timeline of tweets one for text and one for date
    raw_tweets = []
    raw_tweets_date = []
    for tweet in timeline:
        raw_tweets.append([tweet.text])
        raw_tweets_date.append([tweet.created_at])

    # Filter tweets and created at dates within 24 hours of UTC
    tz = pytz.timezone('UTC')
    now = datetime.datetime.now(tz)
    TwentyfourHours = datetime.timedelta(hours=24)
    fullday_tweets_date = []
    fullday_tweets = []
    for tweet in timeline:
        created_at = tweet.created_at.astimezone(tz)
        if tweet.created_at > now - TwentyfourHours:
            fullday_tweets_date.append([tweet.created_at])
            fullday_tweets.append([tweet.text])

    # clean string sentences to remove non-standard characters and links
    clean_string_list = []
    for string in fullday_tweets:
        # Remove non-standard characters using a regular expression
        clean_string = re.sub(r'[^\w\s]', '', string[0])
        # Remove website links
        clean_string = re.sub(r'\n\nhttp\S+', '', clean_string)
        clean_string_list.append(clean_string)

    # Split list of tweet sentences into lists of words
    split_list = []
    for string in clean_string_list:
        words = string.split()
        split_list.append(words)

    # Use a junk list for removed tweets and datetimes which don't meet desired ouput and structure requirement
    junk_list = []
    junk_dates = []
    junk_dates_index = []
    clean_split_list = split_list
    # 1st & 3rd list items must be amounts as integers 
    for i, item in enumerate(split_list):
        try:
            int(item[0])
            int(item[2])
        except ValueError:
            junk_list.append(item)
            clean_split_list.remove(item)
            junk_dates_index.append(i)
            junk_dates.insert(i, fullday_tweets_date[i])
            del fullday_tweets_date[i]

    # Joins sender name between strings 'from' and 'to' and receiver name after 'to'
    for i, row in enumerate(split_list):
        try:
            from_index = row.index('from')
            to_index = row.index('to')
        except ValueError:
            from_index = None
            to_index = None
        # Do process only if 'from' and 'to' both found
        if from_index is not None and to_index is not None:
            from_elements = ' '.join(row[from_index+1:to_index])
            to_elements = ' '.join(row[to_index+1:])
            split_list[i] = row[:from_index] + [from_elements, to_elements]
    # Joins entity name strings after 'at' 
    for i, row in enumerate(split_list):
        try:
            at_index = row.index('at')
        except ValueError:
            at_index = None
        # Do process only if 'at' found
        if at_index is not None:
            at_elements = ' '.join(row[at_index+1:])
            split_list[i] = row[:at_index] + [at_elements]

    # Junk list any items which don't meet table structure: lengths must be no less than 6 or more than 7
    for i, item in enumerate(split_list):
        if len(item) < 6 or len(item) > 7:
            junk_list.append(item)
            clean_split_list.remove(item)
            junk_dates_index.append(i)
            junk_dates.insert(i, fullday_tweets_date[i])
            del fullday_tweets_date[i]
        else:
            pass

    # Create a list of tuples from the clean_split_list and tweets_date lists to pass into table structure
    data = [(date[0], *row) for date, row in zip(fullday_tweets_date, clean_split_list)]
    del row
    # Create the DataFrame from the data list and specify the column names
    df = pd.DataFrame(data, columns=['Date', 'Amount (No.)', 'Cryptocurrency', 'Amount ($)', 'Currency', 'Action', 'From', 'To'])

    # Write the DataFrame to a CSV file
    df.to_csv('whale_alert_tweets.csv', index=False)

    if junk_list:
        # Create a list of tuples from the junk_list and junk_dates lists to pass into table structure
        junk_data = [(date[0], *row) for date, row in zip(junk_dates, junk_list)]
        # Create a DataFrame from the junk_list
        junk_df = pd.DataFrame(junk_data, columns=['Date', *[f'Junk {i}' for i in range(len(junk_list[0]))]])
        # Write the junk_df DataFrame to a sheet in the same CSV file
        junk_df.to_csv('junk_whale_alert_tweets.csv', index=False, header=False, mode='a')
    else: print("No junk twitter posts today")

whale_catching_tweets()
