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

#由于文件中中含有字符串，所以需要逐行读出，将字符串分割，接着再形成新的df
#2010年世界各国GDP排名,表格

with open('./data_1/2010世界各国GDP排名.csv', 'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    world_rank = []
    country_region = []
    continent = []
    gdp = []
    i=-1
    for line in csv_reader:
        world_rank.append(line[0])
        country_region.append(line[1])
        continent.append(line[2])
        gdp.append(line[3])

    fig = go.Figure(data=[go.Table(header=dict(values=['2010年世界排名', '国家或地区','所在大洲','人均GDP(美元计)']),
                               cells=dict(values=[world_rank[1:11],country_region[1:11],continent[1:11],gdp[1:11]]))
                      ])
    #保存照片用pio这条
    # pio.write_image(fig, './produced_data/2010年世界各国GDP排名前十名.jpg')
    #保存html用plotly这条
    plotly.offline.plot(fig, filename="./produced_data/2010年世界各国GDP排名前十名.html",auto_open=False)
    print("2010年世界各国GDP排名.hmtl输出成功")