#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[12]:


tweets = pd.read_csv('airline_tweets.csv')
tweets.head()


# 1. Determine the number of tweets for each airline, indicated by the name in the 'airline' column of the data set. Give the airline name and number of tweets in table form.

# In[13]:


tweets.airline.unique()


# In[14]:


tweets.groupby(['airline']).count()


# In[15]:


airline_count = tweets.groupby(['airline']).count()[['golden']]
airline_count = airline_count.rename(columns={'golden': '# Tweets'})
airline_count


# 2. For each airlines tweets, determine the percentage that are positive, based on the classification in 'airline_sentiment'. Give a table of airline name and percentage, sorted from largest percentage to smallest.

# In[16]:


airline_count['# Tweets']


# In[17]:


positive = tweets[tweets['airline_sentiment'] == 'positive'].groupby('airline').count()[['airline_sentiment']]
percent_posiitve = (positive['airline_sentiment'] / airline_count['# Tweets']) * 100
positive['% Positive'] = percent_posiitve
positive = positive.drop('airline_sentiment', axis=1)
positive.sort_values(by=['% Positive'], ascending=False)


# 3. List all user names (in the 'name' column) with at least 20 tweets along with the number of tweets for each. Give the results in table form sorted from most to least.

# In[18]:


x = tweets.groupby('name').count()
x = x[x['Unnamed: 0'] >= 20]
x = x[['Unnamed: 0']].sort_values(by=['Unnamed: 0'], ascending=False).rename(columns={'Unnamed: 0': '# Tweets'})
x


# 4. Determine the percentage of tweets from users who have more than one tweet in this data set.

# In[25]:


y = tweets.name.value_counts()
y = y[y > 1].sum()*100/len(tweets)
y


# 5. Among the negative tweets, which five reasons are the most common? Give the percentage of negative tweets with each of the five most common reasons. Sort from most to least common.

# In[22]:


negative_tweets = tweets[tweets['airline_sentiment'] == "negative"]
negative_tweets2 = tweets.groupby('airline_sentiment').get_group('negative')
(negative_tweets['tweet_id'].groupby(negative_tweets['negativereason']).count()/len(negative_tweets)*100).sort_values(ascending=False).head(5)


# 6. How many of the tweets for each airline include the phrase "on fleek"?

# In[23]:


tweet_str = tweets[tweets['text'].str.contains("on fleek")].groupby('airline').count()
tweet_str.tweet_id


# 7. What percentage of tweets included a hashtag?

# In[30]:


tweet_hash = tweets[tweets['text'].str.contains("#")]
tweet_hash.shape[0] / tweets.shape[0] * 100


# 8. How many tweets include a link to a web site?

# In[31]:


np.sum(tweets.text.str.contains("http"))


# 9. How many of the tweets include an '@' for another user besides the intended airline?

# In[32]:


np.sum(tweets.text.str.count('@') > 1)


# 10. Assign a score of 1 to each positive tweet, 0 to each neutral tweet, and -1 to each negative tweet. Determine the mean score for each airline, and give the results in table form with airlines and mean scores, sorted from highest to lowest.

# In[33]:


tweets['sentiment'] = tweets['airline_sentiment'].map({'positive': 1, 'neutral': 0, 'negative':-1})
tweets['sentiment'].groupby(tweets['airline']).mean().sort_values(ascending=False)


# 11. Among the tweets that "@" a user besides the indicated airline, what percentage include an "@" directed at the other airlines in this file? (Note: Twitterusernames are not case sensitive, so '@MyName' is the same as '@MYNAME' which is the same as '@myname'.)

# In[36]:


all_tweets = tweets['text'].str.lower()
airhandles = pd.Series(['@virginamerica','@united','@southwestair','@jetblue', 
                        '@usairways','@americanair'])
multats = np.sum(tweets['text'].str.count('@') > 1)
ct = 0
for tweet in all_tweets:
    tweetser = pd.Series(tweet.split()) 
    handlect = np.sum(airhandles.isin(tweetser)) 
    if handlect > 1: 
        ct += 1

100*ct/multats


# 12. Suppose the same user has two or more tweets in a row, based on how they appear in the file. For such tweet sequences, determine the percentage for which the most recent tweet (which comes nearest the top of the file) is a positive tweet.

# In[37]:


tweets['next_name'] = tweets.name.shift(-1)
tweets['match'] = np.where(tweets.name == tweets.next_name, True, False) 
first_match = tweets.loc[tweets['name'] != tweets['name'].shift()] 
answer = first_match[first_match.match == True]

pos = np.where(answer.airline_sentiment == 'positive',1,0).sum() 
pos/len(answer)*100


# 13. Give a count for the top-10 hashtags (and ties) in terms of the number of times each appears. Give the hashtags and counts in a table sorted from most frequent to least frequent. (Note: Twitter hashtags are not case sensitive, so ' HashTag', ' HASHtag' and ' hashtag' are all regarded as the same. Also ignore instances of hashtags that are alone with no other characters.)

# In[38]:


hashtaglist = []  
for i in range(len(tweets)):
    textlist = pd.Series(tweets.loc[i,'text'].split()).str.lower()
    hashtags = textlist[textlist.str.count('#') > 0] 
    hashtaglist = hashtaglist + list(hashtags)
pd.Series(hashtaglist).value_counts().iloc[1:12]


# In[5]:


# regex explanation: locates hashtags, extract all letters a-z following it (i.e. #destinationdragons!, #destinationdragons are the same)
# can also do without regex, and use .split() and loops


# In[ ]:




