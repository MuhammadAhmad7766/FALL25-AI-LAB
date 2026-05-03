import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Fetching a list of sample posts from a public API
    api_url = "https://jsonplaceholder.typicode.com/posts?_limit=5"
    response = requests.get(api_url)
    
    # Check if request was successful, then convert to JSON
    posts = response.json() if response.status_code == 200 else []
    
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)