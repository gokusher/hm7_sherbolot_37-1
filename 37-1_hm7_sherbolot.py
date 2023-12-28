import sqlite3


conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')
conn.commit()




def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    products = [
        ('iPhone 11 Pro', 600.0, 10),
        ('CocaCola', 60.0, 20),
        ('Aralash', 80.0, 15),
        ('Nive Men', 500.0, 25),
        ('Omega 3', 1200.0, 12),
        ('Protein Powder', 4000.0, 8),
        ('Gold Creatine', 3000.0, 18),
        ('Sony WH-1000XM4', 20000.0, 5),
        ('Victus 16 Gaming Laptop', 140000.0, 3),
        ('Nike Hoodie', 6000.0, 10),
        ('Kurut Lite', 35.0, 50),
        ('AWP', 4500.0, 15),
        ('Nike Air Max 97', 13000.0, 7),
    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()
    conn.close()


def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products


def get_products_below_price_limit_and_quantity_above_limit():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE price < 100.0 AND quantity > 5')
    selected_products = cursor.fetchall()
    conn.close()
    return selected_products


def search_products_by_title(title):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + title + '%',))
    matching_products = cursor.fetchall()
    conn.close()
    return matching_products


add_products()
print("\nAll products in the database:")
print(get_all_products())


update_quantity(1, 20)
update_price(2, 30.0)


delete_product(3)


selected_products = get_products_below_price_limit_and_quantity_above_limit()
print("\nProducts below price limit and quantity above limit:")
print(selected_products)


search_results = search_products_by_title('Nike')
print("\nSearch results for 'Nike':")
print(search_results)


conn.close()


