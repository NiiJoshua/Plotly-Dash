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
dropdonw = dcc.Dropdown(options)