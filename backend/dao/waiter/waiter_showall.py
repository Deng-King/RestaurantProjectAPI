import pymysql
from settings import ip


# 显示所有准备上菜的菜品列表及其对应的桌号、订单号，成功返回数据和true，失败返回none和false
# 数据： food_name,food_num,order_id,order_table,food_state
def show(ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 连接food、orderinfo、orderlist三个表，索引出所有准备上菜的菜品列表及其相关信息
        # food_name,food_num,order_id,order_table,food_state
        sql = "select a.food_name,b.food_num,c.order_id,c.order_table,b.food_state from food a, orderinfo b, orderlist c " \
              "where a.food_id=b.food_id and c.order_id=b.order_id and c.order_state=0 and b.food_state =1 "
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return None, False
    return result, True

# ip = '124.70.200.142'
# print(show(ip))
