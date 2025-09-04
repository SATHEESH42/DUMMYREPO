from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    # Simulate search results
    results = [
        {'title': 'Google', 'url': 'https://www.google.com', 'snippet': 'Search the world\'s information, including webpages, images, videos and more.'},
        {'title': 'Google Search', 'url': 'https://www.google.com/search?q=' + query, 'snippet': f'Results for {query}'}
    ]
    return jsonify({'query': query, 'results': results})

if __name__ == '__main__':
    app.run(debug=True)