from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for wooden products
products = [
    {"id": 1, "name": "Oak Dining Table", "price": 450.00, "description": "Elegant oak dining table with a rustic finish.", "image": "oak_table.jpg"},
    {"id": 2, "name": "Walnut Coffee Table", "price": 250.00, "description": "Modern coffee table made from premium walnut.", "image": "walnut_table.jpg"},
    {"id": 3, "name": "Pine Bookshelf", "price": 120.00, "description": "Durable pine bookshelf with multiple compartments.", "image": "pine_bookshelf.jpg"},
    {"id": 4, "name": "Mahogany Bed Frame", "price": 700.00, "description": "Luxurious mahogany bed frame with intricate carvings.", "image": "mahogany_bed.jpg"}
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        customer_name = request.form['name']
        customer_email = request.form['email']
        selected_product = request.form['product']
        return render_template('thank_you.html', name=customer_name, product=selected_product)
    return render_template('checkout.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
