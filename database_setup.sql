-- 1. Create the Database
CREATE DATABASE OpsManager;
USE OpsManager;

-- 2. Create the Inventory Table
CREATE TABLE Inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    stock_level INT DEFAULT 0,
    unit_price DECIMAL(10, 2)
);

-- 3. Create the Logs Table (Where the 'Messy' data goes)
CREATE TABLE Operations_Log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    quantity_used INT,
    status VARCHAR(50), -- e.g., 'Pending', 'Cleaned', 'Error'
    entry_date VARCHAR(100), -- We use VARCHAR first to catch 'Messy' dates
    FOREIGN KEY (item_id) REFERENCES Inventory(item_id)
);