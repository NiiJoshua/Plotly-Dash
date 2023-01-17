from dash import Dash, dcc, Output, Input
import dash_bootstrap_componenets as dbc
import plotly.express as px

# Add data
df = px.data.medals_long()

# Build components
app = Dash(__name__, external_stysheets=[dbc.themes.VAPOR])
mytitle = dcc.Markdown(children='# App that analyzes Olympic medals')
mygraph = dcc.Graph(figures={})
dropdown = dcc.Dropdown(options = ['Bar Plot', 'Scatter Plot'],
                        value = 'Bar Plot', # displated when page loads
                        clearable=False
)

# Custom the Layout
app.layout = dbc.Container([mytitle, mygraph, dropdown])

# callback
@app.callback(
    Output(mygraph, component_property='figure'),
    Input(dropdown, component_property='value')
)
def update_graph(user_input):
    if user_input == 'Bar Plot':
        