from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)


@app.get("/api/products")
def get_products():

    url = "https://api.digikala.com/v1/search/?q=%D9%84%D9%BE%20%D8%AA%D8%A7%D9%BE&";


    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        return jsonify(data)

    except requests.RequestException as error:

        print(error)

        return jsonify({
            "error": "خطا در دریافت محصولات"
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=3000,
        debug=True
    )