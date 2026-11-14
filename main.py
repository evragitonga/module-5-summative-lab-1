import requests
def get_product(product_id):
    response = requests.get(f"http://127.0.0.1:5555/inventory/{product_id}")
    return response.json()
  
def get_products():
  response = requests.get(f"http://127.0.0.1:5555/inventory")
  return response.json()

def get_product_details_by_barcode(barcode):
  response = requests.get(f"http://127.0.0.1:5555/api/{barcode}")
  return response.json()

def delete_product(product_id):
  response = requests.delete(f"http://127.0.0.1:5555/inventory/{product_id}")
  return response.json()
print("1. ADD PRODUCT")
print("2. GET PRODUCT")
print("3. GET PRODUCTS")
print("4. GET PRODUCT DETAILS BY BARCODE")
print("5. DELETE PRODUCT")
choice = int(input("Select a choice 1,2,3,4,5: "))

if choice == 2:
  product_id = int(input("Enter product id: "))
  product = get_product(product_id)
  print(product)
elif choice == 3:
  products = get_products()
  print(products)
elif choice == 5:
  product_id = int(input("Enter product id: "))
  deleted_product = delete_product(product_id)
  print(deleted_product)
elif choice == 4:
  barcode = int(input("Enter barcode: "))
  product_details = get_product_details_by_barcode(barcode)
  print(product_details)