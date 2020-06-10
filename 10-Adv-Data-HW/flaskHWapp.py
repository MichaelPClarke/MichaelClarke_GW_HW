# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:32:05 2020

@author: 575684
"""
import numpy as np
import pandas as pd
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, MetaData, Table
Base = automap_base()
engine = create_engine("sqlite:///hawaii.sqlite")
Base.prepare(engine, reflect=True)
conn = engine.connect()

app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<Start><br/>"
        f"/api/v1.0/<start>/<end>"
    )
#%%
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    results = pd.read_sql('SELECT date,prcp FROM measurement', engine)

    results_json = list(np.ravel(results))

    return jsonify(results_json)

#%%
@app.route('/api/v1.0/stations')
def stations():

    results1 = pd.read_sql("Select distinct station from measurement", engine)

    results1_json = list(np.ravel(results1)) 

    return jsonify(results1_json)
#%%
@app.route('/api/v1.0/tobs')
def tobs_sql():

    results2 = pd.read_sql("Select tobs,count(*) from measurement where station = 'USC00519281' and date > '2016-08-23' group by tobs", engine)

    results2_json = list(np.ravel(results2))  

    return jsonify(results2_json)


#%%
if __name__ == '__main__':
    app.run(debug=True)
