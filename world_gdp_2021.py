
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

    rank_top10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fig = go.Figure(data=[go.Table(header=dict(values=['2021年世界排名', '国家或地区', 'GDP']),
                                   cells=dict(
                                       values=[rank_top10, country_region[2:12], gdp[2:12]]))
                          ])

    # 保存照片用pio这条
    # pio.write_image(fig, './produced_data/2010年世界各国GDP排名前十名.jpg')
    # 保存html用plotly这条
    plotly.offline.plot(fig, filename="./produced_data/2021年世界各国GDP排名前十名.html", auto_open=False)
    print("2021年世界各国GDP排名.hmtl输出成功")