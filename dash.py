# Imports
import pandas as pd
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dcc
import plotly.express as px

# data source
data = "https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Good_to_Know/Dash2.0/social_capital.csv"
df = pd.read_csv(data)

# Build Components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
mytitle = dcc.Markdown(Children='')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options = df.columns.values[2:],
                        value='Cesaream Delivery Rate', # initial displayed value
                        clearable=False)

# Customize layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
])

# Callback
@app.callback(
    Output(mygraph, 'figure'),
    Output(mytitle, 'children'),
    Input(dropdown, value)
)

def update_graph(col_name):
    print(col_name)
    print(type(col_name))

    fig = px.choropleth(data) # graph from plotly.com/python/choropleth-maps