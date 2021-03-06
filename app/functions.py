import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

import pandas as pd
import numpy as np

import gower

import prince

from sklearn import manifold

from components import (ALL_STATS, BASIC_STATS, TYPES, 
						GENS, DATA, BASE_COLS, OTHER, SIZE_COLS,
						CATEGORICAL_COLS_GOWER, NUMERICAL_COLS_GOWER)

GOWER_MATRIX = gower.gower_matrix(DATA.fillna('None')[CATEGORICAL_COLS_GOWER+NUMERICAL_COLS_GOWER])


def update_stats_scatter(stats, types, generations, yaxis):
	labels = BASE_COLS + stats + OTHER
	df = DATA[labels]
	df = df[((df['Type 1'].isin(types)) | (df['Type 2'].isin(types))) & 
									(df['Generation'].isin(generations))]
	df_long = pd.melt(df, id_vars=BASE_COLS+OTHER, value_vars=stats, var_name="Stat")

	if len(stats) == 1:
		fig = px.scatter(df, x=stats[0], y=yaxis,
           hover_name="Name",
                 color_discrete_sequence=px.colors.diverging.Spectral_r)

	else:
		fig = px.scatter(df_long, x="value", y=yaxis,
           hover_name="Name", facet_col="Stat", color="Stat",
                 color_discrete_sequence=px.colors.diverging.Spectral_r)
		for i in range(1, len(stats)+1):
			fig.update_xaxes({"title": stats[i-1]}, col=i)
		fig.for_each_annotation(lambda a: a.update(text=""))

	fig.update_layout(showlegend=False)

	return fig

def update_stats_boxplots(stats, xaxis):
	labels = BASE_COLS + stats 
	df = DATA[labels]
	df = df.fillna('None')
	df_long = pd.melt(df, id_vars=BASE_COLS, value_vars=stats, 
					var_name="Stat", value_name="Distribution")

	fig = px.box(df_long, x=xaxis, y="Distribution", color="Stat", 
		notched=False, 
		hover_data=BASE_COLS,
		color_discrete_sequence=px.colors.diverging.Spectral_r)

	fig.update_layout(legend_orientation='h', 
						legend=dict(x=0.3, y=1.1),
						legend_title_text='')

	return fig

def update_stats_heatmap(col_scale):
	correlations = DATA[ALL_STATS+SIZE_COLS+OTHER].corr().values

	corr_text = np.around(correlations, decimals=2)

	fig = ff.create_annotated_heatmap(correlations, 
							x=ALL_STATS+SIZE_COLS+OTHER, 
							y=ALL_STATS+SIZE_COLS+OTHER, 
							annotation_text=corr_text, 
                            colorscale=col_scale)
	return fig

def get_filtered_data(types, generations, sort_by, ascending):
	df = DATA[((DATA['Type 1'].isin(types)) | (DATA['Type 2'].isin(types))) & 
									(DATA['Generation'].isin(generations))]
	df = df.sort_values(by=sort_by, ascending=ascending)

	return df

def is_pareto_efficient(data, return_mask=True):
    is_efficient = np.arange(data.shape[0])
    n_points = data.shape[0]
    next_point_index = 0  # Next index in the is_efficient array to search for
    while next_point_index<len(data):
        nondominated_point_mask = np.any(data>data[next_point_index], axis=1)
        nondominated_point_mask[next_point_index] = True
        is_efficient = is_efficient[nondominated_point_mask]  # Remove dominated points
        data = data[nondominated_point_mask]
        next_point_index = np.sum(nondominated_point_mask[:next_point_index])+1
    if return_mask:
        is_efficient_mask = np.zeros(n_points, dtype=bool)
        is_efficient_mask[is_efficient] = True
        return is_efficient_mask
    else:
        return is_efficient

def get_pareto_frontier(types, generations, columns=ALL_STATS):
	df = get_filtered_data(types, generations, sort_by='ID', ascending=True)
	frontier = df[is_pareto_efficient(df[columns].values, return_mask=True)]

	return frontier[BASE_COLS+BASIC_STATS]

def plot_pareto_2d(types, generations):
	df = get_filtered_data(types, generations, sort_by='ID', ascending=True)
	pareto_front_indexes = is_pareto_efficient(df[['Max CP', 'Max HP']].values)

	df['is_pareto'] = False
	df.at[df.index[pareto_front_indexes],'is_pareto'] = True

	fig = px.scatter(df, x="Max HP", y="Max CP", 
							color="is_pareto",
							hover_name="Name",
							hover_data=["Is Legendary"])

	fig.update_layout(showlegend=False)
	
	return fig

def plot_pareto_3d(types, generations):
	df = get_filtered_data(types, generations, sort_by='ID', ascending=True)
	pareto_front_indexes = is_pareto_efficient(df[BASIC_STATS].values)

	df['is_pareto'] = False
	df.at[df.index[pareto_front_indexes],'is_pareto'] = True

	fig = px.scatter_3d(df, x="Attack", 
 						y="Defense", 
 						z="Stamina", 
 						color="is_pareto",
 						hover_name="Name",
 						hover_data=["Is Legendary"])

	fig.update_traces(marker_size=4)

	fig.update_layout(scene=dict(xaxis_title='Attack',
                    yaxis_title='Defense',
                    zaxis_title='Stamina'),
					showlegend=False)
	return fig

def get_similar_n(name, n=3):
	X = DATA[NUMERICAL_COLS_GOWER+CATEGORICAL_COLS_GOWER]
	pokemon = X[DATA['Name'] == name]
	similar_indexes = gower.gower_topn(pokemon, X, n=n+1)['index']
	similar = DATA.iloc[similar_indexes]
	similar_imgs = similar['Image URL'].values[1:]

	return list(similar_imgs)

def FAMD(num_components):
	famd = prince.FAMD(n_components=num_components,
						n_iter=3,
						copy=True,
						check_input=True,
						engine='auto',
						random_state=0)

	df = DATA.fillna('None')
	df_reduced = df[CATEGORICAL_COLS_GOWER+NUMERICAL_COLS_GOWER]

	components = famd.fit(df_reduced).row_coordinates(df_reduced)
	components = components.rename(columns={i : "Component "+str(i+1) for i in range(num_components)})

	df = pd.concat([df, components], axis=1)

	return df

def TSNE(num_components):
	df = DATA.fillna('None')

	tsne = manifold.TSNE(n_components=num_components,
							metric='precomputed')

	components = tsne.fit_transform(GOWER_MATRIX)
	components = pd.DataFrame(components).rename(columns={i : "Component "+str(i+1) for i in range(num_components)})

	df = pd.concat([df, components], axis=1)

	return df

def MDS(num_components):
	df = DATA.fillna('None')

	mds = manifold.MDS(n_components=num_components,
							dissimilarity='precomputed')

	components = mds.fit_transform(GOWER_MATRIX)
	components = pd.DataFrame(components).rename(columns={i : "Component "+str(i+1) for i in range(num_components)})

	df = pd.concat([df, components], axis=1)

	return df


def plot_components(method, num_components, color):
	num_components = int(num_components)
	if method == "FAMD":
		df = FAMD(num_components)
	elif method == "MDS":
		df = MDS(num_components)
	else:
		df = TSNE(num_components)

	if num_components == 2:
		fig = px.scatter(df, x="Component 1", 
					y="Component 2", 
					hover_name='Name', 
					color=color,
					color_discrete_sequence=px.colors.diverging.Spectral_r,
					hover_data=["Generation", "Type 1", "Type 2", "Is Legendary"])
		fig.update_layout(scene=dict(xaxis_title='Component 1',
                    	yaxis_title='Component 2'))

	elif num_components == 3:
		fig = px.scatter_3d(df, x="Component 1", 
					y="Component 2",
					z="Component 3", 
					hover_name='Name', 
					color=color,
					color_discrete_sequence=px.colors.diverging.Spectral_r,
					hover_data=["Generation", "Type 1", "Type 2", "Is Legendary"])
		fig.update_layout(scene=dict(xaxis_title='Component 1',
                    	yaxis_title='Component 2',
                    	zaxis_title='Component 3'))
		fig.update_traces(marker_size=4)

	return fig



