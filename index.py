
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Connect to main app.py file
from app import app, server
# Connect to your app pages
from apps import mat5ano2bi, mat9ano2bi, port5ano2bi, port9ano2bi

button = html.Div(children=[
    
    dbc.Button(
            "Segundo Bimestre",
            id="collapse-button2bi",
            className="mb-3",
            color="primary",
            n_clicks=0,),
        dbc.Collapse(children=[
            
            dbc.Button('Matemática 5 Ano', href='/apps/mat5ano2bi', outline=True,className="d-grid gap-2",color="primary"),
            dbc.Button('Matemática 9 Ano', href='/apps/mat9ano2bi', outline=True,className="d-grid gap-2",color="primary"),
            html.Br(), 
           
            dbc.Button('Português 5 Ano', href='/apps/port5ano2bi', outline=True,className="d-grid gap-2",color="success"),
            dbc.Button('Português 9 Ano', href='/apps/port9ano2bi', outline=True,className="d-grid gap-2",color="success"), 
    ], id="collapse2bi", is_open=False, className="mt-3"),
 
    
    
    ],
    className="d-grid gap-2 col-12 mx-auto")
app.layout = html.Div([   
    dcc.Location(id='url', refresh=False),

    html.Div(
    dbc.Container(
        [
            html.H1('Mapa de Habilidade BNCC Miracema do Tocantins')
        ],
        fluid=True,
        className="py-3",
        
    ),
    className="p-5 bg-light rounded-3",style={'background-image': 'url("assets/Top-V1-Mapa-de-Habilidades-BNCC-Aliança.png")','background-size': 'cover','background-repeat': 'no-repeat'}
),
html.Br(),
    html.Div(
        [
        dbc.Row(children=[dbc.Col([dbc.Button("Séries", id="open-offcanvas", n_clicks=0, style={'margin-top':3,'margin-left':10, 'width':200})]),dbc.Col([html.H1(children=[], id='titulo', style={'margin-left':150})], width=9)]),
            dbc.Offcanvas(
                children=[

                    button,
                ],

                id="offcanvas",
                title="Secretaria de Educação de Miracema do Tocantins",
                is_open=False,
                style={'background-color': '#cbe0f0'}
            ),
        ],
    ),

  html.Br(),
     
  html.Div(id='page-content', children=[])

],style={'background-image': 'url("/assets/Bg-Mapa-de-Habilidades-BNCC-Aliança.png")','background-size': 'contain'})




@app.callback(Output('page-content', 'children'),
              Output('titulo', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    
   
    if pathname == '/apps/mat5ano2bi':
        return mat5ano2bi.layout, 'Matemática 5 Ano / 2 Bimestre'
    if pathname == '/apps/mat9ano2bi':
        return mat9ano2bi.layout, 'Matemática 9 Ano / 2 Bimestre'
    
    if pathname == '/apps/port5ano2bi':
        return port5ano2bi.layout, 'Português 5 Ano / 2 Bimestre'
    if pathname == '/apps/port9ano2bi':
        return port9ano2bi.layout, 'Português 9 Ano / 2 Bimestre'
    else:
        return mat5ano2bi.layout, 'Matemática 1 Ano / 1 Bimestre'


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open

@app.callback(
    Output("collapse2bi", "is_open"),
    [Input("collapse-button2bi", "n_clicks")],
    [State("collapse2bi", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)
