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

# app = dash.Dash(
#     __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
# )
server = app.server
df = pd.read_csv('tri_2019_us.csv')
available_indicators = df['CHEMICAL'].unique()
px.set_mapbox_access_token('pk.eyJ1IjoibGl0aGl1bXJvYm90IiwiYSI6ImNranUyNGQyMjcweDgyeXA5cHkxdnJ2Z2wifQ.cxBUPa2rO27ZF-qacR8XbQ')


# fig = px.density_mapbox()

# fig.update_layout(
#     margin=dict(l=20, r=20, t=20, b=20),
#     paper_bgcolor="LightSteelBlue",)




# config = {
#   'toImageButtonOptions': {
#     'format': 'svg', # one of png, svg, jpeg, webp
#     'filename': 'custom_image',
#     'height': 500,
#     'width': 700,
#     'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
#   }
# }




app.title = 'Chemical Emissions - United States' 


### BLUE ONE
#########################################################################

# Layout of Dash App
app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                # Column for user controls
                html.Div(
                    className="four columns div-user-controls",
                    children=[
                        # html.Img(
                        #     className="logo", src=app.get_asset_url("dash-logo-new.png")
                        # ),
                        html.H1(["STACK CHEMICAL AIR EMISSIONS "]),
                        html.H2(["United States Industrial Facilities"]),
                        html.H3(["Year - 2019"]),

                        html.P(
                            """Select a chemical using the dropdown menu below. 
                            The resulting Choropleth map will display the related data from each industrial facility emitting the specified chemical. Zoom in and interact with the map to learn more about each facility."""
                        ),

                        html.Div(
                            className="div-for-dropdown",
                            children=[
                               dcc.Dropdown(
											id='selected_chemical',
											value = 'STYRENE',
											options=[{'label': i, 'value': i} for i in available_indicators])
                            ],
                        ),


 
                    ],
                ),
                # Column for app graphs and plots
                html.Div( 
                    className="eight columns div-for-charts bg-grey",
                    children=[

        	            html.Div(
        	                className="div-for-charts0",
        	                children=[
        	                    dcc.Graph(
                                    id='graphic',
                                    config={
                                        'responsive': True,
                                        # 'fillFrame': True,
                                        'autosizable': True,  

                                    }




                                    # figure={
                                    #     'layout':{
                                    #         'autosize': True,
                                    #         'margin': {'autoexpand':True}
                                    #         # 'title':'test',
                                    #         # 'margin': {
                                    #         #     'l': 200,
                                    #         #     'b': 20,
                                    #         #     'r': 10,
                                    #         #     't': 60
                                    #         # }
                                    #         # 'width':100

                                            

                                    #     }
                                    # }
                                      
                                 )

        	                ]
        	            )
                    ],
                ),
            ]
        )
    ]
)



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
        zoom=2,
        # width=1000,
        labels={"STACK AIR":unit_spec},
        mapbox_style="satellite-streets",
        # layout=''
        # config={'responsive': True,
        #         'fillFrame': True,
        #         'autosizable': True,  
        #          }


    )
  
	return fig

if __name__ == "__main__":
    app.run_server(debug=True)




#############################################################################



















# app.layout = dbc.Container ([
# 	dbc.Row([
# 		dbc.Col(html.H1("Stack Emmisions [U.S.A]",
# 			className='text-center mb-4'), 
# 			width=12
# 		)
# 	]),

# 	dbc.Row([
# 		dbc.Col([
# 			dcc.Dropdown(
# 				id='selected_chemical',
# 				value = 'STYRENE',
# 				options=[{'label': i, 'value': i} for i in available_indicators]),
		
# 			dcc.Graph(
# 				id='graphic',
				
# 			)
# 		],width = {'size':12} ),
		
# 	],justify='center')

# ], fluid=False,)





# @app.callback(dash.dependencies.Output("graphic","figure"),
# 	[dash.dependencies.Input("selected_chemical","value")])


# def update_graph(input_value):

# 	dff = df[df['CHEMICAL'] == input_value]
# 	unit = dff['UNIT OF MEASURE'].unique()
# 	unit_spec = str(unit[0])


# 	fig = px.density_mapbox(dff, 
# 		lat='LATITUDE', 
# 		lon ='LONGITUDE', 
# 		z='STACK AIR', radius=10,  
# 		hover_data=["FACILITY NAME"],
# #                         center=dict(lat=0, lon=0), 

#         zoom=2,

#                         # animation_frame="CHEMICAL",
#         labels={"STACK AIR":unit_spec},
#                         # template = 'plotly_dark',
#         mapbox_style="satellite-streets"

#     )

# 	return fig




# if __name__ == '__main__':
#     app.run_server(debug=True)