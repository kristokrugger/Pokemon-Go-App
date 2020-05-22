import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import server
from app import app

from layouts import (layout_stats_analysis, 
                    layout_top_pokemon, 
                    layout_similar_pokemon,
                    noPage)

import callbacks

import pandas as pd
import io


app.index_string = ''' 
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Pokemon Go Analysis Dashboard</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>Pokemon Go Analysis Dashboard © Kristo Krugger</div>
    </body>
</html>
'''

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pokemon-go-app/' or pathname == '/pokemon-go-app/stats-analysis/':
      return layout_stats_analysis    
    elif pathname == '/pokemon-go-app/top-pokemon/':
        return layout_top_pokemon
    elif pathname == '/pokemon-go-app/similar-pokemon/':
        return layout_similar_pokemon
    else:
        return noPage


external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})

if __name__ == '__main__':
    app.run_server(debug=True)
