import pymysql
from settings import ip


# 后厨展示菜品列表
# 返回 food_name,food_num,order_id,order_table,food_state
def show(ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 显示后厨列表，根据orderlist中的order_id来索引orderinfo中对应的food_id、food_state、food_num，并根据food_id在表food中索引food_name
        sql = "select a.food_name,b.food_num,c.order_id,c.order_table,b.food_state from food a, orderinfo b, orderlist c " \
              "where a.food_id=b.food_id and c.order_id=b.order_id and c.order_state=0 and b.food_state =0 "
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            # 若执行语句出错，则回滚到之前的状态
            db.rollback()
        # 关闭游标和数据库
        cursor.close()
        db.close()
        print(result)
    except:
        return None, False
    # 返回后厨做菜列表和操作成功
    return result, True

