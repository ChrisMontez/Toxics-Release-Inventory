import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Load Data
df = pd.read_csv('tri_2019_us.csv')

available_indicators = df['CHEMICAL'].unique()


app.layout = html.Div([
	dcc.Graph(id='graphic', style={'width': '100%', 'float': 'right', 'display': 'inline-block'}),

	html.Div([
		html.P('Choose a chemical to display on the map'),
		html.Div([
		    # html.Label('Chemicals'),
			dcc.Dropdown(
			id='selected_chemical',
			value = 'STYRENE',
			options=[{'label': i, 'value': i} for i in available_indicators])
		])
	],style={'width': '55%','margin': '0 auto'}),

	


], style={'width': '75%','margin': '0 auto'})



@app.callback(dash.dependencies.Output("graphic","figure"),
	[dash.dependencies.Input("selected_chemical","value")])


def update_graph(input_value):

	dff = df[df['CHEMICAL'] == input_value]
	unit = dff['UNIT OF MEASURE'].unique()
	unit_spec = str(unit[0])
	# unit = 'test'



	fig = px.density_mapbox(dff, 
		lat='LATITUDE', 
		lon ='LONGITUDE', 
		z='STACK AIR', radius=10,  
		hover_data=["FACILITY NAME"],
#                         center=dict(lat=0, lon=0), 
        zoom=2,

                        # animation_frame="CHEMICAL",
        labels={"STACK AIR":unit_spec},
                        # template = 'plotly_dark',
        mapbox_style="carto-darkmatter")






	return fig




if __name__ == '__main__':
    app.run_server(debug=True)