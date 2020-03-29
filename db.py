import sqlite3


class DatabaseManager:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, *args):
        self.cursor.close()


def show_categories():
    categories = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT categories.name FROM categories
            """)
        for c in result:
            categories.append(*c)
    return categories


def show_products_by_id_category(id_category):
    products_by_category = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT my_products.name FROM my_products
            WHERE my_products.id_category = ? AND my_products.status = 1
            """, [id_category])
        for c in result:
            products_by_category.append(*c)
    return products_by_category


def show_id_categories():
    id_categories = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT categories.id FROM categories
            """)
        for c in result:
            id_categories.append(*c)
    return id_categories


def show_products_by_id(id_product):
    products = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT my_products.amount, my_products.price,
            my_products.description
            FROM my_products
            WHERE my_products.id = ? AND my_products.status = 1
            """, [id_product])
        for i in result:
            for k in i:
                products.append(k)
    return products


def show_products_id_by_product_name(product_name):
    products_id = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT my_products.id FROM my_products
            WHERE my_products.name = ? AND my_products.status =1 
            """, [product_name])
        for c in result:
            products_id.append(*c)
    return products_id
