# app.py
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ip_info')
def get_ip_info():
    url = "https://ipapi.co/json/"
    try:
        response = requests.get(url)
        data = response.json()
        # Add IPv6 address to the response
        ipv6_address = data.get('ipv6', 'N/A')
        data['ipv6'] = ipv6_address
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)