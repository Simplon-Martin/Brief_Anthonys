from flask import Blueprint, render_template, request
from app.db import db
# from app.helpers import (reco_by_user_id, filter_by_gender, filter_by_most_recent_gender, get_by_id, filter_content_base_by_author)
import pandas as pd

main_controllers = Blueprint("main", __name__, url_prefix="/")


@main_controllers.route("/", methods=['GET', 'POST'])
def test():
    products = pd.read_sql_query('SELECT * FROM product', db.engine, )
    states = pd.read_sql_query('SELECT * FROM state', db.engine, )
    # return render_template('test.html', books_1=books_1)
    return render_template('index.html', products=products, states=states)


@main_controllers.route("/visualisation", methods=['GET', 'POST'])
def visualisation():

    product_id = request.form.get('select_product')
    product = pd.read_sql('SELECT product FROM `product` WHERE product.product_id =' + product_id, db.engine)
    product = product.to_dict()
    product = product['product'][0]


    state_id = request.form.get('select_state')
    print(type(state_id))
    if state_id != '' :
        print('normalement pas None')
        state = pd.read_sql('SELECT state FROM `state` WHERE state.state_id =' + state_id, db.engine)
        state = state.to_dict()
        state = state['state'][0]


    if product_id is not None and state_id == '':
        twice = False
        info_by_product_id = pd.read_sql('SELECT * FROM amount join product on amount.product_id = product.product_id join state on amount.state_id = state.state_id join month on amount.month_id = month.month_id join color on amount.color_id = color.color_id WHERE product.product_id =' + product_id ,
                                         db.engine)
        info_by_product_id = info_by_product_id.drop_duplicates(subset=['state'])
        states_by_product_abv = info_by_product_id
        return render_template('visualisation.html',
                               states_abv=states_by_product_abv, product=product, twice=twice)
    elif product_id is not None and state_id != '' :
        twice = True
        info_by_product_id_and_state = pd.read_sql(
            'SELECT * FROM amount join product on amount.product_id = product.product_id join state on amount.state_id = state.state_id join month on amount.month_id = month.month_id join color on amount.color_id = color.color_id WHERE product.product_id = ' + product_id + ' and state.state_id = ' + state_id,
            db.engine)
        states_by_product_abv = info_by_product_id_and_state
        return render_template('visualisation.html',
                             states_abv=states_by_product_abv, product=product, state=state, twice=twice);

    return 'ok'



