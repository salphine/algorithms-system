# init_database.py
import sqlite3
import os

def init_database():
    """Initialize database with required tables"""
    # Delete existing database if exists
    if os.path.exists('sales_system.db'):
        os.remove('sales_system.db')
    
    conn = sqlite3.connect('sales_system.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        role TEXT NOT NULL DEFAULT 'user',
        is_active BOOLEAN NOT NULL DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        stock_quantity INTEGER NOT NULL,
        min_stock_level INTEGER NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create sales table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_id TEXT UNIQUE NOT NULL,
        customer_name TEXT,
        total_amount REAL NOT NULL,
        tax_amount REAL NOT NULL,
        payment_method TEXT NOT NULL,
        user_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    # Insert default admin user (password: admin123)
    admin_password = '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'  # SHA256 of 'admin123'
    cursor.execute('''
    INSERT OR IGNORE INTO users (username, password, role, is_active) 
    VALUES (?, ?, ?, ?)
    ''', ('admin', admin_password, 'admin', True))
    
    # Insert sample manager (password: manager123)
    manager_password = 'manager123_hash_here'  # You should hash this properly
    cursor.execute('''
    INSERT OR IGNORE INTO users (username, password, role, is_active) 
    VALUES (?, ?, ?, ?)
    ''', ('manager1', manager_password, 'manager', True))
    
    # Insert sample clerk (password: clerk123)
    clerk_password = 'clerk123_hash_here'  # You should hash this properly
    cursor.execute('''
    INSERT OR IGNORE INTO users (username, password, role, is_active) 
    VALUES (?, ?, ?, ?)
    ''', ('clerk1', clerk_password, 'clerk', True))
    
    # Insert sample products
    sample_products = [
        ('Coca Cola', 'Beverages', 50.0, 100, 20, 'Cold drink'),
        ('Fanta Orange', 'Beverages', 50.0, 80, 20, 'Orange flavored soda'),
        ('Sprite', 'Beverages', 50.0, 60, 15, 'Lemon-lime soda'),
        ('Chips', 'Snacks', 100.0, 50, 10, 'Potato chips'),
        ('Chocolate', 'Dessert', 150.0, 30, 5, 'Milk chocolate'),
        ('Burger', 'Food', 300.0, 40, 10, 'Beef burger'),
        ('Pizza', 'Food', 500.0, 25, 5, 'Cheese pizza'),
        ('Coffee', 'Beverages', 80.0, 200, 30, 'Hot coffee'),
        ('Tea', 'Beverages', 60.0, 150, 25, 'Hot tea'),
        ('Water', 'Beverages', 30.0, 300, 50, 'Bottled water'),
    ]
    
    cursor.executemany('''
    INSERT OR IGNORE INTO products (name, category, price, stock_quantity, min_stock_level, description)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_products)
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_database()