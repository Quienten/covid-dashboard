from urllib.request import urlopen
import json

import plotly.graph_objs as go
from plotly.offline import plot

def world_map(data):
	with urlopen('https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json') as response:
		world_countries = json.load(response)

	figure = go.Figure(
		go.Choroplethmapbox(
			geojson = world_countries, 
			locations = data.iso_code,
			z = data.total_cases,
			marker_opacity = 0.75,
			marker_line_width = 0,
            colorbar_title = 'Total Cases',
			colorscale='Viridis',
            text=data['text'], # hover text
            hoverinfo='text'
		)
	)

	figure.update_layout(
		mapbox_style = 'carto-positron', 
		paper_bgcolor='rgba(0,0,0,0)', 
		mapbox_zoom=2.75, 
		mapbox_center = {'lat': 37.0902, 'lon': -95.7129}, 
		margin = dict(t=0, l=0, r=0, b=0)
	)

	# Update plot sizing
	figure.update_layout(
		width=1000,
		height=600,
		autosize=True,
		margin=dict(t=100, b=0, l=0, r=0),
	)

	# Update 3D scene options
	figure.update_scenes(
		aspectratio=dict(x=1, y=1, z=0.7),
		aspectmode="manual"
	)

	# Add dropdowns
	button_layer_1_height = 1.10
	figure.update_layout(
		updatemenus=[
			dict(
				buttons=list([
					dict(
						args=["colorscale", "Viridis"],
						label="Viridis",
						method="restyle"
					),
					dict(
						args=["colorscale", "Cividis"],
						label="Cividis",
						method="restyle"
					),
					dict(
						args=["colorscale", "Blues"],
						label="Blues",
						method="restyle"
					),
					dict(
						args=["colorscale", "Greens"],
						label="Greens",
						method="restyle"
					),
				]),
				direction="down",
				pad={"r": 10, "t": 10},
				showactive=True,
				x=0.09,
				xanchor="left",
				y=button_layer_1_height,
				yanchor="top"
			),
			dict(
				buttons=list([
					dict(
						args=["reversescale", False],
						label="False",
						method="restyle"
					),
					dict(
						args=["reversescale", True],
						label="True",
						method="restyle"
					)
				]),
				direction="down",
				pad={"r": 10, "t": 10},
				showactive=True,
				x=0.35,
				xanchor="left",
				y=button_layer_1_height,
				yanchor="top"
			)
		]
	)

	figure.update_layout(
    annotations=[
        dict(text="Colorscale:", x=0, xref="paper", y=1.07, yref="paper",
                             align="left", showarrow=False),
        dict(text="Reverse Colorscale:", x=0.2, xref="paper", y=1.07,
                             yref="paper", showarrow=False)
    ])

	world_map_html = plot(figure, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
	#world_map_html = figure.to_html(full_html=False, default_width=2000, default_height=720)

	return world_map_html