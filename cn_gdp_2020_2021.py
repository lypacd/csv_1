import plotly
import plotly.graph_objects as go
import plotly as py
import plotly.graph_objs as go
import csv
import plotly as py
import plotly.graph_objs as go
import numpy as np
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from plotly.graph_objs import Pie
from plotly.graph_objs import *
import plotly.offline


file_name1='./data_1/2010世界各国GDP排名.csv'
file_name2='./data_1/2021世界各国GDP排名.csv'
file_name3='./data_1/2021中国人均GDP排名.csv'
file_name4='./data_1/世界人口排行榜.csv'

with open('./data_1/2021中国人均GDP排名.csv', 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    cn_rank = []
    province_city = []
    gdp2020 = []
    gdp2021 = []
    i = -1
    for line in csv_reader:
        cn_rank.append(line[0].strip('\n').strip('\t'))
        province_city.append(line[1].strip('\n').strip('\t'))
        gdp2020.append(line[2].strip('\n').strip('\t'))
        gdp2021.append(line[3].strip('\n').strip('\t'))
    # print("打印")

    trace0 = go.Bar(
        x=province_city[2:-1],
        y=gdp2020[2:-2],
        name="2020年中国各省市人均GDP"
    )

    trace1 = go.Bar(
        x=province_city[2:-1],
        y=gdp2021[2:-2],
        name="2021年中国各省市人均GDP"
    )

    fig = go.Figure(data=[trace0, trace1])
    pyplt = py.offline.plot
    # fig = go.Figure(data=trace, layout=layout)
    pyplt(fig, filename='./produced_data/2020年和2021年中国人均GDP对比.html' ,auto_open=False)
    print("输出2020年和2021年中国人均GDP对比.html成功")