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


app.layout = html.Div([
	html.Div([
		html.Div([
		    # html.Label('Chemicals'),
			dcc.Dropdown(
			id='selected_chemical',
			value = 'STYRENE',
			options=[{'label': i, 'value': i} for i in available_indicators])
		])
	]),

	dcc.Graph(id='graphic')


])



@app.callback(dash.dependencies.Output("graphic","figure"),
	[dash.dependencies.Input("selected_chemical","value")])


def update_graph(input_value):

	dff = df[df['CHEMICAL'] == input_value]



	fig = px.density_mapbox(dff, lat='LATITUDE', lon ='LONGITUDE', z='STACK AIR', radius=10,  hover_data=["FACILITY NAME", "STACK AIR", "UNIT OF MEASURE"],
#                         center=dict(lat=0, lon=0), 
                        zoom=2,
                        # animation_frame="CHEMICAL",
                        labels={"STACK AIR": "Emissions (lbs)"},
                        mapbox_style="stamen-terrain")


	return fig




if __name__ == '__main__':
    app.run_server(debug=True)