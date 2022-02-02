import click
import pandas as pd
from flask.cli import with_appcontext
from consolemenu import SelectionMenu
from app.db import db
from app.models import Product, State, Month, Color, Amount
# from app.models import Books, Booktags, Tags,  Ratings, Goodreads_book, Toread
from app.helpers import (split_data_to_table, insert_fk)


@click.command("insert-db")
@with_appcontext
def insert_db():
    """Insère les données nécessaire à l'utilisation de l'application"""

    data = pd.read_csv("data/CSV_3.csv")

    product, state, month, color = split_data_to_table(data)
    Product.insert_from_pd(product)
    State.insert_from_pd(state)
    Month.insert_from_pd(month)
    Color.insert_from_pd(color)
    amount = insert_fk(data)
    Amount.insert_from_pd(amount)

    print("Données insérées !!")