import feedparser

def get_articles():
    rss_urls = [
        "https://www.vsd.fr/feed/",
        "https://www.public.fr/feed/"
    ]
    
    articles = []
    for url in rss_urls:
        feed = feedparser.parse(url)
        
        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "url": entry.link,
                "content": entry.summary
            })
    
    return articles
