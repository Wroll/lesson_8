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
        pass


def show_categories():
    categories = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT category.category_name FROM category
            """)
        for c in result:
            categories.append(*c)
    return categories


def show_products_by_id(id_category):
    products_by_category = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT all_products.product_name FROM all_products
            WHERE all_products.id_category = ?
            """, [id_category])
        for c in result:
            products_by_category.append(*c)
    return products_by_category


def show_id_categories():
    id_categories = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT category.id_category FROM category
            """)
        for c in result:
            id_categories.append(*c)
    return id_categories


print(show_id_categories())
print(show_products_by_id(1))