import feedparser

def get_headlines(rss_url):
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Extract the titles from the entries
    headlines = [entry.title for entry in feed.entries]

    return headlines

google_news_url = "https://news.google.com/news/rss"
# print(get_headlines(google_news_url))

