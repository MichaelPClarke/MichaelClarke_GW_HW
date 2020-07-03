# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:32:05 2020

@author: 575684
"""
import numpy as np
import pandas as pd
from flask import Flask, jsonify
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, MetaData, Table

Base = automap_base()

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base.prepare(engine, reflect=True)

conn=engine.connect()

measurement = Base.classes.measurement
station = Base.classes.station


session = Session(engine)

app = Flask(__name__)

#%%


@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )
#%%
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session.query(measurement.date).order_by(measurement.date.desc()).first()
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    df = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date > query_date).all()

    results_json = list(np.ravel(df))

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
@app.route('/api/v1.0/start')
def maxminavg():
    
    results3 = pd.read_sql("Select max(tobs), min(tobs), avg(tobs) from measurement where date > '2016-08-23'", engine)
    
    results3_json = list(np.ravel(results3))
    
    return jsonify(results3_json)


#%%
@app.route('/api/v1.0/start/end')
def maxminavg2():
    
    results4 = pd.read_sql("Select max(tobs), min(tobs), avg(tobs) from measurement where date between '2016-08-23' and '2017-08-24'", engine)
    
    results4_json = list(np.ravel(results4))
    
    return jsonify(results4_json)
#%%
if __name__ == '__main__':
    app.run(debug=True)
