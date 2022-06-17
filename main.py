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
def f1():
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


#世界各国GDP，直方图和饼图
def f2():
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

        rank_top10=[1,2,3,4,5,6,7,8,9,10]
        fig = go.Figure(data=[go.Table(header=dict(values=['2021年世界排名', '国家或地区','GDP']),
                                       cells=dict(
                                           values=[rank_top10, country_region[2:12], gdp[2:12]]))
                              ])

        # 保存照片用pio这条
        # pio.write_image(fig, './produced_data/2010年世界各国GDP排名前十名.jpg')
        # 保存html用plotly这条
        plotly.offline.plot(fig, filename="./produced_data/2021年世界各国GDP排名前十名.html", auto_open=False)
        print("2021年世界各国GDP排名.hmtl输出成功")

        #2021年世界各国GDP排名前九，与其他
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

#中国人均FDP排名前十，直方图，比较2020和2021
def f3():
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
        print("打印")

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
        pyplt(fig, filename='./produced_data/2020年和2021年中国人均GDP对比.html',auto_open=False)
        print("输出2020年和2021年中国人均GDP对比.html成功")
#世界人口排行榜，折线图

def f4():
    with open('./data_1/世界人口排行榜.csv', 'r',encoding='utf8') as f:
        csv_reader = csv.reader(f)
        world_rank = []
        country_region = []
        population = []
        increasing_rate= []
        i=-1
        for line in csv_reader:
            world_rank.append(line[0])
            country_region.append(line[1])
            population.append(line[2])
            increasing_rate.append(line[3])

        # fig = go.Figure(data=[go.Table(header=dict(values=['世界排名', '国家或地区','人口数量','增长率']),
        #                            cells=dict(values=[world_rank[1:-1],country_region[1:-1],population[1:-1],increasing_rate[1:-1]]))
        #                   ])
        #

        # 折线图
        # trace0 = Scatter(
        #
        #     x=country_region[1:-1],
        #
        #     y=population[1:-1]
        #
        # )
        #
        # trace1 = Scatter(
        #
        #     x=country_region[1:-1],
        #
        #     y=increasing_rate[1:-1]
        #
        # )
        trace0 = go.Bar(
                x=country_region[1:-1],
                y=population[1:-1],
            name="各国人口数量"
        )

        trace1 = go.Bar(
                x=country_region[1:-1],
                y=increasing_rate[1:-1],
            name="各国人口增长率"
        )

        fig = go.Figure(data=[trace0, trace1])
        pyplt = py.offline.plot
        pyplt(fig, filename='./produced_data/世界人口排行榜.html', auto_open=False)
        print("世界人口排行榜.hmtl输出成功")

#测试
f1()
f2()
f3()
f4()