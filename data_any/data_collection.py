import requests
import parsel
import csv

f = open('上海.csv', mode='a', encoding='utf8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '小区名称',
    '所在区市',
    '详细地址',
    '总价',
    '单价',
    '房屋户型',
    '房屋朝向',
    '建筑面积',
    '所在楼层',
    '户型结构',
    '建筑类型',
    '装修情况',
    '梯户比例',
    '配备电梯',
    '挂牌时间',
    '交易权属',
    '房屋用途',
    '房屋年限',
    '产权所属',
    '详情页'

])
csv_writer.writeheader()
city = {
    'pudong': 100, 'minhang': 100, 'baoshan': 100,
    'xuhui': 100, 'putuo': 100, 'yangpu': 100,
    'changning': 100, 'songjiang': 100, 'jiading': 100,
    'huangpu': 59, 'jingan': 100, 'hongkou': 84,
    'qingpu': 98, 'fengxian': 65, 'jinshan': 34,
    'chongming': 20

}
for a, b in city.items():
    for page in range(1, b):
        url = f"https://sh.lianjia.com/ershoufang/{a}/pg{page}"
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/109.0.0.0 '
                          'Safari/537.36 '
        }
        request = requests.get(url=url, headers=headers)
        # 获取网页信息
        # print(request)
        selector = parsel.Selector(request.text)
        # print(selector)
        lis = selector.css('.sellListContent li .info')
        for html in lis:
            title = html.css('.title a::text').get()
            Link = html.css(' .title a::attr(href)').get()
            # print(Link)

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/109.0.0.0 '
                              'Safari/537.36 '
            }
            re = requests.get(url=Link, headers=headers)
            selector = parsel.Selector(re.text)
            # 核心卖点
            Core_selling_points = selector.css(
                'body > div.m-content > div.box-l > div:nth-child(2) > div > div:nth-child(2) > div.content::text').get()
            # print(Core_selling_points)
            # 总价
            total_price = selector.css('.overview .content .price-container .price .total::text').get()
            # 单价
            unit_price = selector.css('body > div.overview > div.content > div.price-container > div > div.text > '
                                      'div.unitPrice > span::text').get()
            name = selector.css('.overview .content .aroundInfo .communityName .info::text').get()
            # 所在区市
            D_city = selector.css(
                'body > div.overview > div.content > div.aroundInfo > div.areaName > span.info > a:nth-child('
                '1)::text').get()
            # 详细地址
            address = selector.css(
                'body > div.overview > div.content > div.aroundInfo > div.areaName > span.info > a:nth-child('
                '2)::text').get()
            # 链家编号
            number = selector.css(
                'body > div.overview > div.content > div.aroundInfo > div.houseRecord > span.info::text').get()
            # TODO 基本属性
            base = selector.css('.baseinform .introContent .base li::text').getall()

            # print(base)
            # 房屋户型
            House_type = base[0]
            # 所在楼层
            floor = base[1]
            # 建筑面积
            area = base[2]
            # 户型结构
            House_type_structure = base[3]
            # 套呢面积
            inside_area = base[4]
            # 建筑类型
            Building_type = base[5]
            # 房屋朝向
            House_orientation = base[6]
            # 建筑结构
            building_structure = base[7]
            # 装修情况
            Decoration = base[-3]
            # 体户比例
            proportion = base[-2]
            # 配备电梯
            Equipped_elevator = base[-1]
            # TODO 交易权属
            transaction = selector.css('.baseinform .introContent .transaction .content span::text').getall()
            # print(transaction)
            # 挂牌时间----年
            time = transaction[1]
            time_year = int(time.split("-")[0])
            # 交易权属
            Transaction_ownership = transaction[3]
            # 上次交易
            # 房屋用途
            House_use = transaction[7]
            # 房屋年限
            House_age = transaction[9]
            # 产权所属
            Ownership = transaction[11]
            dit = {
                '标题': title,
                '小区名称': name,
                '所在区市': D_city,
                '详细地址': address,
                '总价': total_price,
                '单价': unit_price,
                '房屋户型': House_type,
                '房屋朝向': House_orientation,
                '建筑面积': area,
                '所在楼层': floor,
                '户型结构': House_type_structure,
                '建筑类型': Building_type,
                '装修情况': Decoration,
                '梯户比例': proportion,
                '配备电梯': Equipped_elevator,
                '挂牌时间': time_year,
                '交易权属': Transaction_ownership,
                '房屋用途': House_use,
                '房屋年限': House_age,
                '产权所属': Ownership,
                '详情页': Link
            }
            csv_writer.writerow(dit)
        print("**********************")
        print(f"{a}地区第{page}页下载完毕")
