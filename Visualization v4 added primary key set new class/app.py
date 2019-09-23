# import necessary libraries
from sqlalchemy import func
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data.sqlite"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Calls(db.Model):
    __tablename__ = 'allcalls'

    id = db.Column(db.Integer, primary_key=True)
    Strike = db.Column(db.String(64))
    Last_Price = db.Column(db.Float)
    Implied_Volatility = db.Column(db.Float)
    Ticker = db.Column(db.String)

    def __repr__(self):
        return '<Calls %r>' % (self.name)

# class Puts(db.Model):
#     __tablename__ = 'puts'

#     Contract = db.Column(db.String, primary_key=True)
#     Ticker = db.Column(db.String)
#     Last_Price = db.Column(db.Float)
#     Strike = db.Column(db.Float)
#     Implied_Volatility = db.Column(db.Float)

#     def __repr__(self):
#         return '<Puts %r>' % (self.name)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


@app.route("/")
def home():
     return"""Welcome!"""
     return render_template("index.html")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# calls_table = Base.classes.All_calls



# @app.route("/tickers")
# def tickers():
#     """Return a list of tickers names."""

#     # Use Pandas to perform the sql query
#     # stmt = db.session.query(calls_data).statement
#     # df = pd.read_sql_query(stmt, db.session.bind) ???
   
#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])


# Query the database and return the jsonified results
@app.route("/calls")
def calls():
    sel = [
        
    # Calls_data.Ticker,
    # Calls_data.Last_Price,
    allcalls.Strike,
    allcalls.Implied_Volatility
    ]

    results = db.session.query(*sel).all()
    df = pd.DataFrame(results, columns=["Strike","Implied_Volatility"])   
    # df = pd.DataFrame(results, columns=["Ticker", "Strike","Last_price","Implied_Volatility"])
    return jsonify(df.to_dict(orient="records"))

# @app.route("/puts")
# def puts_data():
#     sel = [
#     Puts_data.Ticker,
#     Puts_data.Last_Price,
#     Puts_data.Strike,
#     Puts_data.Implied_Volatility
#     ]

#     results = db.session.query(*sel).all()
       
#     df = pd.DataFrame(results, columns=["Ticker", "Strike","Last_price","Implied_Volatility"])
#     return jsonify(df.to_dict(orient="records"))

# @app.route("/pricehistory")
# def historydata():
#     sel = [
#     # To put more

#     ]


if __name__ == "__main__":
    app.run(debug=True)
