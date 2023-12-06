from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import dash_bootstrap_components as dbc

dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])



dash2.layout = html.Div(
    [html.H1("BootSrap Layout"),
     html.P("這是段茖1"),
     html.P("這昃段落2"),
     ],
     className="container-lg",
     style={'backgroundColor':'#666'}


    )