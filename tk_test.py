import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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


mainWindow = tk.Tk()
mainWindow.title("产生式系统")
mainWindow.withdraw()
mainWindow.update()
winWidth = 940
winHeight = 375
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
mainWindow.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
mainWindow.deiconify()

def infop_op():
    if comd.get() == '':
        messagebox.showerror("Error", "请至少输入一个属性ID")
    input_fea = comd.get().split()
    cur = db.cursor()
    cur.execute("SELECT object FROM objects, objects_query WHERE objects_query.object_id = objects.id and objects_query.property_id = %s"%input_fea[0])
    result = cur.fetchall()
    for i in input_fea:
        cur.execute("SELECT object FROM objects, objects_query WHERE objects_query.object_id = objects.id and objects_query.property_id = %s"%i)
        temp_res = cur.fetchall()
        result = list(set(result) & set(temp_res))
    conditions = []
    for i in input_fea:
        cur.execute("SELECT info FROM properties WHERE id = %s"%i)
        conditions.append(cur.fetchall()[0][0].strip())
    condition_info = ''
    for i in conditions:
        print(i, end=" ")
        log_file.write(i + ' ')
        condition_info += i + ' '
    print('\n')
    print("推理过程如下：")
    log_file.write("\n推理过程如下：\n")
    res_info = ''
    if len(result) == 0:
        print("根据所给条件无法判断为何种对象")
        log_file.write("根据所给条件无法判断为何种对象\n")
        res_info += condition_info + " --> " + "根据所给条件无法判断为何种对象"
        loglist.insert(tk.END, res_info)
        messagebox.showerror("Error", "根据所给条件无法判断为何种对象")
    if len(result) == 1:
        for i in range(len(conditions)-1):
            print(conditions[i], end=", ")
            log_file.write(conditions[i] + ', ')
            res_info += conditions[i] + ', '
        print(conditions[-1], end=" --> ")
        log_file.write(conditions[-1] + " --> ")
        res_info += conditions[-1] + " --> "
        print(result[0][0])
        log_file.write(result[0][0] + '\n')
        res_info += result[0][0]
        loglist.insert(tk.END, res_info)
        messagebox.showinfo("推理过程", res_info)
    if len(result) > 1:
        print("该对象可能是：", end="")
        log_file.write("该对象可能是：")
        res_info += condition_info + " --> " + "该对象可能是："
        for i in result:
            print(i[0], end=" ")
            log_file.write(str(i) + ' ')
            res_info += i[0] + ' '
        print('\n')
        log_file.write('\n')
        loglist.insert(tk.END, res_info)
        print("根据所给条件无法判断为何种对象")


def rulop_op():
    rule_con = tk.Toplevel(mainWindow)
    rule_con.withdraw()
    rule_con.update()
    winWidth = 800
    winHeight = 300
    screenWidth = mainWindow.winfo_screenwidth()
    screenHeight = mainWindow.winfo_screenheight()
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    rule_con.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    rule_con.deiconify()

    rule_list = tk.Listbox(rule_con, selectmode=tk.BROWSE, height=14, width=46)
    rule_list.place(x=20, y=20)

    cur = db.cursor()
    cur.execute("SELECT id,object FROM objects")
    data_obj = cur.fetchall()
    cur.execute("SELECT info,object FROM properties, objects, objects_query WHERE objects_query.object_id = objects.id and objects_query.property_id = properties.id")
    fea_list = cur.fetchall()
    for i in data_obj:
        temp_fea = str(i[0]) + '.'
        for j in fea_list:
            if str(i[1]) == j[1]:
                temp_fea += j[0].strip() + ", "
        temp_fea = temp_fea.rstrip(", ")
        temp_fea += ' --> ' + i[1]
        rule_list.insert(tk.END, temp_fea)
        print(temp_fea)
    
    def rule_update():
        print("success")
    def rule_add():
        temp_rul = temp_rule.get().split()
        sql_list = []
        temp_obj = temp_rul[0]
        temp_field = temp_rul[1]
        temp_ru = temp_rul[2:]
        for i in temp_ru:
            sql_list.append([temp_obj, i])
        for i in sql_list:
            cur.execute("INSERT INTO objects_query values(%s, %s, %s)"%(i[0], i[1], temp_field))
            db.commit()
            print("done!")
    def rule_delete():
        id = rule_list.get(tk.ACTIVE).split('.')[0]
        cur = db.cursor()
        try:
            cur.execute("DELETE FROM objects_query WHERE object_id = %s"%id)
            db.commit()
            messagebox.showinfo("INFO", "删除成功")
        except:
            messagebox.showerror("ERROR", "数据库操作失败")
    def rule_move():
        rule_edit.delete(0, tk.END)
        rule_edit.insert(0, rule_list.get(tk.ACTIVE))

    temp_rule = tk.StringVar()
    rule_edit = tk.Entry(rule_con, font=12, textvariable=temp_rule, width=25)
    rule_edit.place(x=400+124, y=42)
    rule_edit_lb = tk.Label(rule_con, text="EDIT RULE", font=12)
    rule_edit_lb.place(x=400+124, y=20)
    rule_move_button = tk.Button(rule_con, text=">>", command=rule_move)
    rule_move_button.place(x=360+95, y=42)
    rule_update_button = tk.Button(rule_con, text="修改规则", command=rule_update, font=12)
    rule_update_button.place(x=440+125, y=80)
    rule_add_button = tk.Button(rule_con, text="添加规则", command=rule_add, font=12)
    rule_add_button.place(x=440+125, y=140)
    rule_delete_button = tk.Button(rule_con, text="删除规则", command=rule_delete, font=12)
    rule_delete_button.place(x=440+125, y=200)


def objop_op():
    obj_con = tk.Toplevel(mainWindow)
    obj_con.withdraw()
    obj_con.update()
    winWidth = 500
    winHeight = 300
    screenWidth = mainWindow.winfo_screenwidth()
    screenHeight = mainWindow.winfo_screenheight()
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    obj_con.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    obj_con.deiconify()

    obj_list = tk.Listbox(obj_con, selectmode=tk.BROWSE, height=14, width=20)
    obj_list.place(x=20, y=20)

    cur = db.cursor()
    cur.execute("SELECT id,object FROM objects")
    data_obj = cur.fetchall()

    def fetch_obj(fid):
        cur.execute("SELECT id,object FROM objects WHERE field_id = %s"%fid)
        data_pro = cur.fetchall()
        obj_list.delete(0, tk.END)
        for i in data_pro:
            temp_fea = str(i[0]) + '.' + i[1]
            obj_list.insert(tk.END, temp_fea)
            print(temp_fea)
    cur.execute("SELECT id,field FROM fields")
    data_field = cur.fetchall()
    cb_list = []
    for k in data_field:
        cb_list.append(str(k[0]) + '.' + k[1])
    for i in data_obj:
        temp_fea = str(i[0]) + '.' + i[1]
        obj_list.insert(tk.END, temp_fea)
        print(temp_fea)
    
    def change_field(*args):
        global temp_id
        temp_id = int(fie_cb.get().split('.')[0])
        fetch_obj(temp_id)
        cur.execute("SELECT id,field FROM fields")
        data_field = cur.fetchall()
        cb_list = []
        for k in data_field:
            cb_list.append(str(k[0]) + '.' + k[1])
        fie_cb['value'] = cb_list
        print(temp_id)

    def obj_update():
        id = obj_list.get(tk.ACTIVE).split('.')[0]
        temp_object = temp_obj.get()
        cur = db.cursor()
        try:
            print("UPDATE objects SET object = \"%s\" WHERE id = \"%s\""%(temp_object, id))
            cur.execute("UPDATE objects SET object = \"%s\" WHERE id = (%s)"%(temp_object, id))
            db.commit()
            messagebox.showinfo("INFO", "修改成功")
            
            fetch_data(field_id)
        except:
            traceback.print_exc()
            messagebox.showerror("ERROR", "数据库操作失败")
    def obj_add():
        cur = db.cursor()
        cur.execute("SELECT object FROM objects")
        temp_object = temp_obj.get()
        obj_data = cur.fetchall()
        if temp_object in obj_data:
            print("已存在该对象")
        else:
            try:
                cur.execute("INSERT INTO objects(object,field_id) values (\"%s\", \"%s\")"%(temp_object, temp_id))
                db.commit()
                cur.execute("SELECT id FROM objects WHERE object='%s'"%temp_object)
                obj_id = cur.fetchone()
                print("done! 该对象id为%s"%obj_id)
                log_file.write("==========LOG" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "==========\n")
                log_file.write("add对象id: %s, 对象名称: %s\n"%(obj_id[0], temp_obj))
                cur = db.cursor()
                cur.execute("SELECT id,object FROM objects WHERE field_id = %s"%temp_id)
                data_obj = cur.fetchall()
                obj_list.delete(0, tk.END)
                for i in data_obj:
                    temp_fea = str(i[0]) + '.' + i[1]
                    obj_list.insert(tk.END, temp_fea)
                    print(temp_fea)
                fetch_data(temp_id)
            except:
                db.rollback()
                traceback.print_exc()
                print("数据库操作失败，已回滚操作，请检查数据库连接")
    def obj_delete():
        id = obj_list.get(tk.ACTIVE).split('.')[0]
        cur = db.cursor()
        try:
            cur.execute("DELETE FROM objects WHERE id = %s"%id)
            db.commit()
            messagebox.showinfo("INFO", "删除成功")
            
            fetch_data(field_id)
        except:
            messagebox.showerror("ERROR", "数据库操作失败")
    def obj_move():
        obj_edit.delete(0, tk.END)
        obj_edit.insert(0, obj_list.get(tk.ACTIVE))

    temp_obj = tk.StringVar()
    obj_edit = tk.Entry(obj_con, font=12, textvariable=temp_obj)
    obj_edit.place(x=240+20, y=72)
    obj_edit_lb = tk.Label(obj_con, text="EDIT OBJECT", font=12)
    obj_edit_lb.place(x=240+20, y=50)
    obj_move_button = tk.Button(obj_con, text=">>", command=obj_move)
    obj_move_button.place(x=190+15, y=72)
    obj_update_button = tk.Button(obj_con, text="修改对象", command=obj_update, font=12)
    obj_update_button.place(x=280+25, y=120)
    obj_add_button = tk.Button(obj_con, text="添加对象", command=obj_add, font=12)
    obj_add_button.place(x=280+25, y=160)
    obj_delete_button = tk.Button(obj_con, text="删除对象", command=obj_delete, font=12)
    obj_delete_button.place(x=280+25, y=200)
    fie_cb = ttk.Combobox(obj_con)
    fie_cb.place(x=240+20, y=20)
    fie_cb.bind("<<ComboboxSelected>>",change_field)
    fie_cb['value'] = cb_list
    fie_cb.current(field_id-1)


def claop_op(fie_id):
    class_con = tk.Toplevel(mainWindow)
    class_con.withdraw()
    class_con.update()
    winWidth = 475
    winHeight = 300
    screenWidth = mainWindow.winfo_screenwidth()
    screenHeight = mainWindow.winfo_screenheight()
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    class_con.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    class_con.deiconify()
    print(fie_id)
    print(field_id)
    class_list = tk.Listbox(class_con, selectmode=tk.BROWSE, height=14, width=20)
    class_list.place(x=20, y=20)
    cur = db.cursor()
    cur.execute("SELECT id,class FROM classes")
    data_class = cur.fetchall()
    def fetch_cla(fid):
        cur.execute("SELECT id,class FROM classes WHERE field_id = %s"%fid)
        data_class = cur.fetchall()
        class_list.delete(0, tk.END)
        for i in data_class:
            temp_fea = str(i[0]) + '.' + i[1]
            class_list.insert(tk.END, temp_fea)
            print(temp_fea)
    cur.execute("SELECT id,field FROM fields")
    data_field = cur.fetchall()
    cb_list = []
    for k in data_field:
        cb_list.append(str(k[0]) + '.' + k[1])
    for i in data_class:
        temp_fea = str(i[0]) + '.' + i[1]
        class_list.insert(tk.END, temp_fea)
        print(temp_fea)
    def change_field(*args):
        global temp_id
        temp_id = int(fie_cb.get().split('.')[0])
        fetch_cla(temp_id)
        print(temp_id)
    def class_update():
        id = class_list.get(tk.ACTIVE).split('.')[0]
        temp_cla = temp_class.get()
        cur = db.cursor()
        try:
            print("UPDATE classes SET info = \"%s\" WHERE id = \"%s\""%(temp_cla, id))
            cur.execute("UPDATE classes SET info = \"%s\" WHERE id = (%s)"%(temp_cla, id))
            db.commit()
            messagebox.showinfo("INFO", "修改成功")
            
            fetch_data(field_id)
        except:
            traceback.print_exc()
            messagebox.showerror("ERROR", "数据库操作失败")
    def class_add():
        cur = db.cursor()
        cur.execute("SELECT object FROM objects")
        temp_cla = temp_class.get()
        cla_data = cur.fetchall()
        if temp_cla in cla_data:
            print("已存在该对象")
        else:
            try:
                cur.execute("INSERT INTO classes(class, field_id) values (\"%s\", \"%s\")"%(temp_cla,temp_id))
                db.commit()
                cur.execute("SELECT id FROM classes WHERE class='%s'"%temp_cla)
                cla_id = cur.fetchone()
                print("done! 该类id为%s"%cla_id)
                log_file.write("==========LOG" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "==========\n")
                log_file.write("add类id: %s, 类名称: %s\n"%(cla_id[0], temp_cla))
                cur = db.cursor()
                cur.execute("SELECT id,class FROM classes WHERE field_id = %s"%temp_id)
                data_obj = cur.fetchall()
                class_list.delete(0, tk.END)
                for i in data_obj:
                    temp_fea = str(i[0]) + '.' + i[1]
                    class_list.insert(tk.END, temp_fea)
                    print(temp_fea)
                
                fetch_data(field_id)
            except:
                db.rollback()
                traceback.print_exc()
                print("数据库操作失败，已回滚操作，请检查数据库连接")
    def class_delete():
        id = class_list.get(tk.ACTIVE).split('.')[0]
        cur = db.cursor()
        try:
            cur.execute("DELETE FROM classes WHERE id = %s"%id)
            db.commit()
            messagebox.showinfo("INFO", "删除成功")
            
            fetch_data(field_id)
        except:
            messagebox.showerror("ERROR", "数据库操作失败")
    def class_move():
        class_edit.delete(0, tk.END)
        class_edit.insert(0, class_list.get(tk.ACTIVE))

    temp_class = tk.StringVar()
    class_edit = tk.Entry(class_con, font=12, textvariable=temp_class)
    class_edit.place(x=320-60, y=72)
    class_edit_lb = tk.Label(class_con, text="EDIT CLASS", font=12)
    class_edit_lb.place(x=320-65, y=50)
    class_move_button = tk.Button(class_con, text=">>", command=class_move)
    class_move_button.place(x=280-75, y=72)
    class_update_button = tk.Button(class_con, text="修改类", command=class_update, font=12)
    class_update_button.place(x=370-75, y=120)
    class_add_button = tk.Button(class_con, text="添加类", command=class_add, font=12)
    class_add_button.place(x=370-75, y=160)
    class_delete_button = tk.Button(class_con, text="删除类", command=class_delete, font=12)
    class_delete_button.place(x=370-75, y=200)
    fie_cb = ttk.Combobox(class_con)
    fie_cb.place(x=320-65, y=20)
    fie_cb.bind("<<ComboboxSelected>>",change_field)
    fie_cb['value'] = cb_list
    fie_cb.current(field_id-1)

def proop_op():
    pro_con = tk.Toplevel(mainWindow)
    pro_con.withdraw()
    pro_con.update()
    winWidth = 450
    winHeight = 300
    screenWidth = mainWindow.winfo_screenwidth()
    screenHeight = mainWindow.winfo_screenheight()
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    pro_con.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    pro_con.deiconify()

    pro_list = tk.Listbox(pro_con, selectmode=tk.BROWSE, height=14, width=15)
    pro_list.place(x=20, y=20)

    cur = db.cursor()
    cur.execute("SELECT id,info FROM properties")
    data_pro = cur.fetchall()

    def fetch_pro(fid):
        cur.execute("SELECT id,info FROM properties WHERE field_id = %s"%fid)
        data_pro = cur.fetchall()
        pro_list.delete(0, tk.END)
        for i in data_pro:
            temp_fea = str(i[0]) + '.' + i[1]
            pro_list.insert(tk.END, temp_fea)
            print(temp_fea)
    cur.execute("SELECT id,field FROM fields")
    data_field = cur.fetchall()
    cb_list = []
    for k in data_field:
        cb_list.append(str(k[0]) + '.' + k[1])
    for i in data_pro:
        temp_fea = str(i[0]) + '.' + i[1]
        pro_list.insert(tk.END, temp_fea)
        print(temp_fea)
    
    def change_field(*args):
        global temp_id
        temp_id = int(fie_cb.get().split('.')[0])
        fetch_pro(temp_id)
        print(temp_id)

    def pro_update():
        id = pro_list.get(tk.ACTIVE).split('.')[0]
        temp_property = temp_pro.get()
        cur = db.cursor()
        try:
            print("UPDATE properties SET info = \"%s\" WHERE id = \"%s\""%(temp_property, id))
            cur.execute("UPDATE properties SET info = \"%s\" WHERE id = (%s)"%(temp_property, id))
            db.commit()
            messagebox.showinfo("INFO", "修改成功")
            
            fetch_data(field_id)
        except:
            traceback.print_exc()
            messagebox.showerror("ERROR", "数据库操作失败")
    def pro_add():
        cur = db.cursor()
        cur.execute("SELECT object FROM objects")
        temp_property = temp_pro.get()
        pro_data = cur.fetchall()
        if temp_property in pro_data:
            print("已存在该属性")
        else:
            try:
                cur.execute("INSERT INTO properties(info, field_id) values (\"%s\", \"%s\")"%(temp_property,temp_id))
                db.commit()
                cur.execute("SELECT id FROM properties WHERE info='%s'"%temp_property)
                pro_id = cur.fetchone()
                print("done! 该属性id为%s"%pro_id)
                log_file.write("==========LOG" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "==========\n")
                log_file.write("add属性id: %s, 属性名称: %s\n"%(pro_id[0], temp_property))
                cur = db.cursor()
                cur.execute("SELECT id,info FROM properties WHERE field_id = %s"%temp_id)
                data_obj = cur.fetchall()
                pro_list.delete(0, tk.END)
                for i in data_obj:
                    temp_fea = str(i[0]) + '.' + i[1]
                    pro_list.insert(tk.END, temp_fea)
                    print(temp_fea)
                
                fetch_data(field_id)
            except:
                db.rollback()
                traceback.print_exc()
                print("数据库操作失败，已回滚操作，请检查数据库连接")
    def pro_delete():
        id = pro_list.get(tk.ACTIVE).split('.')[0]
        cur = db.cursor()
        try:
            cur.execute("DELETE FROM properties WHERE id = %s"%id)
            db.commit()
            messagebox.showinfo("INFO", "删除成功")
            print(field_id)
            fetch_data(field_id)
        except:
            messagebox.showerror("ERROR", "数据库操作失败")
    def pro_move():
        pro_edit.delete(0, tk.END)
        pro_edit.insert(0, pro_list.get(tk.ACTIVE))

    temp_pro = tk.StringVar()
    pro_edit = tk.Entry(pro_con, font=12, textvariable=temp_pro)
    pro_edit.place(x=320-100, y=72)
    pro_edit_lb = tk.Label(pro_con, text="EDIT PROPERTY", font=12)
    pro_edit_lb.place(x=320-100, y=50)
    pro_move_button = tk.Button(pro_con, text=">>", command=pro_move)
    pro_move_button.place(x=280-115, y=72)
    pro_update_button = tk.Button(pro_con, text="修改属性", command=pro_update, font=12)
    pro_update_button.place(x=360-100, y=120)
    pro_add_button = tk.Button(pro_con, text="添加属性", command=pro_add, font=12)
    pro_add_button.place(x=360-100, y=160)
    pro_delete_button = tk.Button(pro_con, text="删除属性", command=pro_delete, font=12)
    pro_delete_button.place(x=360-100, y=200)
    fie_cb = ttk.Combobox(pro_con)
    fie_cb.place(x=320-100, y=20)
    fie_cb.bind("<<ComboboxSelected>>",change_field)
    fie_cb['value'] = cb_list
    fie_cb.current(field_id-1)

def fieop_op():
    fie_con = tk.Toplevel(mainWindow)
    fie_con.withdraw()
    fie_con.update()
    winWidth = 500
    winHeight = 300
    screenWidth = mainWindow.winfo_screenwidth()
    screenHeight = mainWindow.winfo_screenheight()
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    fie_con.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    fie_con.deiconify()

    fie_list = tk.Listbox(fie_con, selectmode=tk.BROWSE, height=14, width=15)
    fie_list.place(x=20, y=20)

    cur = db.cursor()
    cur.execute("SELECT id,field FROM fields")
    data_fie = cur.fetchall()
    for i in data_fie:
        temp_fea = str(i[0]) + '.' + i[1]
        fie_list.insert(tk.END, temp_fea)
        print(temp_fea)
    
    def fie_update():
        id = fie_list.get(tk.ACTIVE).split('.')[0]
        temp_field = temp_fie.get()
        cur = db.cursor()
        try:
            print("UPDATE fields SET field = \"%s\" WHERE id = \"%s\""%(temp_field, id))
            cur.execute("UPDATE fields SET field = \"%s\" WHERE id = (%s)"%(temp_field, id))
            db.commit()
            messagebox.showinfo("INFO", "修改成功")
            
            fetch_data(field_id)
        except:
            traceback.print_exc()
            messagebox.showerror("ERROR", "数据库操作失败")
    def fie_add():
        cur = db.cursor()
        cur.execute("SELECT field FROM fields")
        temp_field = temp_fie.get()
        fie_data = cur.fetchall()
        if temp_field in fie_data:
            print("已存在该领域")
        else:
            try:
                cur.execute("INSERT INTO fields(field) values (\"%s\")"%temp_field)
                db.commit()
                cur.execute("SELECT id FROM fields WHERE field='%s'"%temp_field)
                fie_id = cur.fetchone()
                print("done! 该领域id为%s"%fie_id)
                log_file.write("==========LOG" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "==========\n")
                log_file.write("add领域id: %s, 领域名称: %s\n"%(fie_id[0], temp_field))
                cur = db.cursor()
                cur.execute("SELECT id,field FROM fields")
                data_obj = cur.fetchall()
                fie_list.delete(0, tk.END)
                for i in data_obj:
                    temp_fea = str(i[0]) + '.' + i[1]
                    fie_list.insert(tk.END, temp_fea)
                    print(temp_fea)

                fetch_data(field_id)
            except:
                db.rollback()
                traceback.print_exc()
                print("数据库操作失败，已回滚操作，请检查数据库连接")
    def fie_delete():
        id = fie_list.get(tk.ACTIVE).split('.')[0]
        cur = db.cursor()
        try:
            cur.execute("DELETE FROM fields WHERE id = %s"%id)
            db.commit()
            messagebox.showinfo("INFO", "删除成功")
            
            fetch_data(field_id)
        except:
            messagebox.showerror("ERROR", "数据库操作失败")
    def fie_move():
        fie_edit.delete(0, tk.END)
        fie_edit.insert(0, fie_list.get(tk.ACTIVE))
    temp_fie = tk.StringVar()
    fie_edit = tk.Entry(fie_con, font=12, textvariable=temp_fie)
    fie_edit.place(x=320-75, y=42)
    fie_edit_lb = tk.Label(fie_con, text="EDIT FIELD", font=12)
    fie_edit_lb.place(x=320-75, y=20)
    fie_move_button = tk.Button(fie_con, text=">>", command=fie_move)
    fie_move_button.place(x=280-100, y=42)
    fie_update_button = tk.Button(fie_con, text="修改领域", command=fie_update, font=12)
    fie_update_button.place(x=360-75, y=80)
    fie_add_button = tk.Button(fie_con, text="添加领域", command=fie_add, font=12)
    fie_add_button.place(x=360-75, y=140)
    fie_delete_button = tk.Button(fie_con, text="删除领域", command=fie_delete, font=12)
    fie_delete_button.place(x=360-75, y=200)


clalb = tk.Label(mainWindow)

clalb = tk.Label(mainWindow, text="对象", font=12)
clalb.place(x=40, y=30)
clalist = tk.Listbox(mainWindow, selectmode=tk.BROWSE,height=16, width=15)
clalist.place(x=40, y=50)
prolb = tk.Label(mainWindow, text="属性", font=12)
prolb.place(x=240-40, y=30)
prolist = tk.Listbox(mainWindow, selectmode=tk.BROWSE,height=16, width=15)
prolist.place(x=240-40, y=50)
loglb = tk.Label(mainWindow, text="日志", font=12)
loglb.place(x=650-75, y=30)
loglist = tk.Listbox(mainWindow, selectmode=tk.BROWSE,height=16, width=36)
loglist.place(x=650-75, y=50)

def fetch_data(fie_id):
    prolist.delete(0, tk.END)
    clalist.delete(0, tk.END)
    cur = db.cursor()
    cur.execute("SELECT id,info FROM properties WHERE field_id = %s"%fie_id)
    data_fea = cur.fetchall()
    cur.execute("SELECT id,object FROM objects WHERE field_id = %s"%fie_id)
    data_ani = cur.fetchall()
    cur.execute("SELECT id,field FROM fields")
    data_field = cur.fetchall()
    for i in data_fea:
        prolist.insert(tk.END, str(i[0]) + '.' + i[1])

    for j in data_ani:
        clalist.insert(tk.END, str(j[0]) + '.' + j[1])
    cb_list = []
    for k in data_field:
        cb_list.append(str(k[0]) + '.' + k[1])
    field_cb['value'] = cb_list
    field_cb.current(fie_id-1)
    field_id = fie_id

def change_field(*args):
    temp_id = int(field_cb.get().split('.')[0])
    field_id = temp_id
    print(field_id)
    print(temp_id)
    fetch_data(temp_id)

field_cb = ttk.Combobox(mainWindow)
field_cb.place(x=440-75, y=55)
field_cb.bind("<<ComboboxSelected>>",change_field)

txtlb = tk.Label(mainWindow, text="INPUT ID", font=12)
txtlb.place(x=440-75, y=80)
comd = tk.StringVar()
txtput = tk.Entry(mainWindow, font=12, textvariable=comd)
txtput.place(x=440-75, y=100)

infop = tk.Button(mainWindow, text="推理", command=infop_op, font=12)
infop.place(x=500-75, y=130)
fieop = tk.Button(mainWindow, text="领域操作", command=fieop_op, font=12)
fieop.place(x=485-75, y=160)
rulop = tk.Button(mainWindow, text="规则操作", command=rulop_op, font=12)
rulop.place(x=485-75, y=195)
objop = tk.Button(mainWindow, text="对象操作", command=objop_op, font=12)
objop.place(x=485-75, y=230)
claop = tk.Button(mainWindow, text="类操作", command=lambda: claop_op(field_id), font=12)
claop.place(x=495-75, y=265)
proop = tk.Button(mainWindow, text="属性操作", command=proop_op, font=12)
proop.place(x=485-75, y=300)

field_id = 1
fetch_data(field_id);


mainWindow.mainloop()