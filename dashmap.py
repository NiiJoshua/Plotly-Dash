# Imports
import pandas as pd
from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

# data source
data = "social_capital.csv"
df = pd.read_csv(data)

# Build Components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
mytitle = dcc.Markdown(children='')
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
    Input(dropdown, 'value')
)

def update_graph(col_name):
    print(col_name)
    print(type(col_name))

    fig = px.choropleth(data_frame = df, # graph from plotly.com/python/choropleth-maps
                        locations='STATE',
                        locationmode="USA-states",
                        scope="usa",
                        height=600,
                        color = col_name,
                        animation_frame='YEAR') 

    return fig, '# ' + col_name

# run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8053)