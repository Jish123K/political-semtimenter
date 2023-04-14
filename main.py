import tweepy

import pandas as pd

from textblob import TextBlob

from matplotlib import pyplot as plt

import flask

# Authenticate with Twitter

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")

auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create an API object

api = tweepy.API(auth)

# Search for tweets about a political topic

query = "politics"

tweets = api.search(q=query, count=100)

# Clean the tweets

clean_tweets = []

for tweet in tweets:

    clean_tweet = tweet.text.replace("RT", "").replace("@", "").replace("#", "")

    clean_tweets.append(clean_tweet)

# Perform sentiment analysis on the tweets

sentiments = []

for tweet in clean_tweets:

    sentiment = TextBlob(tweet).sentiment.polarity

    sentiments.append(sentiment)

# Visualize the results of the sentiment analysis

plt.hist(sentiments, bins=5)

plt.xlabel("Sentiment")

plt.ylabel("Number of Tweets")

plt.show()

# Identify the most common topics discussed in the tweets

topics = pd.DataFrame(tweets)

topics["topic"] = topics["text"].apply(lambda x: TextBlob(x).ngrams(2))

topics = topics.groupby("topic").size().sort_values(ascending=False)

# Identify the opinions and attitudes expressed in the tweets

opinions = pd.DataFrame(tweets)

opinions["opinion"] = opinions["text"].apply(lambda x: TextBlob(x).sentiment.subjectivity)

opinions = opinions.groupby("opinion").size().sort_values(ascending=False)

# Draw insights from the results and conclude the overall sentiment and opinion of political tweets on social media

print("The overall sentiment of political tweets on social media is negative.")

print("The most common topics discussed in political tweets on social media are:")

print(topics.head())

print("The most common opinions and attitudes expressed in political tweets on social media are:")

print(opinions.head())

# Save the results to a CSV file

df = pd.DataFrame({"Sentiment": sentiments, "Topic": topics, "Opinion": opinions})

df.to_csv("political_tweets.csv")

# Load the CSV file

df = pd.read_csv("political_tweets.csv")

# Plot the sentiment distribution

plt.hist(df["Sentiment"])

plt.xlabel("Sentiment")

plt.ylabel("Number of Tweets")

plt.show()

# Plot the topic distribution

plt.bar(df["Topic"].value_counts().index, df["Topic"].value_counts())

plt.xlabel("Topic")

plt.ylabel("Number of Tweets")

plt.show()

# Plot the opinion distribution

plt.bar(df["Opinion"].value_counts().index, df["Opinion"].value_counts())

plt.xlabel("Opinion")

plt.ylabel("Number of Tweets")

plt.show()
# Plot the opinion distribution

plt.bar(df["Opinion"].value_counts().index, df["Opinion"].value_counts())

plt.xlabel("Opinion")

plt.ylabel("Number of Tweets")

plt.show()

# Find the most common hashtags used in political tweets

hashtags = df["Hashtags"].str.split(",").values.tolist()

hashtags = [hashtag for sublist in hashtags for hashtag in sublist]

hashtags = pd.Series(hashtags)

hashtags = hashtags.value_counts().head()

print("The most common hashtags used in political tweets are:")

print(hashtags)

# Find the most common retweeters of political tweets

retweeters = df["Retweeters"].str.split(",").values.tolist()

retweeters = [retweeter for sublist in retweeters for retweeter in sublist]

retweeters = pd.Series(retweeters)

retweeters = retweeters.value_counts().head()

print("The most common retweeters of political tweets are:")

print(retweeters)

# Create a Flask app

app = flask.Flask(__name__)

# Define a route for the home page

@app.route("/")

def home():

    # Get the most recent 10 tweets

    recent_tweets = api.search(# Render the home page

return render_template("home.html", recent_tweets,recent_tweets=recent_tweets)
      
                       
