from flask import Flask, render_template
from db import *

"""
1) Создать базу данных товаров, у товара есть: Категория (связанная
таблица), название, есть ли товар в продаже или на складе, цена, кол-во
единиц.Создать html страницу. На первой странице выводить ссылки на все
категории, при переходе на категорию получать список всех товаров в
наличии ссылками, при клике на товар выводить его цену, полное описание и
кол-во единиц в наличии.
2) Создать страницу для администратора, через которую он может добавлять
новые товары и категории.
"""

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"

# 1
@app.route("/categories")
@app.route("/categories/<int:category_id>")
@app.route("/categories/product/<int:product_id>")
def product_categories(category_id=None, product_id=None):
    categories = [c for c in show_categories()]
    id_categories = [i for i in show_id_categories()]
    categories_with_id = list(zip(categories, id_categories))
    if category_id:
        products_by_categories = show_products_by_id_category(category_id)
        id_products = [show_products_id_by_product_name(p)[0] for p in products_by_categories]
        products_by_id = list(zip(id_products, products_by_categories))
        return render_template("products.html", products_by_id=products_by_id)
    if product_id:
        description = show_products_by_id(product_id)
        product_description = {description[0]: "Number of items on sale : ",
                               description[1]: "Price ($) : ",
                               description[2]: "Short Description : "}
        return render_template("product_description.html", product_description=product_description)
    return render_template("categories.html", categories=categories_with_id)


if __name__ == "__main__":
    app.run(debug=True)
