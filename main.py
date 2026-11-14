import requests


def get_product(product_id):
    response = requests.get(f"http://127.0.0.1:5555/inventory/product/{product_id}")
    return response.json()


def get_products():
    response = requests.get(f"http://127.0.0.1:5555/inventory")
    return response.json()


def get_product_details_by_barcode(barcode):
    response = requests.get(f"http://127.0.0.1:5555/inventory/{barcode}")
    return response.json()


def add_product_by_barcode(barcode, stock, price):
    response = requests.post(
        f"http://127.0.0.1:5555/inventory/{barcode}",
        json={"STOCK": stock, "PRICE": price},
    )
    return response.json()


def update_stock_levels(product_id, stock):
    response = requests.patch(
        f"http://127.0.0.1:5555/inventory/{product_id}", json={"STOCK": stock}
    )
    return response.json()


def update_price(product_id, price):
    response = requests.patch(
        f"http://127.0.0.1:5555/inventory/{product_id}", json={"PRICE": price}
    )
    return response.json()


def delete_product(product_id):
    response = requests.delete(f"http://127.0.0.1:5555/inventory/{product_id}")
    return response.json()


def main():
    while True:
        print("1. ADD PRODUCT")
        print("2. GET PRODUCT")
        print("3. GET PRODUCTS")
        print("4. GET PRODUCT DETAILS BY BARCODE")
        print("5. UPDATE STOCK LEVELS OR PRICE")
        print("6. DELETE PRODUCT")
        print("7. Exit")

        choice = int(input("Select a choice 1,2,3,4,5,6,7: "))

        if choice == 1:
            barcode = int(input("Enter barcode: "))
            stock = int(input("Enter stock levels: "))
            price = int(input("Enter price: "))
            new_product = add_product_by_barcode(barcode, stock, price)
            print(new_product)
        elif choice == 2:
            product_id = int(input("Enter product id: "))
            product = get_product(product_id)
            print(product)
        elif choice == 3:
            products = get_products()
            print(products)
        elif choice == 4:
            barcode = int(input("Enter barcode: "))
            product_details = get_product_details_by_barcode(barcode)
            print(product_details)
        elif choice == 5:
            product_id = int(input("Enter product id: "))
            print("1. STOCK")
            print("2. PRICE")
            print("3. EXIT")
            choice = int(input("Select a choice 1,2,3: "))
            if choice == 1:
                stock = int(input("Enter stock levels: "))
                updated_product = update_stock_levels(product_id, stock)
                print(updated_product)
            elif choice == 2:
                price = int(input("Enter price: "))
                updated_product = update_price(product_id, price)
                print(updated_product)
            elif choice == 3:
                break
            else:
                print("Invalid input")
        elif choice == 6:
            product_id = int(input("Enter product id: "))
            deleted_product = delete_product(product_id)
            print(deleted_product)
        elif choice == 7:
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
  main()