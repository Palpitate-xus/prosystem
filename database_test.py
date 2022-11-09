import traceback
import pymysql
import time

current_date = time.strftime("%Y-%m-%d", time.localtime())
filename = "LOG_" + current_date + ".txt"
log_file = open(filename, 'a+')
db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456789',
    database='prosystem'
)


def add_ani():
    temp_ani = input("请输入您想添加的动物名：")
    cur = db.cursor()
    cur.execute("SELECT animal FROM animals")
    ani_data = cur.fetchall()
    if temp_ani in ani_data:
        print("已存在该动物")
    else:
        try:
            cur.execute("INSERT INTO animals(animal) values (\"%s\")"%temp_ani)
            db.commit()
            cur.execute("SELECT id FROM animals WHERE animal='%s'"%temp_ani)
            ani_id = cur.fetchone()
            print("done! 该动物id为%s"%ani_id)
            log_file.write("==========LOG" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "==========\n")
            log_file.write("add动物id: %s, 动物名称: %s\n"%(ani_id[0], temp_ani))
        except:
            db.rollback()
            traceback.print_exc()
            print("数据库操作失败，已回滚操作，请检查数据库连接")

def add_fea():
    temp_fea = input("请输入您想添加的属性名：")
    cur = db.cursor()
    cur.execute("SELECT info FROM features")
    fea_data = cur.fetchall()
    if temp_fea in fea_data:
        print("已存在该属性")
    else:
        try:
            cur.execute("INSERT INTO features(info) values (\"%s\")"%temp_fea)
            db.commit()
            cur.execute("SELECT id FROM features WHERE info='%s'"%temp_fea)
            fea_id = cur.fetchone()
            print("done! 该属性id为%s"%fea_id)
            log_file.write("==========LOG" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "==========\n")
            log_file.write("add属性id: %s, 属性名称: %s\n"%(fea_id[0], temp_fea))
        except:
            db.rollback()
            traceback.print_exc()
            print("数据库操作失败，已回滚操作，请检查数据库连接")

# def list_rules():
#     cur = db.cursor()
#     try:
#         cur.execute("SELECT ")

def list_output(temp = []):
    for i in temp:
        print("{}.\t{}".format(i[0], i[1]))

def add_rule():
    cur = db.cursor()
    try:
        cur.execute("SELECT id,info FROM features")
        data_fea = cur.fetchall()
        cur.execute("SELECT id,animal FROM animals")
        data_ani = cur.fetchall()
        cur.execute("SELECT info,animal FROM features, animals, animals_query WHERE animals_query.animal_id = animals.id and animals_query.feature_id = features.id")
        
        print("现有特征如下：")
        list_output(data_fea)
        print("现有动物如下：")
        list_output(data_ani)
        print("现有规则如下：")
        data_rule = cur.fetchall()
        for i in data_ani:
            temp_fea = ''
            for j in data_rule:
                if str(i[1]) == j[1]:
                    temp_fea += j[0].strip() + ", "
            temp_fea = temp_fea.rstrip(", ")
            temp_fea += ' --> ' + i[1]
            print(temp_fea)

        while(1):
            temp_rule = input("请按以下格式输入新规则(输入0退出)：\n例：有毛发+会下蛋 --> 企鹅则需要输入6 1 5\n")
            if temp_rule == '0':
                break
            log_file.write("==========LOG" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "==========\n")
            log_file.write("add规则: %s\n"%temp_rule)
            temp_rule_list = temp_rule.split()
            sql_list = []
            temp_ani = temp_rule_list[0]
            temp_rul = temp_rule_list[1:]
            for i in temp_rul:
                sql_list.append([temp_ani, i])
            for i in sql_list:
                cur.execute("INSERT INTO animals_query values(%s, %s)"%(i[0], i[1]))
                db.commit()
                print("done!")
        
    except:
        db.rollback()
        traceback.print_exc()
        print("数据库操作失败，已回滚操作，请检查数据库连接")


def query_ani():
    cur = db.cursor()
    try:
        cur.execute("SELECT id, info FROM features")
        data_fea = cur.fetchall()
        print("可选属性如下：")
        list_output(data_fea)
        input_fea = []
        while(1):
            temp_input = input("请输入：")
            if temp_input == '0':
                break
            input_fea.append(temp_input)
        cur.execute("SELECT animal FROM animals, animals_query WHERE animals_query.animal_id = animals.id and animals_query.feature_id = %s"%input_fea[0])
        result = cur.fetchall()
        for i in input_fea:
            cur.execute("SELECT animal FROM animals, animals_query WHERE animals_query.animal_id = animals.id and animals_query.feature_id = %s"%i)
            temp_res = cur.fetchall()
            result = list(set(result) & set(temp_res))
        log_file.write("==========LOG" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "==========\n")
        conditions = []
        for i in input_fea:
            cur.execute("SELECT info FROM features WHERE id = %s"%i)
            conditions.append(cur.fetchall()[0][0].strip())

        print("前提条件为：")
        log_file.write("前提条件为：\n")
        for i in conditions:
            print(i, end=" ")
            log_file.write(i + ' ')
        print('\n')

        print("推理过程如下：")
        log_file.write("\n推理过程如下：\n")
        if len(result) == 0:
            print("根据所给条件无法判断为何种动物")
            log_file.write("根据所给条件无法判断为何种动物\n")
        if len(result) == 1:
            for i in range(len(conditions)-1):
                print(conditions[i], end=", ")
                log_file.write(conditions[i] + ', ')
            print(conditions[-1], end=" --> ")
            log_file.write(conditions[-1] + " --> ")
            print(result[0][0])
            log_file.write(result[0][0] + '\n')
        if len(result) > 1:
            print("该动物可能是：", end="")
            log_file.write("该动物可能是：")
            for i in result:
                print(i[0], end=" ")
                log_file.write(str(i) + ' ')
            print('\n')
            log_file.write('\n')
            print("根据所给条件无法判断为何种动物")
            log_file.write("根据所给条件无法判断为何种动物\n")
            
    except:
        db.rollback()
        traceback.print_exc()
        print("数据库操作失败，已回滚操作，请检查数据库连接")


while(1):
    print("\n1. 推理\n2. 规则操作\n3. 加入属性\n4. 加入动物\n0. 退出程序")
    user_option = input("请输入您想要执行的功能：")
    if user_option == '0':
        break
    if user_option == '1':
        query_ani()
    if user_option == '2':
        add_rule()
    if user_option == '3':
        add_fea()
    if user_option == '4':
        add_ani()

log_file.close()