# File for creation of plotly maps(figs).
# You can use the plotly builtin fig.show() method to map locally.
from urllib.request import urlopen

import pandas as pd

def world_map_data():
	url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
	df = pd.read_csv(url)[['iso_code', 'location', 'population', 'total_cases', 'total_deaths']]

	df = df.drop_duplicates(subset=['iso_code'], keep='last') #Remove multiple data points

	#Grab global case number before removing
	global_cases = df.query("iso_code=='OWID_WRL'").total_cases.astype(int).apply('{:,}'.format).values[0]

	df = df[~df.iso_code.str.contains("OWID")] #Delete rows containing continent data

	df.dropna(subset = ['total_cases'], inplace=True) #Remove some broken countries

	df['total_cases'] = df['total_cases'].astype(int) #Convert to int to remove decimal
	#Make new column and format numbers with commas
	df['total_cases_text'] = df['total_cases'].apply('{:,}'.format)

	df['text'] = df['location'] + " " + df['total_cases_text']

	return [df,global_cases]

def left_table(data):
	data = data.sort_values(by='total_cases', ascending=False)
	return data[['location','total_cases_text','total_deaths','population']].to_numpy()
