from flask import Flask, render_template
from flask import request, jsonify
import sqlite3
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


# @app.route("/categories")
# def product_categories():
#     categories = [c for c in show_categories()]
#     return render_template("categories.html", categories=categories)

@app.route("/categories")
@app.route("/categories/<int:category_id>")
def product_categories(category_id=None):
    categories = [c for c in show_categories()]

    if category_id:
        print("1")
        products = []
        for id_ in show_id_categories():
            if id_ == category_id:
                products = [show_products_by_id(id_)]
        return render_template("products.html", products=products)
    print("2")
    return render_template("categories.html", categories=categories)


if __name__ == "__main__":
    app.run(debug=True)
