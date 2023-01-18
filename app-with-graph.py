from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

# Add data
df = px.data.medals_long()

# Build components
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
mytitle = dcc.Markdown(children='# App that analyzes Olympic medals')
mygraph = dcc.Graph(figure={})
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
        fig = px.bar(data_frame=df,x="nation", y="count",color="medal")
    elif user_input == 'Scatter Plot':
        fig = px.scatter(data_frame=df, x="count", y="nation", color="metal", symbol="metal")

    return fig

# run app
if __name__ == '__main__':
    app.run_server(port=8051)