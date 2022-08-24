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
df_port5ano2bi = pd.read_csv(DATA_PATH.joinpath("port5ano2bi.csv")) 
df_habsport52bi = df_port5ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port5ano2bi['Turma'].unique(), value='A', style ={'margin-top':10, 'margin-left':5}, id='drop-down152bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total152bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal152bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP31"),dbc.CardBody(children=[] , id='EF35LP312bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP312bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP23"),dbc.CardBody(children=[] , id='EF35LP2322bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP2322bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP01"),dbc.CardBody(children=[] , id='EF15LP0122bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP0122bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total152bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP31,
            target="EF35LP312bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP23,
            target="EF35LP2322bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP01,
            target="EF15LP0122bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP15"),dbc.CardBody(children=[] , id='EF05LP152bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP152bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP16"),dbc.CardBody(children=[] , id='EF05LP162bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP162bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP17"),dbc.CardBody(children=[] , id='EF15LP172bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP172bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP27"),dbc.CardBody(children=[] , id='EF35LP272bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP272bi')),
            ]
    ),

    dbc.Popover(
            EF05LP15,
            target="EF05LP152bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05LP16,
            target="EF05LP162bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP17,
            target="EF15LP172bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP27,
            target="EF35LP272bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP03"),dbc.CardBody(children=[] , id='EF05LP032bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP032bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP01"),dbc.CardBody(children=[] , id='EF05LP0122bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP0122bi'), width=3),
            ]
    ),
     dbc.Popover(
            EF05LP03,
            target="EF05LP032bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05LP01,
            target="EF05LP0122bi",
            body=True,
            trigger="hover"),
            
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port5ano2bi['Turma'].unique(), value='A', style ={'margin-top':10, 'margin-left':5}, id='drop-turma142bi')),
    dbc.Col(dcc.Dropdown(df_habsport52bi.columns, value="EF05LP01", style ={'margin-top':10, 'margin-left':5}, id='drop-hab142bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs142bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto142bi',config= {'displaylogo': False}))),


]),

    

])

@app.callback(
    Output('total152bi','children'),
    Output('cardtotal152bi', 'color'),
    Input('drop-down152bi','value')
)
def habtotal(turma):
    df = df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
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
    Output('EF35LP312bi','children'),
    Output('cardEF35LP312bi', 'color'),
    Input('drop-down152bi','value')
)
def hab1(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF35LP31'].values.sum()
    qtd = df['EF35LP31'].count()
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
    Output('EF35LP2322bi','children'),
    Output('cardEF35LP2322bi', 'color'),
    Input('drop-down152bi','value')
)
def hab2(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF35LP23'].values.sum()
    qtd = df['EF35LP23'].count()
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
    Output('EF35LP272bi','children'),
    Output('cardEF35LP272bi', 'color'),
    Input('drop-down152bi','value')
)
def hab3(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF35LP27'].values.sum()
    qtd = df['EF35LP27'].count()
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
    Output('EF05LP152bi','children'),
    Output('cardEF05LP152bi', 'color'),
    Input('drop-down152bi','value')
)
def hab4(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF05LP15'].values.sum()
    qtd = df['EF05LP15'].count()
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
    Output('EF05LP162bi','children'),
    Output('cardEF05LP162bi', 'color'),
    Input('drop-down152bi','value')
)
def hab5(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF05LP16'].values.sum()
    qtd = df['EF05LP16'].count()
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
    Output('EF15LP172bi1','children'),
    Output('cardEF15LP172bi1', 'color'),
    Input('drop-down152bi','value')
)
def hab6(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF15LP17'].values.sum()
    qtd = df['EF15LP17'].count()
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
    Output('EF15LP0122bi','children'),
    Output('cardEF15LP0122bi', 'color'),
    Input('drop-down152bi','value')
)
def hab7(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF15LP01'].values.sum()
    qtd = df['EF15LP01'].count()
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
    Output('EF05LP032bi','children'),
    Output('cardEF05LP032bi', 'color'),
    Input('drop-down152bi','value')
)
def hab8(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF05LP03'].values.sum()
    qtd = df['EF05LP03'].count()
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
    Output('EF05LP0122bi','children'),
    Output('cardEF05LP0122bi', 'color'),
    Input('drop-down152bi','value')
)
def hab10(turma):
    df= df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    soma = df['EF05LP01'].values.sum()
    qtd = df['EF05LP01'].count()
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

#-----------------------------------------------------------------

#-----------------------------------------------------------------

#-----------------------------------------------------------------


@app.callback(
    Output('figacerto142bi','figure'),
    Input('drop-hab142bi','value'),
    Input('drop-turma142bi','value'),
)
def acertos(hab, turma):
    d = df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
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
    Output('fighabs142bi','figure'),
    Input('drop-turma142bi','value'),
)
def habs(turma):
    df = df_port5ano2bi.loc[df_port5ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig



