import string
import random
from flask import Flask, request, jsonify, redirect, url_for
import validators
import db

app = Flask(__name__)

# Generates a random 6-character string (e.g., "aB3xY9")
def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

@app.route('/')
def home():
    return "Welcome to the URL Shortener API!"

@app.route('/api/urls', methods=['POST'])
def shorten_url():
    data = request.get_json()
    
    # 1. Validation
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' field"}), 400
        
    original_url = data['url']
    
    if not validators.url(original_url):
        return jsonify({"error": "Invalid URL format"}), 400

    # 2. Generate code and save to DB
    short_code = generate_short_code()
    
    # Retry up to 5 times if there's a collision
    success = False
    for _ in range(5):
        success = db.insert_url(short_code, original_url)
        if success:
            break
        short_code = generate_short_code()
        
    if not success:
        return jsonify({"error": "Could not generate a unique code"}), 500

    # 3. Return success response
    return jsonify({
        "short_code": short_code,
        "short_url": request.host_url + short_code,
        "original_url": original_url
    }), 201

@app.route('/<string:code>', methods=['GET'])
def redirect_url(code):
    # 1. Look up the code in the DB
    row = db.get_url_by_code(code)
    
    if row is None:
        return jsonify({"error": "URL not found"}), 404
        
    # 2. Increment click count
    db.increment_clicks(code)
    
    # 3. Redirect the user (302 is temporary, which allows tracking)
    return redirect(row['original_url'], code=302)

if __name__ == '__main__':
    db.init_db() # Initialize the database
    app.run(debug=True)