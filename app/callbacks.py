from app import app

from dash.dependencies import Input, Output, State

from plotly import tools
import plotly.express as px

import pandas as pd

import functions as funcs
from components import (BASIC_STATS, TYPES, 
						GENS, DATA, BASE_COLS, 
						SIZE_COLS, RATES)



##### Stats Analysis callbacks #####

@app.callback(
	[Output('datatable-stat-analysis', 'data'),
	Output('datatable-stat-analysis', 'columns')],
    [Input('restore-cols', 'n_clicks')])
def update_table(n_clicks):
	columns = [{"name": i, "id": i, 'deletable': True} for 
                									i in DATA.columns.values[:-4]]
	return DATA.to_dict('records'), columns

@app.callback(
   Output('stats-analysis-scatter', 'figure'),
   [Input('dropdown-basic-stat', 'value'),
   Input('dropdown-type', 'value'),
   Input('dropdown-generation', 'value'),
   Input('radio-HPCP', 'value')])
def update_stats_scatter(stats_value, types_value, 
	gens_value, HPCP_value):
	stats = BASIC_STATS if stats_value == 'All' else [stats_value]
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]
	yaxis = HPCP_value

	fig = funcs.update_stats_scatter(stats, types, generations, yaxis)
	
	return fig

@app.callback(
   Output('stats-analysis-box', 'figure'),
   [Input('dropdown-basic-stat', 'value'),
   Input('radio-boxoptions', 'value'),
   Input('radio-boxplot', 'value')])
def update_stats_boxplot(stats_value, columns, xaxis):
	if columns == 'Stats':
		stats = BASIC_STATS if stats_value == 'All' else [stats_value]
	elif columns == 'Height & Weight':
		stats = SIZE_COLS
	else:
		stats = RATES

	fig = funcs.update_stats_boxplots(stats, xaxis)
	
	return fig

@app.callback(
   Output('stats-heatmap', 'figure'),
   [Input('radio-scale', 'value')])
def update_stats_heatmap(col_scale):
	fig = funcs.update_stats_heatmap(col_scale)
	
	return fig



##### Top Pokemon callbacks #####

@app.callback(
   Output('highest-attack-img', 'src'),
   [Input('dropdown-type-attack', 'value'),
   Input('dropdown-gen-attack', 'value')])
def update_highest_attack(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	filtered_data = funcs.get_filtered_data(types, 
									generations, 
									sort_by='Attack',
									ascending=False)

	img_url = filtered_data.iloc[0]['Image URL']

	return img_url

@app.callback(
   Output('highest-defense-img', 'src'),
   [Input('dropdown-type-defense', 'value'),
   Input('dropdown-gen-defense', 'value')])
def update_highest_defense(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	filtered_data = funcs.get_filtered_data(types, 
									generations, 
									sort_by='Defense',
									ascending=False)

	img_url = filtered_data.iloc[0]['Image URL']

	return img_url

@app.callback(
   Output('highest-stamina-img', 'src'),
   [Input('dropdown-type-stamina', 'value'),
   Input('dropdown-gen-stamina', 'value')])
def update_highest_stamina(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	filtered_data = funcs.get_filtered_data(types, 
									generations, 
									sort_by='Stamina',
									ascending=False)

	img_url = filtered_data.iloc[0]['Image URL']

	return img_url

@app.callback(
   Output('highest-cp-img', 'src'),
   [Input('dropdown-type-cp', 'value'),
   Input('dropdown-gen-cp', 'value')])
def update_highest_cp(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	filtered_data = funcs.get_filtered_data(types, 
									generations, 
									sort_by='Max CP',
									ascending=False)

	img_url = filtered_data.iloc[0]['Image URL']

	return img_url

@app.callback(
   Output('highest-hp-img', 'src'),
   [Input('dropdown-type-hp', 'value'),
   Input('dropdown-gen-hp', 'value')])
def update_highest_hp(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	filtered_data = funcs.get_filtered_data(types, 
									generations, 
									sort_by='Max HP',
									ascending=False)

	img_url = filtered_data.iloc[0]['Image URL']

	return img_url

@app.callback(
   Output('highest-cr-img', 'src'),
   [Input('dropdown-type-cr', 'value'),
   Input('dropdown-gen-cr', 'value')])
def update_highest_cr(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	filtered_data = funcs.get_filtered_data(types, 
									generations, 
									sort_by='Base Capture Rate (%)',
									ascending=False)

	img_url = filtered_data.iloc[0]['Image URL']

	return img_url

@app.callback(
   Output('lowest-fr-img', 'src'),
   [Input('dropdown-type-fr', 'value'),
   Input('dropdown-gen-fr', 'value')])
def update_lowest_fr(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	filtered_data = funcs.get_filtered_data(types, 
									generations, 
									sort_by='Base Flee Rate (%)',
									ascending=True)

	img_url = filtered_data.iloc[0]['Image URL']

	return img_url

@app.callback(
   Output('lowest-km-img', 'src'),
   [Input('dropdown-type-km', 'value'),
   Input('dropdown-gen-km', 'value')])
def update_lowest_km(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	filtered_data = funcs.get_filtered_data(types, 
									generations, 
									sort_by='Distance to Candy (km)',
									ascending=True)

	img_url = filtered_data.iloc[0]['Image URL']

	return img_url

@app.callback(
	[Output('datatable-pareto', 'data'),
	Output('datatable-pareto', 'columns')],
    [Input('dropdown-type', 'value'),
   Input('dropdown-generation', 'value')])
def update_pareto_table(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	frontier = funcs.get_pareto_frontier(types, generations)
	columns = [{"name": i, "id": i, 'deletable': True} for 
                						i in frontier.columns.values]
              									
	return frontier.to_dict('records'), columns

@app.callback(
	Output('pareto-frontier-2d', 'figure'),
    [Input('dropdown-type', 'value'),
   Input('dropdown-generation', 'value')])
def update_pareto_2d(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	fig = funcs.plot_pareto_2d(types, generations)
              									
	return fig

@app.callback(
	Output('pareto-frontier-3d', 'figure'),
    [Input('dropdown-type', 'value'),
   Input('dropdown-generation', 'value')])
def update_pareto_3d(types_value, gens_value):
	types = TYPES if types_value == 'All' else [types_value]
	generations = GENS if gens_value == 'All' else [gens_value]

	fig = funcs.plot_pareto_3d(types, generations)
              									
	return fig




##### Similar Pokemon callbacks #####

@app.callback(
   Output('selected-pokemon', 'src'),
   [Input('dropdown-names', 'value')])
def update_selected_pokemon(name):
	img_url = DATA.loc[DATA['Name'] == name, 'Image URL'].values[0]

	return img_url

@app.callback(
   [Output('similar-first', 'src'),
   Output('similar-second', 'src'),
   Output('similar-third', 'src')],
   [Input('dropdown-names', 'value')])
def update_similar_pokemon(name):
	img_urls = funcs.get_similar_n(name)

	return img_urls

@app.callback(
	Output('FAMD-plot', 'figure'),
    [Input('radio-famd', 'value'),
   Input('famd-color', 'value')])
def update_famd_plot(num_components, color):
	fig = funcs.plot_FAMD(num_components, color)
              									
	return fig
