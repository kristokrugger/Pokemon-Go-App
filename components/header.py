import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo_url = "https://teambeyond.net/wp-content/uploads/2016/07/Pokemon-Header.jpg"

    logo = html.Div([

        html.Div([
            html.Img(src=logo_url, 
                height='250', className="twelve columns padded")
        ], className="twelve columns",
            style={"padding-bottom":"15px"})

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Top and Similar Pokemon in Pokemon Go')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([
        dcc.Link('Stats Analysis', 
                href='/pokemon-go-app/stats-analysis/', 
                className="tab first"),
        dcc.Link('Top Pokemon', 
                href='/pokemon-go-app/top-pokemon/', 
                className="tab"),
        dcc.Link('Similar Pokemon', 
                href='/pokemon-go-app/similar-pokemon/', 
                className="tab"),
    ], className="row ")
    return menu
