from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

inventory = [
    {
        "BARCODE": "0071315040159",
        "BRANDS": "Bread",
        "ID": 1,
        "INGREDIENTS_TEXT": "315' 04015 Clover Valley® 100% Whole Wheat Sandwich Bread 19g OF WHOLE GRAIN PER SERVING  WHOLE GRAIN WHEAT Nutrition Facts FLOUR, WATER, YEAST, SUGAR, WHEAT GLUTEN, SOYBEAN OIL, HONEY, About 19 servings per container CULTURED WHEAT FLOUR, SALT, Serving size 1 slice (33g) MOLASSES, VINEGAR, MODIFIED WHEY, WHEAT STARCH, CITRIC ACID, SESAME",
        "PRICE": 100,
        "PRODUCT_NAME": "Bread",
        "QUANTITY": None,
        "STOCK": 20,
    },
    {
        "BARCODE": "9555487800038",
        "BRANDS": "Farm Fresh",
        "ID": 2,
        "INGREDIENTS_TEXT": "_milk_",
        "PRICE": 80,
        "PRODUCT_NAME": "12000048 Pure Fresh Milk",
        "QUANTITY": "2000 g",
        "STOCK": 20,
    },
]


@app.route("/inventory/product/<int:product_id>")
def get_product(product_id):
    product = next(
        (product for product in inventory if product["ID"] == product_id), None
    )
    if not product:
        return jsonify({"error": "Products not found"}), 404
    return jsonify(product), 200


@app.route("/inventory")
def get_products():
    if not inventory:
        return jsonify({"error": "Products not found"}), 404
    return jsonify(inventory), 200


@app.route("/inventory/<int:barcode>", methods=["GET", "POST"])
def get_product_details_by_barcode_from_external_api_and_add_to_inventory(barcode):
    headers = {"User-Agent": "InventoryManagementSystem/1.0"}
    response = requests.get(
        f"https://world.openfoodfacts.org/api/v3.6/product/{barcode}.json",
        headers=headers,
    )
    if not response:
        jsonify({"error": "No response"}), 404
    data = response.json()
    if not data:
        jsonify({"error": "Products not found"}), 404

    product = data.get("product")
    product_details = {
        "BARCODE": product.get("code"),
        "PRODUCT_NAME": product.get("product_name"),
        "BRANDS": product.get("brands"),
        "INGREDIENTS_TEXT": product.get("ingredients_text"),
        "QUANTITY": product.get("quantity"),
    }
    if request.method == "GET":
        return jsonify(product_details), 200
    if request.method == "POST":
        data = request.get_json()

        product_details["STOCK"] = data.get("STOCK", 0)
        product_details["PRICE"] = data.get("PRICE", 0)
        product_details["ID"] = len(inventory) + 1
        inventory.append(product_details)
        return (
            jsonify(
                {
                    "message": "product created successfully",
                    "product_details": product_details,
                }
            ),
            201,
        )


@app.route("/inventory/<int:product_id>", methods=["PATCH"])
def update(product_id):
    data = request.get_json()
    product = next(
        (product for product in inventory if product["ID"] == product_id), None
    )
    if not product:
        return jsonify({"error": "Product not found"}), 404

    if "STOCK" in data:
        product["STOCK"] = data.get("STOCK", 0)
        return (
            jsonify(
                {"message": "Stock updated successfully", "stock": product["STOCK"]}
            ),
            200,
        )
    if "PRICE" in data:
        product["PRICE"] = data.get("PRICE", 0)
        return (
            jsonify(
                {"message": "Price updated successfully", "price": product["PRICE"]}
            ),
            200,
        )


@app.route("/inventory/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global inventory
    product = next(
        (product for product in inventory if product["ID"] == product_id), None
    )
    if not product:
        return jsonify({"error": "Product to delete not found"}), 404
    inventory = [product for product in inventory if product["ID"] != product_id]
    return jsonify({"message": "Product deleted successfully"}), 200


if __name__ == "__main__":
    app.run(port=5555, debug=True)
