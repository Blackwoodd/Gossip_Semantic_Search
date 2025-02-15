from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from extract_rss import get_articles
import json

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load pre-generated embeddings from JSON file
def load_embeddings():
    with open('data/embeddings.json', 'r') as file:
        # Loads the content of the JSON file and stores it in 'embeddings_data'.
        embeddings_data = json.load(file)

    embeddings = [item['embedding'] for item in embeddings_data]
    titles = [item['title'] for item in embeddings_data]

    return embeddings, titles, embeddings_data


# Transforming the request into embedding
def create_query_embedding(query):
    return model.encode([query])

def search_similar_articles(query):
    #Call function to update JSON file with latest articles (drawback: slows down code)
    #To improve, create an independent script to upldat ethe JSON file
    get_articles()


    query_embedding = create_query_embedding(query)
    
    embeddings, titles, embeddings_data = load_embeddings()
    
    # Calculate cosine similarity between query and articles
    similarities = cosine_similarity(query_embedding, embeddings)
    
    top_n = 5
    top_indices = similarities[0].argsort()[-top_n:][::-1]
    
    results = []
    for i in top_indices:
        similarity_score = similarities[0][i]
        if similarity_score > 0.5:
            result = {
                'title': titles[i],
                'link': embeddings_data[i]['link'],
                'similarity_score': similarity_score
            }
            results.append(result)

    if not results:
        return [{"title": "Aucun article pertinent trouvé.", "link": "#", "similarity_score": 0}]

    return results

