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
df_mat5ano2bi = pd.read_csv(DATA_PATH.joinpath("mat5ano2bi.csv"))
df_habs52bi= df_mat5ano2bi.drop(columns=['Escola','Ano','Turma','Total'])  


layout = html.Div(children=[
    dbc.Row(
        children=[
        dbc.Col(dcc.Dropdown(df_mat5ano2bi['Escola'].unique(), value='E. M. T. I. Vilmar Vasconselos Feitosa', style ={'margin-top':10, 'margin-left':5}, id='drop-downEs52bi',), width=4),
        dbc.Col(dcc.Dropdown(df_mat5ano2bi['Turma'].unique(), value='A', style ={'margin-top':10, 'margin-left':5}, id='drop-down52bi',), width=2)]),
       
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total52bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal52bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA02"),dbc.CardBody(children=[] , id='EF05MA022bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA022bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA03"),dbc.CardBody(children=[] , id='EF05MA032bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA032bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA19"),dbc.CardBody(children=[] , id='EF05MA192bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA192bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total52bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA02,
            target="EF05MA022bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA03,
            target="EF05MA032bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA19,
            target="EF05MA192bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA18"),dbc.CardBody(children=[] , id='EF05MA182bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA182bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA24"),dbc.CardBody(children=[] , id='EF05MA242bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA242bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA25"),dbc.CardBody(children=[] , id='EF05MA252bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA252bi')),
            ]
    ),
    dbc.Popover(
            EF05MA18,
            target="EF05MA182bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA24,
            target="EF05MA242bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA25,
            target="EF05MA252bi",
            body=True,
            trigger="hover"),
    
    html.Br(),
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat5ano2bi['Turma'].unique(), value='A', style ={'margin-top':10, 'margin-left':5}, id='drop-turma52bi')),
    dbc.Col(dcc.Dropdown(df_habs52bi.columns, value="EF05MA25", style ={'margin-top':10, 'margin-left':5}, id='drop-hab52bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs52bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto52bi',config= {'displaylogo': False}))),
])

])


@app.callback(
    Output('total52bi','children'),
    Output('cardtotal52bi', 'color'),
    Input('drop-down52bi','value'),
    Input('drop-downEs52bi', 'value'),
)
def hab1(turma, escola):
    dff = df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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
    Output('EF05MA022bi','children'),
    Output('cardEF05MA022bi', 'color'),
    Input('drop-down52bi','value'),
    Input('drop-downEs52bi', 'value'),
)
def hab1(turma, escola):
    dff = df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF05MA02'].values.sum()
    qtd = df['EF05MA02'].count()
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
    Output('EF05MA032bi','children'),
    Output('cardEF05MA032bi', 'color'),
    Input('drop-down52bi','value'),
    Input('drop-downEs52bi', 'value'),
)
def hab1(turma, escola):
    dff = df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF05MA03'].values.sum()
    qtd = df['EF05MA03'].count()
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
    Output('EF05MA192bi','children'),
    Output('cardEF05MA192bi', 'color'),
    Input('drop-down52bi','value'),
    Input('drop-downEs52bi', 'value'),
)
def hab1(turma, escola):
    dff = df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF05MA19'].values.sum()
    qtd = df['EF05MA19'].count()
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
    Output('EF05MA182bi','children'),
    Output('cardEF05MA182bi', 'color'),
    Input('drop-down52bi','value'),
    Input('drop-downEs52bi', 'value'),
)
def hab1(turma, escola):
    dff = df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF05MA18'].values.sum()
    qtd = df['EF05MA18'].count()
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
    Output('EF05MA242bi','children'),
    Output('cardEF05MA242bi', 'color'),
    Input('drop-down52bi','value'),
    Input('drop-downEs52bi', 'value'),
)
def hab1(turma, escola):
    dff = df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF05MA24'].values.sum()
    qtd = df['EF05MA24'].count()
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
    Output('EF05MA252bi','children'),
    Output('cardEF05MA252bi', 'color'),
    Input('drop-down52bi','value'),
    Input('drop-downEs52bi', 'value'),
)
def hab1(turma, escola):
    dff = df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF05MA25'].values.sum()
    qtd = df['EF05MA25'].count()
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



#-----------------------------------------------------------------------
@app.callback(
    Output('figacerto52bi','figure'),
    Input('drop-hab52bi','value'),
    Input('drop-turma52bi','value'),
    Input('drop-downEs52bi','value')
)
def acertos(hab, turma, escola):
    df=df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
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
    Output('fighabs52bi','figure'),
    Input('drop-turma52bi','value'),
    Input('drop-downEs52bi','value'),
)
def habs(turma,escola):
    d = df_mat5ano2bi.loc[df_mat5ano2bi['Escola']==escola]
    df = d.loc[d['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

