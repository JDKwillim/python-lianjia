import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import SymbolType, ThemeType

data = pd.read_csv("上海二手房2.csv")
# 缺失值查看  ----无缺失值\
#
# print(data.isnull().sum())
#
# data.info()
# # 将建筑面积单位去掉
data['建筑面积'] = data['建筑面积'].apply(lambda a: a[:-1]).astype('float')


# print(data['建筑面积'])
# print(data.describe())
# # 统计每个市区二手房数据


# print(city_group)

# TODO 可视化地图上海各区二手房分布 ------转化为列表[上街区,123]
def Map_num():
    city_group = data.groupby('所在区市').count()['小区名称']

    x = city_group.index.tolist()
    y = city_group.values.tolist()
    # print(x, y)
    new_x = [x + '区' for x in x]
    Map_count = (
        Map(init_opts=opts.InitOpts(width="1500px", height="800px"))
        .add('上海', [list(z) for z in zip(new_x, y)], "上海")
        .set_global_opts(

            title_opts=opts.ComponentTitleOpts(title='上海市二手房各区分布'),
            visualmap_opts=opts.VisualMapOpts(max_=3500)
        )
    )
    Map_count.render("可视化结果\上海各区二手房分布.html")


# TODO 上海市各区二手房的平均价格

def mean_price():
    mean_price_city = data.groupby('所在区市')['总价'].mean().astype(int)
    mean_price_city_sort = mean_price_city.sort_values(ascending=False)
    # print(mean_price_city)
    mean_price_city_sort_x = mean_price_city_sort.index.tolist()
    mean_price_city_sort_y = mean_price_city_sort.values.tolist()
    # print(mean_price_city_sort_x,mean_price_city_sort_y)
    mean_price_city_b = (
        Bar()
        .add_xaxis(mean_price_city_sort_x)
        .add_yaxis("单位(万元)", mean_price_city_sort_y)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="上海二手房平均价格(四舍五入)"),
            datazoom_opts=opts.DataZoomOpts(),
        )
        .render("可视化结果\上海市各区二手房平均总价.html")
    )


# TODO 上海市各区二手房的平均面积
def mean_area():
    mean_area_city = data.groupby('所在区市')['建筑面积'].mean().astype(int)
    # print(mean_area_city)
    mean_area_city_x = mean_area_city.index.tolist()
    mean_area_city_y = mean_area_city.values.tolist()
    mean_area_city_c = (
        EffectScatter()
        .add_xaxis(mean_area_city_x)
        .add_yaxis("单位㎡", mean_area_city_y, symbol=SymbolType.ARROW)
        .set_global_opts(title_opts=opts.TitleOpts(title="上海市各区二手房的平均面积"))
        .render("可视化结果\上海市各区二手房的平均面积.html")
    )


# TODO 上海市各区二手房平均单价
def mean_unit_price():
    mean_unit_price_city = data.groupby('所在区市')['单价'].mean().astype(int)
    # print(mean_unit_price_city)
    mean_unit_price_city_x = mean_unit_price_city.index.tolist()
    mean_unit_price_city_y = mean_unit_price_city.values.tolist()
    c = (
        Line()
        .add_xaxis(mean_unit_price_city_x)
        .add_yaxis("单位(元/平方米)", mean_unit_price_city_y, is_smooth=True)
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="上海市各区二手房平均单价"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
        )
        .render("可视化结果\上海市各区二手房平均单价.html")
    )


# TODO 房屋户型数据>100
def houseType():
    # print(data['房屋户型'].unique())
    house_type = data.groupby('房屋户型').count()['小区名称']
    # print(house_type)
    house_type_index = house_type.index.tolist()
    house_type_values = house_type.values.tolist()
    house_type_list = [list(z) for z in zip(house_type_index, house_type_values)]
    # print(house_type_list)
    new_house_type_x = []
    new_house_type_y = []
    for house_type in house_type_list:
        if house_type[1] > 100:
            new_house_type_x.append(house_type[0])
            new_house_type_y.append(house_type[1])

    house_type_L = (
        Line(init_opts=opts.InitOpts(height="400px", width="1000px"))
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
        .add_xaxis(xaxis_data=new_house_type_x)
        .add_yaxis(
            series_name="123",
            y_axis=new_house_type_y,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .render("可视化结果\房屋户型数据.html")
    )


# TODO 统计每个区的最高房价
def max_min_price():
    city_max_price = data.groupby('所在区市').max()['总价']
    city_min_price = data.groupby('所在区市').min()['总价']
    city_max_price_x = city_max_price.index.tolist()
    city_max_price_y = city_max_price.values.tolist()
    city_min_price_y = city_min_price.values.tolist()
    # print(city_max_price,city_min_price)

    city_group_B = (
        Bar()
        .add_xaxis(city_max_price_x)
        .add_yaxis("最大值", city_max_price_y)
        .add_yaxis("最小值", city_min_price_y)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="各区最大最小值", subtitle="单位(万元)"),
            brush_opts=opts.BrushOpts(),
        )
        .render("可视化结果\各区最大最小值.html")
    )


# TODO 装修情况占比
def Decoration():
    Decoration_data = data.groupby('装修情况').count()['标题']
    Decoration_data_x = Decoration_data.index.tolist()
    Decoration_data_y = Decoration_data.values.tolist()

    data_pair = [list(z) for z in zip(Decoration_data_x, Decoration_data_y)]
    data_pair.sort(key=lambda x: x[1])

    Decoration_P = (
        Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
        .add(
            series_name="装修情况",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="装修情况占比",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
        )
        .render("可视化结果\装修情况占比.html")
    )


# TODO 建筑类型
def Building_type():
    Building_type_data = data.groupby('建筑类型').count()['总价']
    Building_type_data_x = Building_type_data.index.tolist()
    Building_type_data_y = Building_type_data.values.tolist()

    Building_type_data_p = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add(
            "",
            [list(z) for z in zip(Building_type_data_x, Building_type_data_y)],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="建筑类型"))
        .render("可视化结果\建筑类型占比.html")
    )


# TODO 交易权属
def Transaction():
    Transaction_ownership_data = data.groupby('交易权属').count()['总价']
    Transaction_ownership_data_x = Transaction_ownership_data.index.tolist()
    Transaction_ownership_data_y = Transaction_ownership_data.values.tolist()
    House_use_data = data.groupby('房屋用途').count()['总价']
    House_use_data_x = House_use_data.index.tolist()
    House_use_data_y = House_use_data.values.tolist()
    inner_data_pair = [list(z) for z in zip(Transaction_ownership_data_x, Transaction_ownership_data_y)]
    outer_data_pair = [list(z) for z in zip(House_use_data_x, House_use_data_y)]
    (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add(
            series_name="交易权属",
            data_pair=inner_data_pair,
            radius=[0, "30%"],
            label_opts=opts.LabelOpts(position="inner"),
        )
        .add(
            series_name="房屋用途",
            radius=["40%", "55%"],
            data_pair=outer_data_pair,
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            )
        )
        .render("可视化结果\交易权属与房屋用途.html")
    )


# TODO 上海市二手房总价与面积散点图
def price_area():
    total_price = data['总价'].tolist()
    area = data['建筑面积'].tolist()
    S = (
        Scatter(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(total_price)
        .add_yaxis("", area)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="总价与面积"),
            visualmap_opts=opts.VisualMapOpts(max_=1000),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .render("可视化结果\上海市二手房总价与面积散点图r.html")
    )


if __name__ == '__main__':
    # 各市区数量
    Map_num()
    # 平均面积
    mean_area()
    # 单价平均
    mean_unit_price()
    # 总价
    mean_price()
    # 房屋户型前100
    houseType()
    # 每个区最高房价
    max_min_price()
    # 装修情况
    Decoration()
    # 建筑类型
    Building_type()
    # 交易权属
    Transaction()
    # 房价与面积散点
    price_area()
