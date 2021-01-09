# from dash.react import dash

# my_app = Dash('my app')

# from dash_componentsw import h1, Plotly

# my_app.layout = h1('Hello World')

# my_app.server.run(debug=True)

# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('tri_2019_us.csv')
styrene  = df[(df['CHEMICAL'] == 'STYRENE')]


fig = px.density_mapbox(styrene, lat='LATITUDE', lon ='LONGITUDE', z='STACK AIR', radius=10,  hover_data=["FACILITY NAME", "STACK AIR", "UNIT OF MEASURE"],
                        center=dict(lat=0, lon=0), zoom=0,
                        labels={"STACK AIR": "Emissions (lbs)"},
                        mapbox_style="stamen-terrain")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)