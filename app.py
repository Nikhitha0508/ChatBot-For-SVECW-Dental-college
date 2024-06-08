from flask import Flask, render_template, request
from dental_chatbot import greeting, response  # Import your chatbot functions
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app)


@app.route('/')
@cache.cached(timeout=300)
def cached_endpoint():
    # Your expensive computation or database query here
    return 'Cached response' 
def home():
    return render_template("index.html")

# Flask endpoint modification
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    response_message = response(user_message)
    return response_message  # Return the response as a string


if __name__ == '__main__':
    app.run(debug=True)

