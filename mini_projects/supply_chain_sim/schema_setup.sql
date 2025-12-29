-- FILE: mini_projects/supply_chain_sim/schema_setup.sql

-- 1. Master Data: Products
-- Stores static information about items.
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    sku VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100),
    category VARCHAR(50),
    price_eur DECIMAL(10, 2)
);

-- 2. Transactional Data: Inventory Movements
-- Logs every single movement (Inbound/Outbound)
CREATE TABLE IF NOT EXISTS inventory_movements (
    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    movement_type VARCHAR(10) CHECK(movement_type IN ('INBOUND', 'OUTBOUND', 'RETURN')),
    quantity INTEGER NOT NULL,
    movement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    warehouse_zone VARCHAR(20),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);