import os
from flask import Flask, render_template, request, redirect, jsonify
from dotenv import load_dotenv
import stripe

from utils.product_utils import load_products, parse_custom_options, create_metadata

# Load .env
load_dotenv()

app = Flask(__name__)

# Stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
DOMAIN_URL = os.getenv("DOMAIN_URL")

# Figure out path to products.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_PATH = os.path.join(BASE_DIR, "docs", "products.json")

# Load products at startup
PRODUCTS = load_products(PRODUCTS_PATH)

@app.route("/")
def home():
    return render_template("home.html", products=PRODUCTS.values())

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    product_id = request.form.get("product_id")
    if product_id not in PRODUCTS:
        return jsonify({"error": "Invalid product"}), 400

    product = PRODUCTS[product_id]
    custom_options = parse_custom_options(product, request.form)
    metadata = create_metadata(product_id, custom_options)

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': product["currency"],
                    'product_data': {
                        'name': product["name"],
                        'description': product["description"]
                    },
                    'unit_amount': product["price_cents"],
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=DOMAIN_URL + '/success',
            cancel_url=DOMAIN_URL + '/cancel',
            payment_intent_data={
                'metadata': metadata
            }
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/cancel")
def cancel():
    return render_template("cancel.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
