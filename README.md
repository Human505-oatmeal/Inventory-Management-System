# Inventory Management System

## Overview
This inventory management system is built with Python and PostgreSQL for efficient inventory tracking and management. This system allows users to add, update, delete and view inventory items, and also implements backup functionality via the CLI.

## Features
- Add, update, delete, and read inventory items
- Database backup

## Table of Contents
1. [Installation](#installation)
2. [Database Schema](#database-schema)
3. [Contributing](#contributing)
4. [License](#license)

## Installation

## Prerequisites
- Python 3.x
- PostgreSQL
- Git

### Step-by-step installation

1. **Clone the repository**
```bash
git clone https://github.com/Human505-oatmeal/Inventory-Management-System.git
cd Inventory-Management-System
```

2. **Create and activate the virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Required Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up PostgreSQL**
- Create a new PostgreSQL database
- Update database configuration in `config.py`

5. **Run the application**
```bash
python app.py
```

## Database Schema

### Tables

**Categories**


Column | Type | Description
-------|------|------------
id | SERIAL | PRIMARY KEY
name | VARCHAR | Category name

**Suppliers**


Column | Type | Description
-------|------|------------
id | SERIAL | PRIMARY KEY
name | VARCHAR | Supplier name

**Products**

Column | Type | Description
-------|------|------------
id | SERIAL | PRIMARY KEY
name | VARCHAR | Product name
category_id | INT | The category_id that the product is associated with
supplier_id | INT | The supplier_id that the product is associated with
quantity | INT | The quantity of the product
price | DECIMAL(9,2) | The price of the product

**Inventory_Transactions**


Column | Type | Description
-------|------|------------
id | SERIAL | Primary Key
product_id | INT | The product id relating to the products table
transaction_type | VARCHAR | The type of transaction
quantity | INT | The quantity
transaction_date | DATE | Gets the current date, however you don't need to worry about this since the system does it for you.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes. I'm a bit new to Github so please be patient, I will do my best!

## License

See LICENSE file.
