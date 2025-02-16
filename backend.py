from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
from extract_rss import get_articles

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def load_embeddings():
    try:
        with open('data/embeddings.json', 'r') as file:
            embeddings_data = json.load(file)
        
        embeddings = [item['embedding'] for item in embeddings_data]
        titles = [item['title'] for item in embeddings_data]

        return embeddings, titles, embeddings_data
    except FileNotFoundError:
        return [], [], []

# Transforming the request into embedding
def create_query_embedding(query):
    return model.encode([query])

# Update embeddings and save articles in a JSON file
def update_embeddings():
    articles = get_articles()
    
    embeddings_data = []
    for article in articles:
        article_embedding = model.encode(article['content'])
        embeddings_data.append({
            'title': article['title'],
            'link': article['url'],
            'embedding': article_embedding.tolist()
        })
    
    with open('data/embeddings.json', 'w') as file:
        json.dump(embeddings_data, file)
    
    print("Embedding file successfully updated.")

def search_similar_articles(query):
    # Call function to update JSON file with latest articles (drawback: slows down code)
    #To improve, create an independent script to upldat ethe JSON file
    update_embeddings()

    query_embedding = create_query_embedding(query)
    
    embeddings, titles, embeddings_data = load_embeddings()
    
    # Calculate cosine similarity between query and articles
    similarities = cosine_similarity(query_embedding, embeddings)
    
    top_n = 5
    top_indices = similarities[0].argsort()[-top_n:][::-1]
    
    results = []
    for i in top_indices:
        similarity_score = similarities[0][i]
        if similarity_score > 0.4:
            result = {
                'title': titles[i],
                'link': embeddings_data[i]['link'],
                'similarity_score': similarity_score
            }
            results.append(result)

    if not results:
        return [{"title": "No relevant articles found.", "link": "#", "similarity_score": 0}]

    return results
