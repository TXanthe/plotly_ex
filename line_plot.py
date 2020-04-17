# 2.5-1 基本示例
import plotly as py
import plotly.graph_objs as go
import pandas as pd


# input data 
data = pd.read_csv('data/data.csv')

# Basic Line
pyplt = py.offline.plot

SP500 = data['SP500']
oil = data['CrudeOil']
date = data['Date']

trace1 = go.Scatter(
    x = date,
    y = SP500,
    name = 'SP500',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4),
    connectgaps = True
)
trace2 = go.Scatter(
    x = date,
    y = oil
)
layout = dict(
    title = 'SP500&oil',
    xaxis = dict(title = 'Date'),
    yaxis = dict(title = 'profit_rate')
)

fig = dict(data = [trace1, trace2], layout = layout)
pyplt(fig, filename='output/basic-line.html')
