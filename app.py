from flask import Flask,request,jsonify
import requests

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

@app.route("/api/<int:barcode>")
def get_product_from_external_api(barcode):
  headers = {
    "User-Agent":  "InventoryManagementSystem/1.0"
    }
  response = requests.get(f"https://world.openfoodfacts.org/api/v3.6/product/{barcode}.json",headers=headers)
  data =response.json()
  product = data['product']
  product_details = {"PRODUCT_NAME":product['product_name'],
                     "BRANDS":product['brands'],
                     "INGREDIENTS_TEXT":product['ingredients_text']}
  return jsonify(product_details)

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