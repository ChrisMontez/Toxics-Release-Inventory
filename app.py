import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
	meta_tags=[{'name': 'viewport',
				'content': 'width=device-width, initial-scale=1.0'}])

server = app.server
df = pd.read_csv('tri_2019_us.csv')
available_indicators = df['CHEMICAL'].unique()

px.set_mapbox_access_token('pk.eyJ1IjoibGl0aGl1bXJvYm90IiwiYSI6ImNranUyNGQyMjcweDgyeXA5cHkxdnJ2Z2wifQ.cxBUPa2rO27ZF-qacR8XbQ')


app.layout = dbc.Container ([
	dbc.Row([
		dbc.Col(html.H1("Stack Emmisions [U.S.A]",
			className='text-center  mb-4'), 
			width=12
		)
	]),

	dbc.Row([
		dbc.Col([
			dcc.Dropdown(
				id='selected_chemical',
				value = 'STYRENE',
				options=[{'label': i, 'value': i} for i in available_indicators]),
		
			dcc.Graph(
				id='graphic',
				
			)
		],width = {'size':12} ),
		
	],justify='center')
], fluid=False,)





@app.callback(dash.dependencies.Output("graphic","figure"),
	[dash.dependencies.Input("selected_chemical","value")])


def update_graph(input_value):

	dff = df[df['CHEMICAL'] == input_value]
	unit = dff['UNIT OF MEASURE'].unique()
	unit_spec = str(unit[0])


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
        mapbox_style="satellite-streets"

    )

	return fig




if __name__ == '__main__':
    app.run_server(debug=True)