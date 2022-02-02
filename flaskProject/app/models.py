from pandas import DataFrame
from app.db import db


class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column("product_id", db.Integer, primary_key=True, autoincrement=True)
    product = db.Column("product", db.String(255))

    def insert_from_pd(product: DataFrame):
      product.to_sql("product", db.engine, if_exists="append", index=False)


class State(db.Model):
    __tablename__ = 'state'
    state_id = db.Column("state_id", db.Integer, primary_key=True, autoincrement=True)
    state = db.Column("state", db.String(255))
    state_abv = db.Column("state_abv", db.String(255))

    def insert_from_pd(state: DataFrame):
      state.to_sql("state", db.engine, if_exists="append", index=False)


class Month(db.Model):
    __tablename__ = 'month'
    month_id = db.Column("month_id", db.Integer, primary_key=True, autoincrement=True)
    month = db.Column("month", db.String(255))

    def insert_from_pd(month: DataFrame):
      month.to_sql("month", db.engine, if_exists="append", index=False)


class Color(db.Model):
    __tablename__ = 'color'
    color_id = db.Column("color_id", db.Integer, primary_key=True, autoincrement=True)
    color = db.Column("color", db.String(255))

    def insert_from_pd(color: DataFrame):
      color.to_sql("color", db.engine, if_exists="append", index=False)


class Amount(db.Model):
    __tablename__ = 'amount'
    amount_id = db.Column("amount_id", db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column("amount", db.Integer)
    product_id = db.Column("product_id", db.Integer, db.ForeignKey('product.product_id'))
    month_id = db.Column("month_id", db.Integer, db.ForeignKey('month.month_id'))
    color_id = db.Column("color_id", db.Integer, db.ForeignKey('color.color_id'))
    state_id = db.Column("state_id", db.Integer, db.ForeignKey('state.state_id'))

    def insert_from_pd(amount: DataFrame):
        amount.to_sql("amount", db.engine, if_exists="append", index=False)
