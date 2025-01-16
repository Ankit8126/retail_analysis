# Intelligent Retail Analytics System

##  Tables and Relationships

- users Table
``` sql 
-----------
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    phone_number number(10) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'retailer') DEFAULT 'retailer',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

- categories Table
```sql 
------
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);
```

- products Table
``` sql 
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL, -- Selling price
    cost_price DECIMAL(10, 2) NOT NULL, -- Cost price for profit calculation
    stock INT DEFAULT 0, -- Current stock level
    category_id INT REFERENCES categories(category_id) ON DELETE SET NULL,
    sku VARCHAR(50) UNIQUE NOT NULL, -- Unique SKU for each product
    image VARCHAR(255), -- Image URL for the product
    status VARCHAR(50) DEFAULT 'active', -- Active or inactive status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- CHECK (price > 0), -- Ensure valid price
    -- CHECK (cost_price > 0), -- Ensure valid cost price
    -- CHECK (stock >= 0) -- Ensure non-negative stock
);


```
3. daily_sales Table
- Purpose: Daily sales ka record rakhne ke liye. Har din kitna maal bika aur uska total revenue.
``` sql
CREATE TABLE daily_sales (
    sale_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
    date DATE DEFAULT CURRENT_DATE,
    quantity_sold INT NOT NULL,
    total_sale_value DECIMAL(10, 2) NOT NULL, -- quantity_sold * price
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

- stock_adjustments Table
- Purpose: Stock me manual changes ka track rakhne ke liye, jaise naya stock aana ya damage ki wajah se reduction.
``` sql 
CREATE TABLE stock_adjustments (
    adjustment_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
    adjustment_type ENUM('addition', 'reduction') NOT NULL,
    quantity INT NOT NULL,
    reason TEXT,
    adjusted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

- sales_forecast Table
- Purpose: Future me demand forecasting ke liye AI/ML predictions store karna.
``` sql 
 CREATE TABLE sales_forecast (
    forecast_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
    forecast_date DATE NOT NULL,
    predicted_demand INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```