from app import app, inventory


def test_get_product():
    inventory.clear()
    inventory.append({
            "BARCODE": "9555487800038",
            "BRANDS": "Farm Fresh",
            "ID": 2,
            "INGREDIENTS_TEXT": "_milk_",
            "PRICE": 80,
            "PRODUCT_NAME": "12000048 Pure Fresh Milk",
            "QUANTITY": "2000 g",
            "STOCK": 20,
        })

    response = app.test_client().get("/inventory/product/2")

    assert response.status_code == 200
    assert response.json["PRODUCT_NAME"] == "12000048 Pure Fresh Milk"


def test_delete_product():
    inventory.clear()
    inventory.append({
            "BARCODE": "9555487800038",
            "BRANDS": "Farm Fresh",
            "ID": 2,
            "INGREDIENTS_TEXT": "_milk_",
            "PRICE": 80,
            "PRODUCT_NAME": "12000048 Pure Fresh Milk",
            "QUANTITY": "2000 g",
            "STOCK": 20,
        })

    response = app.test_client().delete("/inventory/2")

    assert response.status_code == 200
