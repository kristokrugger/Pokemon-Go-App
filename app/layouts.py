import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd

from components import (ALL_STATS, DATA, TYPES,
						BASE_COLS, BASIC_STATS, 
						Header,
                        get_full_stats_dropdown,
                        get_basic_stats_dropdown, 
                        get_types_dropdown,
                        get_gens_dropdown,
                        get_HPCP_radio,
                        get_boxoptions_radio,
                        get_boxplot_radio,
                        get_scale_radio,
                        get_name_dropdown,
                        get_types_dropdown_attack,
						get_gens_dropdown_attack,
						get_types_dropdown_defense,
						get_gens_dropdown_defense,
						get_types_dropdown_stamina,
						get_gens_dropdown_stamina,
						get_types_dropdown_cp,
						get_gens_dropdown_cp,
						get_types_dropdown_hp,
						get_gens_dropdown_hp,
						get_types_dropdown_cr,
						get_gens_dropdown_cr,
						get_types_dropdown_fr,
						get_gens_dropdown_fr,
						get_types_dropdown_km,
						get_gens_dropdown_km,
                        get_famd_radio,
                        get_famd_dropdown)




######################## 404 Page ########################
noPage = html.Div([ 
    # CC Header
    Header(),
    html.P(["404 Page not found"])
    ], className="no-page")



######################## START Stats Analysis Layout ########################
layout_stats_analysis =  html.Div([
    html.Div([
        # Header
        Header(),
        html.Div([
          html.H6(["Stats Analysis"], 
            className="gs-header gs-text-header padded")
          ]),
        # Restore button
        html.Div([
          html.A(html.Button('Restore Columns', id='restore-cols'), id='download-link-stats-analysis')
          ]),
        # First Data Table
        html.Div([
            dash_table.DataTable(
                id='datatable-stat-analysis',
                columns=[{"name": i, "id": i, 'deletable': True} for 
                									i in DATA.columns.values[:-4]], 
                data=DATA.to_dict('records'),
                editable=False,
                style_table={'maxWidth': '1500px',
                             'maxHeight': '250px',
                             'overflowY': 'scroll'},
                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
                style_cell_conditional=  
                      [{'if': {'column_id': c}, 'backgroundColor': '#EAFAF1'} for c in ALL_STATS] 
                      + [{'if': {'column_id': c}, 'backgroundColor': '#FEF9E7'} for c in ['Type 1', 'Type 2']] 
                      + [{'if': {'column_id': c}, 'backgroundColor': '#EBF5FB'} for c in ['Generation' ,'Name', 'ID']],
                style_header={'backgroundColor': 'black','color': 'white'})
            ], className="twelve columns"),
 
        # stats scatter plot
        html.Div([ 
        	html.Div([
            html.Div([html.H6(["Scatterplot Controls"], 
            	className="gs-header gs-text-header padded")]),
            html.Br([]),
            html.Div([get_basic_stats_dropdown()]),
            html.Div([get_gens_dropdown()]),
            html.Div([get_types_dropdown()]),
            html.Div([get_HPCP_radio()])], 
            	className="three columns"),
            html.Div([
              dcc.Graph(id='stats-analysis-scatter', style={"visibility": "visible"})], className="nine columns"
              )
            ], 
        className="row"),

        # stats boxplots 
        html.Div([ 
        	html.Div([ 
        	html.Br([]),
        	html.Br([]),
            html.Div([html.H6(["Boxplot Controls"], 
            	className="gs-header gs-text-header padded")]),
            html.Br([]),
            html.Div([get_boxoptions_radio(),
            		get_boxplot_radio()])], 
            	className="two columns"),
            html.Div([
              dcc.Graph(id='stats-analysis-box', style={"visibility": "visible"})], 
              className="ten columns"
              )
            ], 
        className="row"),

        # stats correlations
        html.Div([ 
        	html.Div([ 
            html.Div([html.H6(["Heatmap Controls"], 
            	className="gs-header gs-text-header padded")]),
            html.Br([]),
            html.Div([get_scale_radio()])], 
            	className="three columns"),
            html.Div([
              dcc.Graph(id='stats-heatmap', style={"visibility": "visible"})], 
              className="nine columns"
              )
            ], 
        className="row")


        

        ], className="subpage")
    ], className="page")

######################## END Stats Analysis Layout ########################





######################## START Top Pokemon Layout ########################
layout_top_pokemon =  html.Div([
    html.Div([
        # Header
        Header(),
        html.Div([
          html.H6(["Top Pokemon Analysis"], 
            className="gs-header gs-text-header padded")
          ]),
        # best individual stat rankings
        html.Div([ 
        	html.Div([
            html.Div([html.H6(["Highest Attack"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='highest-attack-img',
              	src=''),
            html.Div([get_types_dropdown_attack()]),
            html.Div([get_gens_dropdown_attack()])
            ], 
            	className="three columns"),
            html.Div([
            html.Div([html.H6(["Highest Defense"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='highest-defense-img',
              	src=''),
            html.Div([get_types_dropdown_defense()]),
            html.Div([get_gens_dropdown_defense()])
            ], 
            	className="three columns"),
            html.Div([
            html.Div([html.H6(["Highest Stamina"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='highest-stamina-img',
              	src=''),
            html.Div([get_types_dropdown_stamina()]),
            html.Div([get_gens_dropdown_stamina()])
            ], 
            	className="three columns"),
            html.Div([
            html.Div([html.H6(["Highest Max CP"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='highest-cp-img',
              	src=''),
            html.Div([get_types_dropdown_cp()]),
            html.Div([get_gens_dropdown_cp()])
            ], 
            	className="three columns"),
            
            ], 
        className="row"),
        html.Div([ 
        	html.Div([
            html.Div([html.H6(["Highest Max HP"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='highest-hp-img',
              	src=''),
            html.Div([get_types_dropdown_hp()]),
            html.Div([get_gens_dropdown_hp()])
            ], 
            	className="three columns"),
            html.Div([
            html.Div([html.H6(["Highest Capture Rate"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='highest-cr-img',
              	src=''),
            html.Div([get_types_dropdown_cr()]),
            html.Div([get_gens_dropdown_cr()])
            ], 
            	className="three columns"),
            html.Div([
            html.Div([html.H6(["Lowest Flee Rate"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='lowest-fr-img',
              	src=''),
            html.Div([get_types_dropdown_fr()]),
            html.Div([get_gens_dropdown_fr()])
            ], 
            	className="three columns"),
            html.Div([
            html.Div([html.H6(["Lowest Km/Candy"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='lowest-km-img',
              	src=''),
            html.Div([get_types_dropdown_km()]),
            html.Div([get_gens_dropdown_km()])
            ], 
            	className="three columns"),
            
            ], 
        className="row"),
        html.Br([]),

        html.Div([ 
        	html.Div([ 
            html.Div([html.H6(["Pareto Frontier Based on Max CP and Max HP"], 
            	className="gs-header gs-text-header padded")]),
            dcc.Graph(id='pareto-frontier-2d', style={"visibility": "visible"})], 
            	className="five columns"),
            html.Div([
            	html.Div([html.H6(["Pareto Frontier Based on Attack, Defense, and Stamina"], 
            		className="gs-header gs-text-header padded")]),
              	dcc.Graph(id='pareto-frontier-3d', style={"visibility": "visible"})], 
              		className="seven columns")
            ], 
        className="row"),
        html.Br([]),

        html.Div([ 
        	html.Div([
            html.Div([html.H6(["Frontier Controls"], 
            	className="gs-header gs-text-header padded")]),
      
            html.Div([get_types_dropdown()]),
            html.Div([get_gens_dropdown()])
            ], 
            	className="two columns"),
            html.Div([
            html.Div([html.H6(["Pareto Frontier Based on Attack, Defense, Stamina, Max HP, and Max CP"], 
            	className="gs-header gs-text-header padded"),
            	dash_table.DataTable(
	                id='datatable-pareto',
	                columns=[{"name": i, "id": i, 'deletable': True} for 
	                									i in BASE_COLS+BASIC_STATS], 
	                data=DATA.to_dict('records'),
	                editable=False,
	                style_table={'maxWidth': '1500px',
	                             'maxHeight': '250px',
	                             'overflowY': 'scroll'},
	                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
	                css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
	                style_cell_conditional=  
	                      [{'if': {'column_id': c}, 'backgroundColor': '#EAFAF1'} for c in ALL_STATS] 
	                      + [{'if': {'column_id': c}, 'backgroundColor': '#FEF9E7'} for c in ['Type 1', 'Type 2']] 
	                      + [{'if': {'column_id': c}, 'backgroundColor': '#EBF5FB'} for c in ['Generation' ,'Name', 'ID']],
	                style_header={'backgroundColor': 'black','color': 'white'})
            ]),
            
            ], 
            	className="ten columns")
            
            ], 
        className="row"),


        ], className="subpage")
    ], className="page")

######################## END Top Pokemon Layout ########################
 



######################## START Similar Pokemon Layout ########################
layout_similar_pokemon =  html.Div([
    html.Div([
        # Header
        Header(),
        html.Div([
          html.H6(["Similar Pokemon Analysis"], 
            className="gs-header gs-text-header padded")
          ]),
        html.Div([ 
        	html.Div([
            html.Div([html.H6(["Select a Pokemon"], 
            	className="gs-header gs-text-header padded")]),
            html.Img(id='selected-pokemon',
              	src='https://images.gameinfo.io/pokemon/256/001-00.png'),
            html.Div([get_name_dropdown()])
            ], 
            	className="three columns"),
            html.Div([
            	html.Div([html.H6(["Most Similar Pokemon Based on Gower Distance"], 
            		className="gs-header gs-text-header padded")]),
            	html.Img(id='similar-first',
              	src=''),
            	html.Img(id='similar-second',
              	src=''),
              	html.Img(id='similar-third',
              	src='')
              	],
            	className="nine columns")
            
            ], 
        className="row"),

        html.Br([]),

        html.Div([ 
            html.Div([ 
            html.Div([html.H6(["FAMD Controls"], 
                className="gs-header gs-text-header padded")]),
      
            html.Div([get_famd_radio()]),
            html.Div([get_famd_dropdown()])
            ], 
                className="three columns"),

            html.Div([
                html.Div([html.H6(["Factor Analysis of Mixed Data (FAMD)"], 
                className="gs-header gs-text-header padded")]),
                dcc.Graph(id='FAMD-plot', style={"visibility": "visible"})], 
                className="nine columns")
            ], 
        className="row")
     

        ], className="subpage")
    ], className="page")

######################## END Similar Pokemon Layout ########################

