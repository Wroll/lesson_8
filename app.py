from flask import Flask, render_template, request
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


@app.route("/")
def admin_page():
    return render_template("admin_page.html")


@app.route("/admin", methods=['POST'])
def handler_product():
    status = 0
    mandatory_attributes = ['product_name', 'amount', 'price', 'product_category', 'description']
    print(request.form)
    if request.form['product_name'] and request.form['amount'] and request.form['price'] and request.form[
        'product_category'] and request.form['description']:
        if not check_products(request.form['product_name']):
            return "Product already exist"
        if check_category(request.form['product_category']):
            return f"Category {request.form['product_category']} not exist"
        try:  # kostil
            if request.form['in_sale'] == 'on':
                status = 1
        except:
            status = 1

        print(request.form['product_name'], request.form['amount'], request.form['price'],
              request.form['product_category'], request.form['description'], status)
        # add_new_product(request.form['product_name'], request.form['amount'], request.form['price'],
        #                 request.form['product_category'], request.form['description'], status)
        return "New product is added "
    else:
        attr = ", ".join(mandatory_attributes)
        return f"{attr} must be filled"


@app.route("/admin/new_category", methods=['POST'])
def handler_category():
    print(request.form['category_name'])
    if request.form['category_name']:
        if not check_category(request.form['category_name']):
            return "Category already exist"
            # add to base
        # add_new_category(request.form['category_name'])
        return "New category added"

    return f"Parametr new category name unfilled"


if __name__ == "__main__":
    app.run(debug=True)
