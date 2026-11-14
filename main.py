import requests
def get_product(product_id):
    response = requests.get(f"http://127.0.0.1:5555/inventory/{product_id}")
    return response.json()
  
def get_products():
  response = requests.get(f"http://127.0.0.1:5555/inventory")
  return response.json()
print("1. ADD PRODUCT")
print("2. GET PRODUCT")
print("3. GET PRODUCTS")
choice = int(input("Select a choice 1,2,3,4: "))

if choice == 2:
  product_id = int(input("Enter product id: "))
  product = get_product(product_id)
  print(product)
elif choice == 3:
  products = get_products()
  print(products)