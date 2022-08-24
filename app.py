import dash
import dash_bootstrap_components as dbc

# meta_tags servem para deixar o app responsivo
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}], external_stylesheets=[dbc.themes.MATERIA]
                )
server = app.server
