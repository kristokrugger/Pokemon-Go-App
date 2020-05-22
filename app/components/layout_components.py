import dash_core_components as dcc
import dash_html_components as html
import dash_table

from . import dash_reusable_components as drc

import pandas as pd


DATA = pd.read_csv('data/pokemon_data_full.csv', 
               header=0, 
               index_col=0, 
               dtype={'Generation':str, 'Is Legendary':str})

POKEMON_NAMES = DATA['Name'].values

NUMERICAL_COLS_GOWER = ['Attack', 'Defense', 'Stamina', 
               'Max CP', 'Max HP', 'Height (m)', 
               'Weight (kg)','Base Capture Rate (%)', 
               'Base Flee Rate (%)', 'Distance to Candy (km)'
]

CATEGORICAL_COLS_GOWER = ['Generation', 'Type 1', 
                  'Type 2', 'Is Legendary'
]

BASE_COLS = ['Name', 'ID', 
         'Generation', 'Type 1', 
         'Type 2', 'Max CP', 'Max HP']

BASIC_STATS = ['Attack', 'Defense', 'Stamina']

ALL_STATS = ['Attack', 'Defense', 'Stamina', 'Max HP', 'Max CP']

GENS = ['1', '2', '3', '4', '5', '7']

TYPES = ['Grass',
		 'Fire',
		 'Water',
		 'Bug',
		 'Normal',
		 'Poison',
		 'Electric',
		 'Ground',
		 'Fairy',
		 'Fighting',
		 'Psychic',
		 'Rock',
		 'Ghost',
		 'Ice',
		 'Dragon',
		 'Steel',
		 'Dark',
		 'Flying'
 ]

COLOUR_SCALES = ['Blues', 
      'Blues_r', 
      'Purples', 
      'Purples_r', 
      'Greens', 
      'Greens_r',
      'Viridis',
      'Viridis_r',
      'RdBu',
      'RdBu_r'
]

RATES = ["Base Capture Rate (%)", "Base Flee Rate (%)"]

SIZE_COLS = ['Height (m)', 'Weight (kg)']

OTHER = ["Base Capture Rate (%)",
         "Base Flee Rate (%)",
         "Distance to Candy (km)"
]

def get_full_stats_dropdown():
	dropdown = drc.NamedDropdown(name="Stats",
                                 id="dropdown-full-stat",
                                 options=[ 
                                    	{"label":val, "value":val} for val in 
                                    			["All"] + ALL_STATS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
	return html.Div([dropdown])

def get_basic_stats_dropdown():
	dropdown = drc.NamedDropdown(name="Stats",
                                 id="dropdown-basic-stat",
                                 options=[ 
                                    	{"label":val, "value":val} for val in 
                                    			["All"] + BASIC_STATS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
	return html.Div([dropdown])

def get_types_dropdown():
	dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type",
                                 options=[ 
                                    	{"label":val, "value":val} for val in 
                                    			["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
	return html.Div([dropdown])


def get_gens_dropdown():
	dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-generation",
                                 options=[ 
                                    	{"label":val, "value":val} for val in 
                                    			["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
	return html.Div([dropdown])


def get_HPCP_radio():
	radio = drc.NamedRadioItems(name="Y Axis",
								id="radio-HPCP",
								options=[ 
                                    	{"label":val, "value":val} for val in 
                                    			["Max CP", 
                                             "Max HP", 
                                             "Base Capture Rate (%)",
                                             "Base Flee Rate (%)",
                                             "Distance to Candy (km)"] 
                                    ],
                                 value="Max CP")
	return radio


def get_boxoptions_radio():
   radio = drc.NamedRadioItems(name="Show:",
                        id="radio-boxoptions",
                        options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["Stats", "Height & Weight", "Capture/Flee Rate"] 
                                    ],
                                 value="Stats")
   return radio


def get_boxplot_radio():
   radio = drc.NamedRadioItems(name="X Axis",
                        id="radio-boxplot",
                        options=[      
                                 {"label":"Generation", "value":"Generation"},
                                 {"label":"Primary \nType", "value": "Type 1"}, 
                                 {"label":"Secondary \nType", "value": "Type 2"}  
                                 ],
                                 value="Generation")
   return radio


def get_scale_radio():
   radio = drc.NamedRadioItems(name="Colour Scale",
                        id="radio-scale",
                        options=[ 
                                       {"label":val, "value":val} for val in 
                                             COLOUR_SCALES 
                                    ],
                                 value="Blues_r")
   return radio

def get_name_dropdown():
   dropdown = drc.NamedDropdown(name="Pokemon Name",
                                 id="dropdown-names",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             POKEMON_NAMES     
                                    ],
                                 clearable=False,
                                 searchable=True,
                                 value=POKEMON_NAMES[0])
   return html.Div([dropdown])

def get_types_dropdown_attack():
   dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type-attack",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_gens_dropdown_attack():
   dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-gen-attack",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])

def get_types_dropdown_defense():
   dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type-defense",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_gens_dropdown_defense():
   dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-gen-defense",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_types_dropdown_stamina():
   dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type-stamina",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_gens_dropdown_stamina():
   dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-gen-stamina",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])

def get_types_dropdown_cp():
   dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type-cp",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_gens_dropdown_cp():
   dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-gen-cp",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])

def get_types_dropdown_hp():
   dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type-hp",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_gens_dropdown_hp():
   dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-gen-hp",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])

def get_types_dropdown_cr():
   dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type-cr",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_gens_dropdown_cr():
   dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-gen-cr",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])

def get_types_dropdown_fr():
   dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type-fr",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_gens_dropdown_fr():
   dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-gen-fr",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])

def get_types_dropdown_km():
   dropdown = drc.NamedDropdown(name="Type",
                                 id="dropdown-type-km",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + TYPES
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])

   
def get_gens_dropdown_km():
   dropdown = drc.NamedDropdown(name="Generation",
                                 id="dropdown-gen-km",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             ["All"] + GENS
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="All")
   return html.Div([dropdown])


def get_famd_radio():
   radio = drc.NamedRadioItems(name="Number of Components",
                        id="radio-famd",
                        options=[{"label":i, "value":i} for i in ["2", "3"]],
                                 value="2")
   return radio

def get_famd_dropdown():
   dropdown = drc.NamedDropdown(name="Color Based on",
                                 id="famd-color",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             CATEGORICAL_COLS_GOWER
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="Is Legendary")
   return html.Div([dropdown])

def get_mds_radio():
   radio = drc.NamedRadioItems(name="Number of Components",
                        id="radio-mds",
                        options=[{"label":i, "value":i} for i in ["2", "3"]],
                                 value="2")
   return radio

def get_mds_dropdown():
   dropdown = drc.NamedDropdown(name="Color Based on",
                                 id="mds-color",
                                 options=[ 
                                       {"label":val, "value":val} for val in 
                                             CATEGORICAL_COLS_GOWER
                                    ],
                                 clearable=False,
                                 searchable=False,
                                 value="Is Legendary")
   return html.Div([dropdown])

