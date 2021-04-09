import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html
import plotly.graph_objects as go
from pandas_datareader import data as web 
from datetime import datetime as dt

import pandas as pd
import yfinance as yf


data = {'AMZN': yf.Ticker('AMZN').history(period = '1y'),\
        'AAPL': yf.Ticker('AAPL').history(period = '1y'),\
        'GOOG': yf.Ticker('GOOG').history(period = '1y')\
        }

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("My name is Bot, I'm a James. I also have a license to Plot.", style={'text-align':'center'}),

    dcc.Dropdown(id = 'Select_Stock',
                options = [{'label': 'Amazon', 'value':'AMZN'}, 
                            {'label': 'Apple', 'value':'AAPL'},
                            {'label': 'Google', 'value':'GOOG'}],
                multi = False,
                value = 'AMZN',
                style = {'width':'40%'}),
    
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='Stock_Vis', figure = {})
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='Stock_Vis', component_property='figure')],
    [Input(component_id='Select_Stock', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    df = data[option_slctd]

    # Plotly Express
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    fig.update_layout(paper_bgcolor="black", plot_bgcolor="black")

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig

if __name__ == '__main__':
    app.run_server(debug = True)
