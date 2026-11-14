from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

inventory = []

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

@app.route("/api/<int:barcode>",methods=['GET','POST'])
def get_product_details_by_barcode_from_external_api_and_add_to_inventory(barcode):
    headers = {
      "User-Agent":  "InventoryManagementSystem/1.0"
      }
    response = requests.get(f"https://world.openfoodfacts.org/api/v3.6/product/{barcode}.json",headers=headers)
    data =response.json()
    product = data.get('product')
    product_details = {"BARCODE":product.get('code'),
      "PRODUCT_NAME":product.get('product_name'),
                      "BRANDS":product.get('brands'),
                      "INGREDIENTS_TEXT":product.get('ingredients_text'),"QUANTITY":product.get('quantity')}
    if request.method == 'GET':
      return jsonify(product_details),200
    if request.method == "POST":
      data = request.get_json()
      
      product_details['STOCK'] = data.get("STOCK",0)
      product_details['PRICE'] = data.get("PRICE",0)
      product_details['ID'] = len(inventory) + 1
      inventory.append(product_details)
      return jsonify({"message":"product created successfully",
                      "product_details":product_details}),200

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