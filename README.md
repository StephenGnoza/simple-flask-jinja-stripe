# Stripe Checkout Flask App

This is a simple Flask + Stripe demo app that sells products via Stripe Checkout.

🟢 Supports multiple products defined in JSON  
🟢 Dynamically generates checkout forms with options (dropdowns, textfields)  
🟢 Passes customer-selected options to Stripe as payment metadata  

Perfect as a template for small shops, digital goods, or demos!

---

## 🌟 Features

✅ Flask app with Stripe integration  
✅ Dockerized for easy deployment (e.g. Google Cloud Run)  
✅ Products defined in `docs/products.json`  
✅ Supports custom product options:  
- Dropdown (e.g. colors)  
- Textfield (e.g. custom message)  
✅ Stripe Checkout for secure payment  
✅ Metadata passed to Stripe PaymentIntent  

---

## 🗂️ Project Structure

```
.
├── app.py
├── utils/
│   ├── __init__.py
│   └── product_utils.py
├── docs/
│   └── products.json
├── templates/
│   ├── home.html
│   ├── success.html
│   └── cancel.html
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 🚀 Quick Start

### 1️⃣ Clone the repo

```bash
git clone https://github.com/StephenGnoza/simple-flask-jinja-stripe.git
cd simple-flask-jinja-stripe
```

---

### 2️⃣ Set up your Stripe keys

Create a `.env` file:

```
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
DOMAIN_URL=http://localhost:8080
```

✅ Replace with your Stripe test keys.  
✅ `DOMAIN_URL` is where Stripe will redirect after payment. Use localhost for local dev.

---

### 3️⃣ Install dependencies (local)

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Then open in your browser:

```
http://localhost:8080
```

---

### 4️⃣ Use Docker (optional)

Build and run with Docker Compose:

```bash
docker-compose up --build
```

✅ This uses your `.env` file automatically!

---

## ⚙️ Define Products

Products are defined in:

```
docs/products.json
```

Example:

```json
[
    {
        "id": "custom_message",
        "name": "Custom Mug",
        "description": "A mug with options.",
        "price_cents": 1500,
        "currency": "usd",
        "options": [
          ["Size", "dropdown", "12oz,16oz"],
          ["Custom Message", "textfield"]
        ]
    }
  ]
```

✅ Supports:  
- **Dropdown**: `["Label", "dropdown", "Choice1,Choice2,Choice3"]`  
- **Textfield**: `["Label", "textfield"]`  

✅ Add as many products and options as you like.

---

## 🧭 How It Works

⭐ Home page renders all products from JSON  
⭐ Each product has its options in a form  
⭐ On "Buy Now", creates Stripe Checkout Session  
⭐ User pays via Stripe Checkout  
⭐ Options selected are passed as metadata to Stripe PaymentIntent  
⭐ You see them in the Stripe Dashboard

---

## 📝 License

MIT

---

## 📌 Notes

⚠️ This is a demo template.  
You are responsible for PCI compliance in production.  
Always secure your keys and consider using Stripe Webhooks for order fulfillment.

---

## 🏁 Author

Built with ❤️ by [Stephen Gnoza](https://github.com/StephenGnoza)
