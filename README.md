# Inventory Management System

A simple application for adding, viewing, updating, and deleting products. It also retrieves product details using a barcode through the Open Food Facts API.

## 1. Setup

### Step 1: Install Python

Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/) and install it.

### Step 2: Fork and Clone the Repository

Fork the GitHub repository, then clone it:

```bash
git clone https://github.com/evragitonga/module-5-summative-lab-1.git
```

### Step 3: Open the Project Folder

Open the project folder in your terminal.

### Step 4: Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 5: Install Requirements

```bash
pip install -r requirements.txt
```

## 2. Run the Application

**Step 1: Start the server**

```bash
python app.py
```

**Step 2: Open another terminal and start main**

```bash
python main.py
```

## 3. Using the Application

Choose an option from the menu:

1. **Add Product:** Add a product using its barcode.
2. **Get Product:** View a product using its ID.
3. **Get All Products:** View all products in the inventory.
4. **Search Product:** Retrieve product details using a barcode.
5. **Update Product:** Update the stock or price of a product.
6. **Delete Product:** Remove a product from the inventory.
7. **Exit:** Close the application.

Follow the instructions displayed on the screen to complete each action.

## 4. Technologies Used

- Python
- Flask
- Requests
- Open Food Facts API
