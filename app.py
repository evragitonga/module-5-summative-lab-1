from flask import Flask,request,jsonify

app = Flask(__name__)

inventory = [{
  "id":4
}]

@app.route("/inventory/<int:product_id>")
def get_product(product_id):
  product = next((product for product in inventory if product['id'] == product_id),None)
  if not product:
    return jsonify({"error":"Products not found"}),404
  return jsonify(product),200

@app.route("/inventory")
def get_products():
  if not inventory:
    return jsonify({"error":"Products not found"}),404
  return jsonify(inventory),200

@app.route("/inventory/<int:product_id>",methods=['DELETE'])
def delete_product(product_id):
  global inventory
  product = next((product for product in inventory if product['id'] == product_id),None)
  if not product:
    return jsonify({"error":"Product to delete not found"}),404
  inventory = [product for product in inventory if product['id']!= product_id]
  return jsonify({"message":"Product deleted successfully"}),200

if __name__ == "__main__":
  app.run(port=5555,debug=True)