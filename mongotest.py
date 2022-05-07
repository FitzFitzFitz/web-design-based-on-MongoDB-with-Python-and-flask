from flask import Flask, render_template, request, redirect
from pymongo import MongoClient  # 使用pymongo库里面的mongoclient
import datetime  # 导入时间模块

client = MongoClient('localhost', 27017)  # 地址与接口
database = client.get_database('Bills')  # 数据库名
collection = database.get_collection('table')  # 表名
# doc = {
#     '_id': '13373608878',
#     'name': '夏嘉尔',
#     'password': '123',
#     'IDnum': '320281200111024516',
#     'ADMIN': '是',
#
#     'balance': '100',
#     'payable': '50',
#     'basic_fee': '40',
#     'extra_fee': '10',
#
#     'basic_call': '100',
#     'basic_traffic': '10',
#     'total_call': '10',
#     'total_traffic': '11',
#     'VPN_service': '是',
#     'extra_call': '0',
#     'extra_traffic': '1'
# }
# collection.insert_one(doc)
# 读取一项实验
# phone = '13373608878'
# 法1
# key = collection.find_one({'phone': phone}, {'password': 1, '_id': 0})
# print(key['password'])

# key = collection.find_one({'phone': phone})['password']
# print(key)
# 法2
# for x in collection.find():
#     if x['phone'] == phone:
#         p = x['password']
# print(p)


# 显示全部实验
# phone = name = password = IDnum = ADMIN = balance = payable = \
#     basic_fee = extra_fee = basic_call = basic_traffic = \
#     total_call = total_traffic = VPN_service = extra_call = extra_traffic = []
# x = collection.find({})
# for i in x:
#     phone.append(i['phone'])
# for i in x:
#     name.append(i['name'])
# for i in x:
#     password.append(i['password'])
#     IDnum.append(i['IDnum'])
#     ADMIN.append(i['ADMIN'])
#     balance.append(i['balance'])
#     payable.append(i['payable'])
#     basic_fee.append(i['basic_fee'])
#     extra_fee.append(i['extra_fee'])
#     basic_call.append(i['basic_call'])
#     basic_traffic.append(i['basic_traffic'])
#     total_call.append(i['total_call'])
#     total_traffic.append(i['total_traffic'])
#     VPN_service.append(i['VPN_service'])
#     extra_call.append(i['extra_call'])
#     extra_traffic.append(i['extra_traffic'])

# users = collection.find({},{'_id':0})
# for user in users:
#     print(user)

# count实验
mix = '13373608878'
c1 = collection.count_documents({'phone': mix})
c2 = collection.count_documents({'name': mix})
c3 = collection.count_documents({'IDnum': mix})
count = c1 + c2 + c3
print(c1, c2, c3, count)
print(type(c1), type(c2), type(c3), type(count))

# 先查询返回的值是否存在
# print(phone, password, count)
# if count == 0:
#     # 想return到一个提示错误的网页
#     return redirect('./name_error')
# else:
# 跳转到一个查找结果页面search_result，类似admin
# 要传出一个键值对，妈的到底之前给了哪个
condition = {}
if c1 == 1:
    condition = {'phone': mix}
elif c2 == 1:
    condition = {'name': mix}
else:
    condition = {'IDnum': mix}
print(condition)
users = collection.find_one(condition)
count=collection.count_documents(condition)
print(count)
print(users['IDnum'],users['phone'])
