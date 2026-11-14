from flask import Flask,request,jsonify

app = Flask(__name__)

inventory = []

@app.route("/inventory/<int:product_id>")
def get_product(product_id):
  product = next((product for product in inventory if product.id == product_id),None)
  if not product:
    return jsonify("Product not found",404)
  return jsonify(product)

@app.route("/inventory")
def get_products():
  if not inventory:
    return jsonify("Products not found",404)
  return jsonify(inventory),200

if __name__ == "__main__":
  app.run(port=5555,debug=True)