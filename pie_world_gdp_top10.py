
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

with open('./data_1/2021世界各国GDP排名.csv', 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    world_rank = []
    country_region = []
    continent = []
    gdp = []
    i = -1
    for line in csv_reader:
        world_rank.append(line[0])
        country_region.append(line[1])
        gdp.append(line[3])

    # 2021年世界各国GDP排名前九，与其他
    pyplt = py.offline.plot
    labels = country_region[2:11]
    labels.append("其他")
    #制作饼图需要对gdp数据进行处理
    gdp_num=[]
    j=-1
    others=0
    for gdp_item in gdp:
        j+=1
        if j>1:
            gdp_num_item=gdp_item.split('(')[0]
            gdp_temp=gdp_num_item[0:-2]
            # gdp_temp=gdp_num_item.strip('亿')
            # print(gdp_temp)
            gdp_num.append(float(gdp_temp))
    k=0
    for temp in gdp_num:
        if k>=9:
            others += temp
        k += 1
    values=gdp_num[1:10]
    values.append(others)
    trace = [go.Pie(labels=labels, values=values)]
    layout = go.Layout(
        title='2021年世界各国GDP排名前九名占比'
    )
    fig = go.Figure(data=trace, layout=layout)
    pyplt(fig, filename='./produced_data/2021年世界各国GDP排名前九名占比.html', auto_open=False)
    print("输出2021年世界各国GDP排名前九名占比.html")