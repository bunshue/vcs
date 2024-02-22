import subprocess

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

class ProductResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    img = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    search_text = db.Column(db.String(255))
    source = db.Column(db.String(255))

    def __init__(self, name, img, url, price, search_text, source):
        self.name = name
        self.url = url
        self.img = img
        self.price = price
        self.search_text = search_text
        self.source = source


class TrackedProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tracked = db.Column(db.Boolean, default=True)

    def __init__(self, name, tracked=True):
        self.name = name
        self.tracked = tracked

@app.route("/update-tracked-products", methods=["POST"])
def update_tracked_products():
    tracked_products = TrackedProducts.query.all()
    url = "https://amazon.ca"

    product_names = []
    for tracked_product in tracked_products:
        name = tracked_product.name
        if not tracked_product.tracked:
            continue

        command = f"python ./scraper/__init__.py {url} \"{name}\" /results"
        subprocess.Popen(command, shell=True)
        product_names.append(name)

    response = {'message': 'Scrapers started successfully',
                "products": product_names}
    return jsonify(response), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
