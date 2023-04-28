import pandas as pd
import numpy as np
import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import SymbolType, ThemeType

data = pd.read_csv('上海二手房2.csv')


def x():
    df = data.groupby(['建筑类型'])['单价'].agg([
        'size', 'mean', 'max', 'min'
    ]).round(2)
    df = df.rename(columns={
        'size': '数量', 'mean': '平均价格', 'max': '最大值', 'min': '最小值'
    })
    # print(df['平均价格'].values.tolist())
    c = (
        Bar()
        .add_xaxis(df.index.tolist())
        .add_yaxis("平均价格", df['平均价格'].values.tolist())
        .add_yaxis("最大值", df['最大值'].values.tolist())
        .add_yaxis("最小值", df['最小值'].values.tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="建筑类型对单价影响", subtitle=""),
            brush_opts=opts.BrushOpts(),
        )
        .render("可视化结果/建筑类型对单价影响.html")
    )


def x1():
    df = data.groupby(['装修情况'])['单价'].agg([
        'size', 'mean', 'max', 'min'
    ]).round(2)
    df = df.rename(columns={
        'size': '数量', 'mean': '平均价格', 'max': '最大值', 'min': '最小值'
    })
    # print(df['平均价格'].values.tolist())
    c = (
        Bar()
        .add_xaxis(df.index.tolist())
        .add_yaxis("平均价格", df['平均价格'].values.tolist())
        .add_yaxis("最大值", df['最大值'].values.tolist())
        .add_yaxis("最小值", df['最小值'].values.tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="装修情况对单价影响", subtitle=""),
            brush_opts=opts.BrushOpts(),
        )
        .render("可视化结果/装修情况对单价影响.html")
    )


def x2():
    df = data.groupby(['房屋用途'])['单价'].agg([
        'size', 'mean', 'max', 'min'
    ]).round(2)
    df = df.rename(columns={
        'size': '数量', 'mean': '平均价格', 'max': '最大值', 'min': '最小值'
    })
    # print(df['平均价格'].values.tolist())
    c = (
        Bar()
        .add_xaxis(df.index.tolist())
        .add_yaxis("平均价格", df['平均价格'].values.tolist())
        .add_yaxis("最大值", df['最大值'].values.tolist())
        .add_yaxis("最小值", df['最小值'].values.tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="房屋用途对单价影响", subtitle=""),
            brush_opts=opts.BrushOpts(),
        )
        .render("可视化结果/房屋用途对单价影响.html")
    )


if __name__ == '__main__':
    x()
    x1()
    x2()
