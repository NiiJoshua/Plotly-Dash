from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc

# Build components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children = '')
myinput = dbc.Input(value='# Hello World - First interactive app')

# Layout
app.layout = dbc.Container([mytext, myinput])

# Callback
@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)

def update_title(user_input): # arguements come from the component property of the in Input
    return user_input # returned objects are assigned to the component property of the Output

# Run app
if __name__ == '__main__':
    app.run_server(port=8052)