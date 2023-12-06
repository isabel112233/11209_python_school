from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
dash2 = Dash(requests_pathname_prefix="/dash/app2/")

dash2.layout = html.Div([
    html.H1("Dash H1"),
    html.P("這是段茖1"),
    html.P("這是段茖2"),

])