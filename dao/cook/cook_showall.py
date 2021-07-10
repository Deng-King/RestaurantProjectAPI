import pymysql


def show(ip):   # return food_name,food_num,order_id,order_table,food_state
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select a.food_name,b.food_num,c.order_id,c.order_table,b.food_state from food a, orderinfo b, orderlist c " \
          "where a.food_id=b.food_id and c.order_id=b.order_id and c.order_state=0 and b.food_state =0 "
    try:
        cursor.execute(sql)
        result=cursor.fetchall()
    except:
        db.rollback()
    # result = (())
    # sql = 'select * from orderlist where order_state=0'
    # cursor.execute(sql)
    # orderlist = cursor.fetchall()
    # for i in orderlist:
    #     table_num = i[1]
    #     # print(table_num)
    #     sql = 'select * from orderinfo where order_id=%d and food_state=1' % (i[0])
    #     cursor.execute(sql)
    #     orderinfo = cursor.fetchall()
    #     for j in orderinfo:
    #         sql = 'select food_name from food where food_id=%d' % (j[1])
    #         cursor.execute(sql)
    #         food_name = cursor.fetchone()
    #         # print(food_name)
    #         temp = ((food_name[0], j[2], j[0], table_num, j[3]),)  # 菜品名称、菜品数量、订单号、属于哪一桌、菜的状态
    #         result = result + temp
    cursor.close()
    db.close()
    return result

# ip = '124.70.200.142'
# print(show(ip))
