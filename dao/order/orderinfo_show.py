import pymysql
#from settings import ip

def show():
    # 返回格式：元组套元组
    # order_id
    # food_id
    # food_num
    # food_state
    # 打开数据库连接
    try:
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select * from orderinfo"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        return None,False
    return data,True


ip = '124.70.200.142'
print(show())
