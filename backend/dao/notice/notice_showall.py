import pymysql
from settings import ip


# 展示公告列表，成功则返回notice表中所有内容和true，失败则返回none和false
# 返回数据格式为：notice_id,user_id,user_name,notice_content,notice_title,notice_level,notice_create_time
def show(ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "select * from notice"
        cursor.execute(sql)
        data = cursor.fetchall()
        # result用来存放处理后的公告数据
        result = (())
        # 处理每条公告的创建时间，从timestamp转换为string
        for i in data[::-1]:
            # 获取当前公告的创建日期和时间，并转为字符串
            date = str(i[5].date())
            time = str(i[5].time())
            # 根据user_id索引员工姓名
            sql = 'select user_name from user where user_id = %d' % (i[1])
            cursor.execute(sql)
            name = cursor.fetchone()
            # 用元组存放各条公告的数据，按照如下顺序
            # notice_id    [0]     user_id         [1]
            # user_name    [2]     notice_content  [3]
            # notice_title [4]     notice_level    [5]
            # notice_create_time   [6]
            res = ((i[0], i[1], name[0], i[2], i[3], i[4], date + " " + time),)
            # 元组拼接为结果
            result = result + res
    except:
        cursor.close()
        db.close()
        return None, False
    cursor.close()
    db.close()
    return result, True

# ip = '124.70.200.142'
# user_id = 1
# content = '111'
# title = '1111'
# notice_level = 1
# print(show(ip))
