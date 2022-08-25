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
df_mat9ano2bi = pd.read_csv(DATA_PATH.joinpath("mat9ano2bi.csv")) 
df_habs92bi= df_mat9ano2bi.drop(columns=['Escola','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(children = [dbc.Col(dcc.Dropdown(df_mat9ano2bi['Escola'].unique(), value='E. M. E. C Boanerges Moreira de Paula', style ={'margin-top':10, 'margin-left':5}, id='drop-downE92bi',), width=4),
                        dbc.Col(dcc.Dropdown(df_mat9ano2bi['Turma'].unique(), value='U', style ={'margin-top':10, 'margin-left':5}, id='drop-down92bi',), width=2) ]
        ),

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total92bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal92bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA09"),dbc.CardBody(children=[] , id='EF09MA092bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA092bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA09bTO"),dbc.CardBody(children=[] , id='EF09MA09bTO2bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA09bTO2bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA12"),dbc.CardBody(children=[] , id='EF09MA122bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA122bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total92bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA09,
            target="EF09MA092bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA09bTO,
            target="EF09MA09bTO2bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA12,
            target="EF09MA122bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA19"),dbc.CardBody(children=[] , id='EF09MA192bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA192bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA09aTO"),dbc.CardBody(children=[] , id='EF09MA09aTO2bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA09aTO2bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA22"),dbc.CardBody(children=[] , id='EF09MA222bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA222bi')),
            ]
    ),
    dbc.Popover(
            EF09MA19,
            target="EF09MA192bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA09aTO,
            target="EF09MA09aTO2bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA22,
            target="EF09MA222bi",
            body=True,
            trigger="hover"),
    
    html.Br(),
   
     dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat9ano2bi['Turma'].unique(), value='U', style ={'margin-top':10, 'margin-left':5}, id='drop-turma92bi')),
    dbc.Col(dcc.Dropdown(df_habs92bi.columns, value="EF09MA22", style ={'margin-top':10, 'margin-left':5}, id='drop-hab92bi')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs92bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto92bi',config= {'displaylogo': False}))),

])

])



@app.callback(
    Output('total92bi','children'),
    Output('cardtotal92bi', 'color'),
    Input('drop-down92bi','value'),
    Input('drop-downE92bi','value'),
)
def habtotal(turma, escola):
    dff=df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    df = dff.loc[dff['Turma']==turma]
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
    Output('EF09MA092bi','children'),
    Output('cardEF09MA092bi', 'color'),
    Input('drop-down92bi','value'),
    Input('drop-downE92bi','value'),
)
def habtotal(turma, escola):
    dff=df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    df = dff.loc[dff['Turma']==turma]
    soma = df['EF09MA09'].values.sum()
    qtd = df['EF09MA09'].count()
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
    Output('EF09MA09bTO2bi','children'),
    Output('cardEF09MA09bTO2bi', 'color'),
    Input('drop-down92bi','value'),
    Input('drop-downE92bi','value'),
)
def habtotal(turma, escola):
    dff=df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    df = dff.loc[dff['Turma']==turma]
    soma = df['EF09MA09bTO'].values.sum()
    qtd = df['EF09MA09bTO'].count()
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
    Output('EF09MA122bi','children'),
    Output('cardEF09MA122bi', 'color'),
    Input('drop-down92bi','value'),
    Input('drop-downE92bi','value'),
)
def habtotal(turma, escola):
    dff=df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    df = dff.loc[dff['Turma']==turma]
    soma = df['EF09MA12'].values.sum()
    qtd = df['EF09MA12'].count()
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
    Output('EF09MA192bi','children'),
    Output('cardEF09MA192bi', 'color'),
    Input('drop-down92bi','value'),
    Input('drop-downE92bi','value'),
)
def habtotal(turma, escola):
    dff=df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    df = dff.loc[dff['Turma']==turma]
    soma = df['EF09MA19'].values.sum()
    qtd = df['EF09MA19'].count()
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



#-----------------------------------------------------------------

#-----------------------------------------------------------------




#-----------------------------------------------------------------

@app.callback(
    Output('EF09MA09aTO2bi','children'),
    Output('cardEF09MA09aTO2bi', 'color'),
    Input('drop-down92bi','value'),
    Input('drop-downE92bi','value'),
)
def habtotal(turma, escola):
    dff=df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    df = dff.loc[dff['Turma']==turma]
    soma = df['EF09MA09aTO'].values.sum()
    qtd = df['EF09MA09aTO'].count()
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
    Output('EF09MA222bi','children'),
    Output('cardEF09MA222bi', 'color'),
    Input('drop-down92bi','value'),
    Input('drop-downE92bi','value'),
)
def habtotal(turma, escola):
    dff=df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    df = dff.loc[dff['Turma']==turma]
    soma = df['EF09MA22'].values.sum()
    qtd = df['EF09MA22'].count()
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


#-----------------------------------------------------------------



#-----------------------------------------------------------------


#-----------------------------------------------------------------



#-----------------------------------------------------------------



@app.callback(
    Output('figacerto92bi','figure'),
    Input('drop-hab92bi','value'),
    Input('drop-turma92bi','value'),
    Input('drop-downE92bi','value'),
)
def acertos(hab, turma, escola):
    df = df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    d = df.loc[df['Turma']==turma]
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
    Output('fighabs92bi','figure'),
    Input('drop-turma92bi','value'),
    Input('drop-downE92bi','value'),
    
)
def habs(turma,escola):
    d = df_mat9ano2bi.loc[df_mat9ano2bi['Escola']==escola]
    df = d.loc[d['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
