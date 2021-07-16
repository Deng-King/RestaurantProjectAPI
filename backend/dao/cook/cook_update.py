import pymysql
from settings import ip


# 厨师将食物状态改变为准备上菜，输入food_id和order_id，返回true或false
def update(food_id, order_id, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 后厨将食物状态从正在烹饪改为准备上菜，即把food_state由0改为1
    # 根据输入的order_id和food_id来索引相应订单对应的菜品，并更改状态
    sql = 'update orderinfo set food_state=1 where order_id=%d and food_id=%d and food_state=0' % (order_id, food_id)
    try:
        # 执行语句，提交结果，关闭数据库，并返回true
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return True
    except:
        # 若执行语句出错，则回滚到之前的状态，关闭数据库，并返回true
        db.rollback()
        cursor.close()
        db.close()
        return False

