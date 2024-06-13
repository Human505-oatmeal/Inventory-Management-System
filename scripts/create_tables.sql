CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);
CREATE TABLE Suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    category_id INT NOT NULL,
    supplier_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(9,2),
    FOREIGN KEY (category_id) REFERENCES Categories(id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(id)
);
CREATE TABLE Inventory_Transactions (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    transaction_type VARCHAR NOT NULL,
    quantity INT NOT NULL,
    transaction_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (product_id) REFERENCES Products(id)
);