from flask import Flask, render_template, request
from backend import search_similar_articles

app = Flask(__name__)
# Reminder:
# POST is an HTTP method used to send data to the server.
# GET is used to retrieve data from the server

# Definition of the main route ('/') that accepts GET and POST requests (For Flask)
@app.route('/', methods=['GET', 'POST'])
def search():
    results = []

    if request.method == 'POST':
        query = request.form['query']
        results = search_similar_articles(query)

    return render_template('index.html', results=results)
    
if __name__ == '__main__':
    app.run(debug=True)

