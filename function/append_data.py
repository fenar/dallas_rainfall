#this module appends live Dallas Rainfall  data into BigQuery, there will be duplicates
#we will handle the duplicates over Datalab and save in to another BQ Table for presentation over Data Studio
#FENAR

from __future__ import print_function, absolute_import 
import pandas as pd 
from sodapy import Socrata
from google.datalab import Context 
import time
from datetime import datetime, timedelta
import logging 

logging.basicConfig(level=logging.DEBUG)

def run():
	client = Socrata("www.dallasopendata.com", None)
	results = client.get("xm9r-xkdu", limit=2000)
	results_df = pd.DataFrame.from_records(results)
        results_df.to_gbq('dallas.rainfall', 'fenar-bigdatadallas-demo', chunksize=None, verbose=True, if_exists='append')
