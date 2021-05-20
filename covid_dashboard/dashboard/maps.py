# File for creation of plotly maps(figs).
# You can use the plotly builtin fig.show() method to map locally.
import json
from urllib.request import urlopen

import plotly.graph_objs as go
from plotly.offline import plot

import pandas as pd

def usa_counties():
    """[summary]: Returns live cases of USA at county-level
    
    source:
        ³ nytimes
    Returns:
        [pd.DataFrame]
    """
    populations = pd.read_csv('https://raw.githubusercontent.com/balsama/us_counties_data/master/data/counties.csv')[['FIPS Code', 'Population', 'State']]
    populations.rename(columns={'FIPS Code': 'fips'}, inplace=True)
    populations.drop(populations.index[(populations["State"] == "New York")],axis=0,inplace=True)
    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv', dtype={"fips": str}).iloc[:,:6]
    df = pd.merge(df, populations, on='fips')
    df['cases/capita'] = (df.cases / df.Population)*100000 # per 100k residents

    return df


def usa_map():
    # Map of USA subdivided by FIPS-codes (counties), showing cases per-capita basis
    # Reference: https://plotly.com/python/reference/#choroplethmapbox
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    df = usa_counties()
    df.drop([2311], inplace=True)
    #print(df[2311])

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson = counties, 
            locations = df.fips,
            z = df['cases/capita'],
            marker_opacity = 0.75,
            marker_line_width = 0,
            colorscale = [
                [0, '#000000'],
                [(1/8)*1, '#FF0000'],
                [(1/8)*2, '#00FF00'],
                [(1/8)*3, '#0000FF'],
                [(1/8)*4, '#FFFF00'],
                [(1/8)*5, '#00FFFF'],
                [(1/8)*6, '#FF00FF'],
                [(1/8)*7, '#FF0000'],
                [1, '#FFFFFF']
            ]
        )
    )

    fig.update_layout(
        mapbox_style = 'carto-positron', 
        paper_bgcolor='rgba(0,0,0,0)', 
        mapbox_zoom=2.75, 
        mapbox_center = {'lat': 37.0902, 'lon': -95.7129}, 
        margin = dict(t=0, l=0, r=0, b=0)
    )
    plot_div = plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})

    return plot_div