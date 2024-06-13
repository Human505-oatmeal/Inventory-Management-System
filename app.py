import psycopg2
import logging
import os
import subprocess
from psycopg2 import OperationalError, DatabaseError
from config import db_params

logging.basicConfig(level=logging.INFO)


def get_connection():
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except OperationalError as e:
        logging.error(f"Connection error: {e}")
        exit()

def create_category(name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO CATEGORIES (name) VALUES (%s)", (name,))
                conn.commit()
                logging.info("Category created successfully.")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error creating category {e}")

def read_categories():
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM CATEGORIES")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
            except DatabaseError as e:
                logging.error(f"Error reading categories: {e}")

def update_category(category_id, new_name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("UPDATE CATEGORIES SET NAME = %s WHERE id = %s", (new_name, category_id))
                conn.commit()
                logging.info("Category updated successfully.")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error updating category: {e}")

def delete_category(category_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("DELETE FROM CATEGORIES WHERE id = %s", (category_id,))
                conn.commit()
                logging.info("Category deleted Successfully.")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error deleting category: {e}")

def create_suppliers(name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO SUPPLIERS (name) VALUES (%s)", (name,))
                conn.commit()
                logging.info("Supplier created successfully!")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error creating supplier: {e}")

def read_suppliers():
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM SUPPLIERS")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
            except DatabaseError as e:
                logging.error(f"Error reading supplier: {e}")

def update_suppliers(supplier_id, name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("UPDATE SUPPLIERS SET NAME = %s WHERE id = %s", (name, supplier_id))
                conn.commit()
                logging.info("Suppliers updated successfully.")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error updating supplier: {e}")

def delete_suppliers(supplier_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("DELETE FROM SUPPLIERS WHERE ID = %s", (supplier_id,))
                conn.commit()
                logging.info("Supplier deleted successfully.")
            except DatabaseError as e:
                conn.rollback
                logging.error(f"Error deleting supplier: {e}")

def create_products(name, category_id, supplier_id, quantity, price):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO PRODUCTS (name, category_id, supplier_id, quantity, price) VALUES (%s, %s, %s, %s, %s)", (name, category_id, supplier_id, quantity, price))
                conn.commit()
                logging.info("Products created successfully.")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error creating product: {e}")

def read_products():
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM PRODUCTS")
                conn.commit()
                rows = cur.fetchall()
                for row in rows:
                    print(row)
            except DatabaseError as e:
                logging.error(f"Error reading products: {e}")

def update_products(product_id, name, category_id, supplier_id, quantity, price):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("UPDATE PRODUCTS SET name = %s, category_id = %s, supplier_id = %s, quantity = %s, price = %s WHERE id = %s", (name, category_id, supplier_id, quantity, price, product_id))
                conn.commit()
                logging.info("Products updated successfully.")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error updating product: {e}")           

def delete_products(product_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("DELETE FROM products WHERE id = %s", (product_id))
                conn.commit()
                logging.info("Deleted product successfully.")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error deleting product: {e}")

def create_inventory_transactions(product_id, transaction_type, quantity):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO INVENTORY_TRANSACTIONS (product_id, transaction_type, quantity) VALUES (%s, %s, %s)", (product_id, transaction_type, quantity))
                conn.commit()
                logging.info("Created inventory transaction successfully.")
            except DatabaseError as e:
                conn.rollback()
                logging.error(f"Error creating inventory transactions: {e}")

def read_inventory_transactions():
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM INVENTORY_TRANSACTIONS")
                conn.commit()
                rows = cur.fetchall()
                for row in rows:
                    print(row)
            except DatabaseError as e:
                logging.error(f"Error reading inventory transactions: {e}")

def backup():
    try:
        os.environ['PGPASSWORD'] = db_params["password"]
        command = [
            "pg_dump",
            "--dbname", db_params["database"],
            "--username", db_params["user"],
            "--host", db_params["host"],
            "--port", db_params["port"],
            "--no-password",
            "--file", "backup.sql"
        ]
        subprocess.run(command, check=True)
    except Exception as db_err:
        logging.error(f"Error: {db_err}")


def category_operations():
    while True:
        print(
            """Category Operations:
1. Create Category
2. Read Category
3. Update Category
4. Delete Category
5. Back to Main Menu"""
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Create name: ")
            create_category(name)
        elif choice == "2":
            read_categories()
        elif choice == "3":
            category_id = int(input("Enter Category ID: "))
            new_name = input("Enter new name: ")
            update_category(category_id, new_name)
        elif choice == "4":
            category_id = int(input("Enter Category ID: "))
            delete_category(category_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        
def supplier_operations():
    while True:
        print(
            """Supplier Operations:
1. Create Supplier
2. Read Supplier
3. Update Supplier
4. Delete Supplier
5. Back to Main Menu"""
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Create name: ")
            create_suppliers(name)
        elif choice == "2":
            read_suppliers()
        elif choice == "3":
            supplier_id = int(input("Enter Supplier ID: "))
            new_name = input("Enter supplier new name: ")
            update_suppliers(supplier_id, new_name)
        elif choice == "4":
            supplier_id = int(input("Enter Supplier ID: "))
            delete_suppliers(supplier_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
def product_operations():
    while True:
        print(
            """Product Operations:
1. Create Product
2. Read Product
3. Update Product
4. Delete Product
5. Back to Main Menu"""
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter a new name: ")
            category_id = int(input("Enter your category ID: "))
            supplier_id = int(input("Enter your supplier ID: "))
            quantity = int(input("Enter your quantity: "))
            price = float(input("Enter your price: "))
            create_products(name, category_id, supplier_id, quantity, price)
        elif choice == "2":
            read_products()
        elif choice == "3":
            product_id = int(input("Enter your product ID: "))
            name = input("Enter your product name: ")
            category_id = int(input("Enter category ID: "))
            supplier_id = int(input("Enter supplier ID: "))
            quantity = int(input("Enter your product quantity: "))
            price = float(input("Enter your product price: "))
            update_products(product_id, name, category_id, supplier_id, quantity, price)
        elif choice == "4":
            product_id = int(input("Enter your product ID: "))
            delete_products(product_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
def inventory_transaction_operations():
    while True:
        print(
            """Inventory Transaction Operations:
1. Create Inventory Transaction
2. Read Inventory Transaction
3. Back to Main Menu"""
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            product_id = int(input("Enter your product ID: "))
            transaction_type = input("Enter your transaction type (IN/OUT): ")
            quantity = int(input("Enter your quantity: "))
            create_inventory_transactions(product_id, transaction_type, quantity)
        elif choice == "2":
            read_inventory_transactions()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    while True:
        print(
            """Main Menu:
1. Category Operations
2. Supplier Operations
3. Product Operations
4. Inventory Transaction Operations
5. Backup Database
6. Exit"""
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            category_operations()
        elif choice == "2":
            supplier_operations()
        elif choice == "3":
            product_operations()
        elif choice == "4":
            inventory_transaction_operations()
        elif choice == "5":
            backup()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")    


if __name__ == "__main__":
    main()