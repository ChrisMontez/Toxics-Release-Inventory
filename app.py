import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Load Data
df = pd.read_csv('tri_2019_us.csv')

available_indicators = df['CHEMICAL'].unique()

#Display
# fig = px.density_mapbox(df, lat='LATITUDE', lon ='LONGITUDE', z='STACK AIR', radius=10,  hover_data=["FACILITY NAME", "STACK AIR", "UNIT OF MEASURE"],
# #                         center=dict(lat=0, lon=0), 
#                         zoom=2,
#                         # animation_frame="CHEMICAL",
#                         labels={"STACK AIR": "Emissions (lbs)"},
#                         mapbox_style="stamen-terrain")


# app.layout = html.Div(children=[
#     html.H1(children='Testing One Two Three'),
#     html.Div(children='''
#         test test test.
#     '''),
#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

app.layout = html.Div([
	html.Div([
	    html.Label('Chemicals'),
		dcc.Dropdown(
		id='chemical',
		options=[{'label': i, 'value': i} for i in available_indicators],
		value='STYRENE'
		),
		dcc.Graph(id='indicator-graphic')
	])

])

# app.callback(
# 	 Output('indicator-graphic', 'figure'),
# 	 Input('chemical', 'value')
# 	 )


#     Output('example-graph', 'figure'),
#     Input('chemical', 'value'))

# def update_graph(chemical_name, chemical_value):

# 	dff = df[df['CHEMICAL'] == chemical_value]

# 	fig = px.density_mapbox(df, 
# 		lat=dff[dff['Indicator Name'] == chemical_name]['LATITUDE'], 
# 		lon=dff[dff['Indicator Name'] == chemical_name]['LONGITUDE'], 
# 		z=dff[dff['Indicator Name'] == chemical_name]['STACK AIR'], 
# 		radius=10,  
# 		hover_data=["FACILITY NAME", "STACK AIR", "UNIT OF MEASURE"],
# 	    zoom=2,
# 	    labels={"STACK AIR": "Emissions (lbs)"},
# 	    mapbox_style="stamen-terrain"
# 	 )

# 	return fig




if __name__ == '__main__':
    app.run_server(debug=True)