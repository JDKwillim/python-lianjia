import pandas as pd

import numpy as np

data = pd.read_csv("data/shanghai3.csv")
# 缺失值查看  ----无缺失值\
data.info()
print(data.isnull().sum())
print(data.duplicated(keep='first').sum())
data.drop_duplicates(inplace=True)
print(data.describe())
#
# # TODO 房屋朝向
# data.loc[data['房屋朝向'] == '简装', '房屋朝向'] = '南北'
# data.loc[data['房屋朝向'] == '毛坯', '房屋朝向'] = '南北'
# data.loc[data['房屋朝向'] == '精装', '房屋朝向'] = '南北'
# #
# #
# data['房屋朝向'] = data['房屋朝向'].str.replace('南 北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西 东', '东西')
# data['房屋朝向'] = data['房屋朝向'].str.replace('北 西', '西北')
#
# data['房屋朝向'] = data['房屋朝向'].str.replace('南 西', '西南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('北 东', '东北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 北', '东北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西 西南', '西南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('北 南', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东西 南', '东西')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南 南 北', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 北 南', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南 西 南 南 北', '东西')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西南 南 北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 西 北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 东南 南', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东西南南', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南 南北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 南', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('南东北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西南南', '西南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('南 东', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 东北北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('南 东南', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西南 南北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南 东北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西北', '西北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东西南北', '南北')
# data['房屋朝向']=data['房屋朝向'].str.replace('东南 西南北','南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西 南北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西 南', '西南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南南', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南 西南北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西南北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西西南', '西南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 东南', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西 北', '西北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 西', '东西')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东西南 北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南 南', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西南 南', '西南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('南西北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西南西北', '西北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西南 北', '南北')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西南北', '南北')
#
# data['房屋朝向'] = data['房屋朝向'].str.replace('东西南', '南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东南东南', '东南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('东 东西南', '南')
# data['房屋朝向'] = data['房屋朝向'].str.replace('西北 西北', '西北')
# # TODO 户型结构
# data.loc[data['户型结构']=='194.76㎡','户型结构']='平层'
# data.loc[data['户型结构']=='162.17㎡','户型结构']='平层'
# data.loc[data['户型结构']=='340.93㎡','户型结构']='平层'
# data.loc[data['户型结构']=='212.84㎡','户型结构']='复式'
# data.loc[data['户型结构']=='149.23㎡','户型结构']='平层'
# data.loc[data['户型结构']=='288.36㎡','户型结构']='平层'
# data.loc[data['户型结构']=='260㎡','户型结构']='平层'
# data.loc[data['户型结构']=='171.31㎡','户型结构']='平层'
#
# data.loc[data['户型结构']=='173.9㎡','户型结构']='平层'
# data.loc[data['户型结构']=='278.17㎡','户型结构']='平层'
# data.loc[data['户型结构']=='288㎡','户型结构']='平层'
# data.loc[data['户型结构']=='244.03㎡','户型结构']='复式'
# data.loc[data['户型结构']=='287.18㎡','户型结构']='平层'
# data.loc[data['户型结构']=='273.28㎡','户型结构']='平层'
# data.loc[data['户型结构']=='213.53㎡','户型结构']='平层'
# data.loc[data['户型结构']=='398㎡','户型结构']='平层'
#
# data.loc[data['户型结构']=='357.94㎡','户型结构']='平层'
# data.loc[data['户型结构']=='309.66㎡','户型结构']='平层'
# data.loc[data['户型结构']=='310.05㎡','户型结构']='平层'
# data.loc[data['户型结构']=='158.48㎡','户型结构']='复式'
# data.loc[data['户型结构']=='156.9㎡','户型结构']='平层'
# data.loc[data['户型结构']=='516.26㎡','户型结构']='平层'
# data.loc[data['户型结构']=='316.83㎡','户型结构']='平层'
# data.loc[data['户型结构']=='266.1㎡','户型结构']='平层'
#
# data.loc[data['户型结构']=='316.61㎡','户型结构']='平层'
# data.loc[data['户型结构']=='403.3㎡','户型结构']='平层'
# data.loc[data['户型结构']=='202.9㎡','户型结构']='平层'
# data.loc[data['户型结构']=='133.85㎡','户型结构']='复式'
# data.loc[data['户型结构']=='282㎡','户型结构']='平层'
# data.loc[data['户型结构']== '203.4㎡','户型结构']='平层'
# data.loc[data['户型结构']=='113.11㎡','户型结构']='平层'
# data.loc[data['户型结构']=='116.44㎡','户型结构']='平层'
#
# data.loc[data['户型结构']=='300㎡','户型结构']='平层'
# data.loc[data['户型结构']=='301㎡','户型结构']='平层'
# data.loc[data['户型结构']=='335㎡','户型结构']='平层'
# data.loc[data['户型结构']=='227㎡','户型结构']='复式'
# data.loc[data['户型结构']=='104.62㎡','户型结构']='平层'
# data.loc[data['户型结构']== '358.23㎡','户型结构']='平层'
# data.loc[data['户型结构']=='109.48㎡','户型结构']='平层'
# data.loc[data['户型结构']=='175.81㎡','户型结构']='平层'
#
# data.loc[data['户型结构']=='197.57㎡','户型结构']='平层'
# data.loc[data['户型结构']=='447.64㎡','户型结构']='平层'
# data.loc[data['户型结构']=='262.83㎡','户型结构']='平层'
# data.loc[data['户型结构']=='323.39㎡','户型结构']='复式'
# data.loc[data['户型结构']== '356.3㎡','户型结构']='平层'
#
#
# data.loc[data['建筑类型']== '暂无数据','建筑类型']='板塔结合'
# data.loc[data['建筑类型']== '未知结构','建筑类型']='砖混结构'
# data.loc[data['建筑类型']== '框架结构','建筑类型']='板塔结合'
# data.loc[data['建筑类型']== '混合结构','建筑类型']='砖混结构'
# data.loc[data['建筑类型']== '平房','建筑类型']='砖混结构'
#
# data.loc[data['装修情况'] == '有', '装修情况'] = '精装'
# data.loc[data['装修情况'] == '钢混结构', '装修情况'] = '精装'
# data.loc[data['装修情况'] == '砖混结构', '装修情况'] = '简装'
#
# data.loc[data['装修情况'] == '混合结构', '装修情况'] = '精装'
# data.loc[data['装修情况'] == '无', '装修情况'] = '精装'
# data.loc[data['装修情况'] == '框架结构', '装修情况'] = '简装'
#
# data.loc[data['装修情况'] == '未知', '装修情况'] = '暂无数据'
# data.loc[data['装修情况'] == '商水', '装修情况'] = '精装'
# data.loc[data['装修情况'] == '未知结构', '装修情况'] = '简装'
# data.loc[data['装修情况'] == '其他', '装修情况'] = '简装'
#
# data.loc[data['梯户比例'] == '精装', '梯户比例'] = '三梯四户'
# data.loc[data['梯户比例'] == '简装', '梯户比例'] = '一梯四户'
# data.loc[data['梯户比例'] == '毛坯', '梯户比例'] = '两梯四户'
# data.loc[data['梯户比例'] == '商水', '梯户比例'] = '三梯四户'
# data.loc[data['梯户比例'] == '商电', '梯户比例'] = '三梯四户'
#
# data.loc[data['配备电梯']=='暂无数据','配备电梯']='有'
# data.loc[data['配备电梯']=='集中供暖','配备电梯']='无'
# data.loc[data['配备电梯']=='自供暖','配备电梯']='有'
# data.loc[data['配备电梯']=='2.56元/m3','配备电梯']='有'
# data.loc[data['配备电梯']=='2.58元/m3','配备电梯']='有'
# data.loc[data['配备电梯']=='商电','配备电梯']='无'
# data.loc[data['配备电梯']=='未知','配备电梯']='有'
#
# data.loc[data['配备电梯']=='3.48元/m3','配备电梯']='有'
# data.loc[data['配备电梯']=='3元/m3','配备电梯']='无'
# data.loc[data['配备电梯']=='3.45元/m3','配备电梯']='有'
# data.loc[data['配备电梯']=='3.77元/m3','配备电梯']='有'
# data.loc[data['配备电梯']=='6元/m3','配备电梯']='有'
# data.loc[data['配备电梯']=='2.7元/m3','配备电梯']='无'
# data.loc[data['配备电梯']=='2元/m3','配备电梯']='有'
#
# data.loc[data['配备电梯']=='联排','配备电梯']='有'
# data.loc[data['配备电梯']=='叠拼','配备电梯']='有'
# data.loc[data['配备电梯']=='双拼','配备电梯']='有'
# data.loc[data['配备电梯']=='独栋','配备电梯']='暂无数据'
#
# print(data['建筑类型'].unique())
#
#
# data.loc[data['所在区市'] == '浦东', '所在区市'] = '浦东新'
#
# data.to_csv('上海二手房2.csv', index=False, encoding='utf8')

