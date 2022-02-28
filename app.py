"""

This module uses dash to plot interactive graph of data set
obtained from seaborn dataframe.


"""
__version__ = '0.1'
__author__= 'Imran Shah'

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import seaborn as sns


df = sns.load_dataset('iris')

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Iris Dataset',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Exploring the Iris dataset with Dash', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    #generate_table(df),

    dcc.Graph(
        id='scatter-plot',
    ),
    html.P('Petal Width:'),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])


@app.callback(
    Output("scatter-plot", "figure"), 
    [Input("range-slider", "value")])
def update_bar_chart(slider_range):
    """
    Creates a scatter-plot with range slider that can be updated interactively
    """
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length", 
        color="species", size='petal_length', 
        hover_data=['petal_width'])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)