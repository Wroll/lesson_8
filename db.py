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
            SELECT categories.category_name FROM categories
            """)
        for c in result:
            categories.append(*c)
    return categories


def show_products_by_id_category(id_category):
    products_by_category = []
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT my_products.product_name FROM my_products
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
            WHERE my_products.product_name = ? AND my_products.status =1 
            """, [product_name])
        for c in result:
            products_id.append(*c)
    return products_id


def check_products(product_name):
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT my_products.product_name FROM my_products
            WHERE my_products.product_name = ? 
            """, [product_name])
        r = [i for i in result]
        if len(r) == 0:
            return True
        else:
            return False


def check_category(category_name):
    with DatabaseManager('products.db') as db:
        result = db.execute("""
            SELECT categories.category_name FROM categories
            WHERE categories.category_name = ? 
            """, [category_name])
        r = [i for i in result]
        if len(r) == 0:
            return True
        else:
            return False


def add_new_product(product_name_, amount, price, product_category, description, status):
    c = sqlite3.connect('products.db')
    c.cursor()
    c.execute("""
         INSERT INTO my_products (product_name, amount, price, id_category, description, status)
         VALUES (?,?,?,(SELECT categories.id
         FROM categories WHERE categories.category_name = ?),?,?)
        """, [product_name_, amount, price, product_category, description, status])
    c.commit()
    c.close()


def add_new_category(new_category_name):
    c = sqlite3.connect('products.db')
    c.cursor()
    c.execute("""
            INSERT INTO categories (category_name)
            VALUES (?)
           """, [new_category_name])
    c.commit()
    c.close()


# add_new_product("iphone", 2, 100,
#                 "phones", "cool phone", 1)

# print(check_category("phones"))
