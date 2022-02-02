import pandas as pd
import re
from app.db import db


def split_data_to_table(data: pd.DataFrame):
    products = data['Products'].unique()
    product = pd.DataFrame(products)
    product.columns = ['Product']

    states = data['Locations'].unique()
    state = pd.DataFrame(states)
    state.columns = ['State']
    state['state_abv'] = ""

    dict_state_abv = {
        'Illinois': 'IL',
        'New York': 'NY',
        'Pennsylvania': 'PA',
        'New Jersey': 'NJ',
        'Alabama': 'AL',
        'North Carolina': 'NC',
        'Alaska': 'AK',
        'Montana': 'MT',
        'Colorado': 'CO',
        'Idaho': 'ID',
        'Arizona': 'AZ',
        'Iowa': 'IA',
        'Arkansas': 'AR',
        'Washington': 'WA',
        'Mississippi': 'MS',
        'Indiana': 'IN',
        'Kentucky': 'KY',
        'Florida': 'FL',
        'Connecticut': 'CT',
        'Michigan': 'MI',
        'Utah': 'UT',
        'Virginia': 'VA',
        'California': 'CA',
        'Minnesota': 'MN',
        'Vermont': 'VT',
        'Delaware': 'DE',
        'Hawaii': 'HI',
        'Texas': 'TX',
        'South Carolina': 'SC',
        'Ohio': 'OH',
        'Oregon': 'OR',
        'Louisiana': 'LA',
        'Maryland': 'MD',
        'Massachussets': 'MA',
        'Georgia': 'GA',
        'North Dakota': 'ND',
        'Kansas': 'KS',
        'New Mexico': 'NM',
        'Wyoming': 'WY',
        'Wisconsin': 'WI',
        'Oklahoma': 'OK',
        'New Hampshire': 'NH',
        'Nevada': 'NV',
        'Missouri': 'MO',
        'Nebraska': 'NE',
        'Rhode Island': 'RI',
        'Tennessee': 'TN',
        'Maine': 'ME',
        'West Virginia': 'WV',
        'South Dakota': 'SD'
    }
    for key, valeur in dict_state_abv.items():
        for i in range(len(state['State'])):
            if state['State'][i] == key:
                state['state_abv'][i] = valeur

    months = data['Expiration Date']

    for month in months:
        r = re.findall(r"\d+", month)
        if r :
            data['Expiration Date'] = data['Expiration Date'].apply(lambda x: x.replace(r[0], ''))

    month = data['Expiration Date'].unique()
    month = pd.DataFrame(month, columns=['month'])

    color = data['packaging'].unique()
    color = pd.DataFrame(color, columns=['color'])

    return product, state, month, color


def insert_fk(data):
    state = pd.read_sql('SELECT * FROM state', db.engine)
    month = pd.read_sql('SELECT * FROM month', db.engine)
    color = pd.read_sql('SELECT * FROM color', db.engine)
    product = pd.read_sql('SELECT * FROM product', db.engine)

    state_dict = {}
    month_dict = {}
    color_dict = {}
    product_dict = {}
    for i in range(len(state)):
        state_dict[state['state'][i]] = state['state_id'][i]

    for i in range(len(month)):
        month_dict[month['month'][i]] = month['month_id'][i]

    for i in range(len(color)):
        color_dict[color['color'][i]] = color['color_id'][i]

    for i in range(len(product)):
        product_dict[product['product'][i]] = product['product_id'][i]

    for key, valeur in state_dict.items():
        # data['Locations'] = data['Locations'].apply(lambda x: x.replace(key, str(valeur)))
        for i in range(len(data['Locations'])):
            if data['Locations'][i] == key:
                data['Locations'][i] = valeur

    for key, valeur in month_dict.items():
        data['Expiration Date'] = data['Expiration Date'].apply(lambda x: x.replace(key, str(valeur)))

    for key, valeur in color_dict.items():
        for i in range(len(data['packaging'])):
            if data['packaging'][i] == key:
                data['packaging'][i] = valeur

    for key, valeur in product_dict.items():
        data['Products'] = data['Products'].apply(lambda x: x.replace(key, str(valeur)))

    data = data.rename(columns={
        'Locations': 'state_id',
        'Expiration Date': 'month_id',
        'packaging': 'color_id',
        'Products': 'product_id'
                                })
    del data['ID']
    amount = data
    return amount
