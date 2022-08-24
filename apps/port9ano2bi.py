from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib
from app import app
from dicionario import *


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df_port9ano2bi = pd.read_csv(DATA_PATH.joinpath("port9ano2bi.csv")) 
df_habsport92bi = df_port9ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port9ano2bi['Turma'].unique(), value='U', style ={'margin-top':10, 'margin-left':5}, id='drop-down192bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total192bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal192bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP02"),dbc.CardBody(children=[] , id='EF09LP022bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP022bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP04"),dbc.CardBody(children=[] , id='EF89LP042bi', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP042bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP11"),dbc.CardBody(children=[] , id='EF09LP112bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP112bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total192bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09LP02,
            target="EF09LP022bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP04,
            target="EF89LP042bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09LP11,
            target="EF09LP112bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP10"),dbc.CardBody(children=[] , id='EF09LP102bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP102bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP33"),dbc.CardBody(children=[] , id='EF89LP332bi', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP332bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP12"),dbc.CardBody(children=[] , id='EF09LP1232bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP1232bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP27"),dbc.CardBody(children=[] , id='EF69LP2732bi', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP2732bi')),
            ]
    ),
    dbc.Popover(
            EF09LP10,
            target="EF09LP102bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP33,
            target="EF89LP332bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09LP12,
            target="EF09LP1232bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP27,
            target="EF69LP2732bi",
            body=True,
            trigger="hover"),
    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port9ano2bi['Turma'].unique(), value='U', style ={'margin-top':10, 'margin-left':5}, id='drop-turma182bi')),
    dbc.Col(dcc.Dropdown(df_habsport92bi.columns, value="EF69LP27", style ={'margin-top':10, 'margin-left':5}, id='drop-hab182bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs182bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto182bi',config= {'displaylogo': False}))),


]),



])

@app.callback(
    Output('total192bi','children'),
    Output('cardtotal192bi', 'color'),
    Input('drop-down192bi','value')
)
def habtotal(turma):
    df = df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    soma = df['Total'].values.sum()
    qtd = df['Total'].count()
    soma=int(soma)
    qtd= int(qtd)
    media= soma//qtd
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'
#----------------------------------------------------------------------
@app.callback(
    Output('EF09LP022bi','children'),
    Output('cardEF09LP022bi', 'color'),
    Input('drop-down192bi','value')
)
def hab1(turma):
    df= df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    soma = df['EF09LP02'].values.sum()
    qtd = df['EF09LP02'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------

@app.callback(
    Output('EF89LP042bi','children'),
    Output('cardEF89LP042bi', 'color'),
    Input('drop-down192bi','value')
)
def hab2(turma):
    df= df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    soma = df['EF89LP04'].values.sum()
    qtd = df['EF89LP04'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------

@app.callback(
    Output('EF09LP112bi','children'),
    Output('cardEF09LP112bi', 'color'),
    Input('drop-down192bi','value')
)
def hab3(turma):
    df= df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma] 
    soma = df['EF09LP11'].values.sum()
    qtd = df['EF09LP11'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------

@app.callback(
    Output('EF09LP102bi','children'),
    Output('cardEF09LP102bi', 'color'),
    Input('drop-down192bi','value')
)
def hab4(turma):
    df= df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    soma = df['EF09LP10'].values.sum()
    qtd = df['EF09LP10'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------

@app.callback(
    Output('EF89LP332bi','children'),
    Output('cardEF89LP332bi', 'color'),
    Input('drop-down192bi','value')
)
def hab5(turma):
    df= df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    soma = df['EF89LP33'].values.sum()
    qtd = df['EF89LP33'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'


#-----------------------------------------------------------------

@app.callback(
    Output('EF09LP1232bi','children'),
    Output('cardEF09LP1232bi', 'color'),
    Input('drop-down192bi','value')
)
def hab6(turma):
    df= df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    soma = df['EF09LP12'].values.sum()
    qtd = df['EF09LP12'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'


#-----------------------------------------------------------------

@app.callback(
    Output('EF69LP2732bi','children'),
    Output('cardEF69LP2732bi', 'color'),
    Input('drop-down192bi','value')
)
def hab7(turma):
    df= df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    soma = df['EF69LP27'].values.sum()
    qtd = df['EF69LP27'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------------

@app.callback(
    Output('figacerto182bi','figure'),
    Input('drop-hab182bi','value'),
    Input('drop-turma182bi','value'),
)
def acertos(hab, turma):
    d = df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    dff= d[hab]
    acerto = 0
    erro = 0
    for i in dff:
        if i > 0:
            acerto= acerto+1
        else:
            erro = erro +1
    fig= px.pie( values=[acerto, erro], names = {acerto:'Apresentaram Domínio Mínimo', erro:'Não Apresentaram Domínio Mínimo'}, color={'Apresentaram Domínio Mínimo':'#0000ff','Não Apresentaram Domínio Mínimo':'#ff0000'}, title='Percentual de estudantes que mostraram <br> pelo menos domínio mínimo na habilidade '+str(hab)+' na turma '+str(turma).upper())
    return fig

@app.callback(
    Output('fighabs182bi','figure'),
    Input('drop-turma182bi','value'),
)
def habs(turma):
    df = df_port9ano2bi.loc[df_port9ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

