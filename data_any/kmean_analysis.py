import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import SymbolType, ThemeType

df = pd.read_csv('jieguo.csv', usecols=[2, 4, 5, 8, 21])
df['建筑面积'] = df['建筑面积'].apply(lambda a: a[:-1]).astype('float')

# 按照类别进行分组，并计算单价、面积、总价的平均值
agg_data = df.groupby('类别', as_index=False)['单价', '建筑面积', '总价'].mean().round(2)

# 获取每种类别的数量
count_data = df['类别'].value_counts().reset_index()
count_data.columns = ['类别', '数量']

# 合并两个聚合结果
result = pd.merge(agg_data, count_data, on='类别')
print(result)


# df.info()
# print(df.head(5))
def category_0():
    category = df.loc[df['类别'] == 0]
    # print(category)
    category0 = category.groupby(['所在区市']).count()['单价']
    x = category0.index.tolist()
    y = category0.values.tolist()
    # print(x, y)
    new_x = [x + '区' for x in x]
    print(category0)
    c = (
        Map(init_opts=opts.InitOpts(width="1500px", height="800px"))
        .add("上海", [list(z) for z in zip(new_x, y)], "上海")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="0类"), visualmap_opts=opts.VisualMapOpts()
        )
        .render("KMeans结果/第0类分布.html")
    )


def category_1():
    category = df.loc[df['类别'] == 1]
    # print(category)
    category1 = category.groupby(['所在区市']).count()['单价']
    x = category1.index.tolist()
    y = category1.values.tolist()
    # print(x, y)
    new_x = [x + '区' for x in x]
    print(category1)
    c = (
        Map(init_opts=opts.InitOpts(width="1500px", height="800px"))
        .add("上海", [list(z) for z in zip(new_x, y)], "上海")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="1类"), visualmap_opts=opts.VisualMapOpts()
        )
        .render("KMeans结果/第1类分布.html")
    )


def category_2():
    category = df.loc[df['类别'] == 2]
    # print(category)
    category2 = category.groupby(['所在区市']).count()['单价']
    x = category2.index.tolist()
    y = category2.values.tolist()
    # print(x, y)
    new_x = [x + '区' for x in x]
    print(category2)
    c = (
        Map(init_opts=opts.InitOpts(width="1500px", height="800px"))
        .add("上海", [list(z) for z in zip(new_x, y)], "上海")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2类"), visualmap_opts=opts.VisualMapOpts()
        )
        .render("KMeans结果/第2类分布.html")
    )


def category_3():
    category = df.loc[df['类别'] == 3]
    # print(category)
    category3 = category.groupby(['所在区市']).count()['单价']
    x = category3.index.tolist()
    y = category3.values.tolist()
    # print(x, y)
    new_x = [x + '区' for x in x]
    print(category3)
    c = (
        Map(init_opts=opts.InitOpts(width="1500px", height="800px"))
        .add("上海", [list(z) for z in zip(new_x, y)], "上海")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="3类"), visualmap_opts=opts.VisualMapOpts()
        )
        .render("KMeans结果/第3类分布.html")
    )


if __name__ == '__main__':
    category_0()
    category_1()
    category_2()
    category_3()
