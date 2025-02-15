from backend import search_similar_articles

# Testing a user request
query = "Actus Elon Musk"

results = search_similar_articles(query)

# This function displays the results
for result in results:
    print(f"Title: {result['title']}\nLink: {result['link']}\nSimilarity Score: {result['similarity_score']}\n")