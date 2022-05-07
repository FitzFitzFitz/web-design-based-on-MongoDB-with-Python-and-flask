from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient  # 使用pymongo库里面的mongoclient


client = MongoClient('localhost', 27017)  # 地址与接口
database = client.get_database('Bills')  # 数据库名
collection = database.get_collection('table')  # 表名

# 使用Flask对象创建一个app对象
app = Flask(__name__)
DB = [
    {
        'phone': '13373608878',
        'name': '夏嘉尔',
        'password': '123',
        'IDnum': '320281200111024516',
        'ADMIN': '是',

        'balance': '100',
        'payable': '50',
        'basic_fee': '40',
        'extra_fee': '10',

        'basic_call': '100',
        'basic_traffic': '10',
        'total_call': '10',
        'total_traffic': '11',
        'VPN_service': '是',
        'extra_call': '0',
        'extra_traffic': '1'
    },
    {
        'phone': '17851177994',
        'name': '宋栩庆',
        'password': '123',
        'IDnum': '410423200009042039',
        'ADMIN': '是',

        'balance': '1000',
        'payable': '500',
        'basic_fee': '400',
        'extra_fee': '100',

        'basic_call': '1000',
        'basic_traffic': '100',
        'total_call': '100',
        'total_traffic': '110',
        'VPN_service': '是',
        'extra_call': '0',
        'extra_traffic': '10'
    },
    {
        'phone': '13656160540',
        'name': '陈奕开',
        'password': '123',
        'IDnum': '320281200105249014',
        'ADMIN': '是',

        'balance': '1000',
        'payable': '500',
        'basic_fee': '400',
        'extra_fee': '100',

        'basic_call': '1000',
        'basic_traffic': '100',
        'total_call': '100',
        'total_traffic': '110',
        'VPN_service': '是',
        'extra_call': '0',
        'extra_traffic': '10'
    },
    {
        'phone': '19852121226',
        'name': '陈潇宇',
        'password': '123',
        'IDnum': '320311200009276414',
        'ADMIN': '是',

        'balance': '1000',
        'payable': '500',
        'basic_fee': '400',
        'extra_fee': '100',

        'basic_call': '1000',
        'basic_traffic': '100',
        'total_call': '100',
        'total_traffic': '110',
        'VPN_service': '是',
        'extra_call': '0',
        'extra_traffic': '10'
    },
    {
        'phone': '15878709596',
        'name': '莫桐',
        'password': '123',
        'IDnum': '45212820010404001X',
        'ADMIN': '是',

        'balance': '1000',
        'payable': '500',
        'basic_fee': '400',
        'extra_fee': '100',

        'basic_call': '1000',
        'basic_traffic': '100',
        'total_call': '100',
        'total_traffic': '110',
        'VPN_service': '是',
        'extra_call': '0',
        'extra_traffic': '10'
    }
]


# collection.insert_many(DB)

# @app是  ，route是路由
@app.route('/')  # /是访问的路径
def hello_world():  # put application's code here
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 登录的功能
    if request.method == 'POST':
        # request可以拿到前端浏览器传回的数据
        phone = request.form.get('phone')
        password = request.form.get('password')
        count = collection.count_documents({'phone': phone})  # 先查询id是否存在，不存在返回False
        # print(phone, password, count)
        if count == 0:
            # 想return到一个提示错误的网页
            return redirect('./login_name_error')
        else:
            # filter={'password'}
            password = collection.find_one({'phone': phone})['password']
            ADMIN = collection.find_one({'phone': phone})['ADMIN']
            if password != password:
                # 想return到一个提示错误的网页
                return redirect('./login_password_error')
            elif ADMIN == "是":
                print('从服务器接收到的数据：', phone, password)
                # 登陆成功之后应该跳转到管理页面
                return redirect('./admin')
            else:
                # 如果不是管理员，则跳进用户界面
                return redirect(url_for('userdb', phone=phone))

    return render_template('login.html')  # get 请求获取这个网站，post请求获取数据


# @app.route('/login/',methods=['GET','POST'])
# def user_login():
#     username = 'unsprint'
#  	return redirect(url_for('index',username=username))
# url_for在index的路由和username之间加一个?进行拼接,使得username成为一个可接受的参数
# #通过路由接收参数
# @app.route('/index/?<string:username>')  #这里指定了接收的username的类型,如果不符合会报错,
# 	def index(username):                     #可以将string改成path, 这样username就会被当成路径来接收,也就是说username可以是任意可键入路由的值了
# 	return username


@app.route('/login_name_error')
def name_error():
    return render_template('login_name_error.html')


@app.route('/login_password_error')
def password_error():
    return render_template('login_password_error.html')


@app.route('/search_name_error')
def search_name_error():
    # 复制框架源码
    return render_template('search_name_error.html')


@app.route('/admin')
def admin():
    # 重新传一遍数据库
    users = collection.find({}, {'_id': 0})
    return render_template('admin.html', users=users)


@app.route('/search', methods=['GET', 'POST'])
def search():
    user = {}
    if request.method == 'POST':
        # request可以拿到前端浏览器传回的数据
        mix = request.form.get('mix')
        print(mix)
        # name = request.form.get('name')
        # IDnum = request.form.get('IDnum')

        c1 = collection.count_documents({'phone': mix})
        c2 = collection.count_documents({'name': mix})
        c3 = collection.count_documents({'IDnum': mix})
        count = c1 + c2 + c3
        # 先查询返回的值是否存在
        # print(phone, password, count)
        if count == 0:
            # 想return到一个提示错误的网页
            return redirect('./search_name_error')
        else:
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
            user = collection.find_one(condition)
            # return render_template('search.html', user=user)
    return render_template('search.html', user=user)


@app.route('/add', methods=['GET', 'POST'])
def add():
    # 复制框架源码
    if request.method == 'POST':
        phone = request.form.get('phone')
        name = request.form.get('name')
        password = request.form.get('password')
        IDnum = request.form.get('IDnum')
        ADMIN = request.form.get('ADMIN')
        balance = request.form.get('balance')
        payable = request.form.get('payable')
        basic_fee = request.form.get('basic_fee')
        extra_fee = request.form.get('extra_fee')
        basic_call = request.form.get('basic_call')
        basic_traffic = request.form.get('basic_traffic')
        total_call = request.form.get('total_call')
        total_traffic = request.form.get('total_traffic')
        VPN_service = request.form.get('VPN_service')
        extra_call = request.form.get('extra_call')
        extra_traffic = request.form.get('extra_traffic')
        print('获取的用户信息：', phone, name, password,
              IDnum, ADMIN, balance, payable, basic_fee, extra_fee,
              basic_call, basic_traffic, total_call,
              total_traffic, VPN_service, extra_call, extra_traffic)
        doc = {'phone': phone, 'name': name, 'password': password,
               'IDnum': IDnum, 'ADMIN': ADMIN, 'balance': balance,
               'payable': payable, 'basic_fee': basic_fee,
               'extra_fee': extra_fee, 'basic_call': basic_call,
               'basic_traffic': basic_traffic,
               'total_call': total_call, 'total_traffic': total_traffic,
               'VPN_service': VPN_service, 'extra_call': extra_call,
               'extra_traffic': extra_traffic}
        collection.insert_one(doc)
        return redirect('./admin')
    return render_template('add.html')


@app.route('/delete')
def delete_user():
    # 在后台需要拿到用户的名字
    print(request.method)
    phonenum = request.args.get('phone')
    # 再传一遍数据库
    users = collection.find({}, {'_id': 0})
    # 找到用户并删除
    for user in users:
        if user['phone'] == phonenum:
            # 要在数据库里删除user
            collection.delete_one({'phone': phonenum})
            # users.remove(user)  # python 删除pop remove
    return redirect('./admin')


@app.route('/change', methods=["GET", "POST"])
def change_user():
    phone = request.args.get('phone')
    if request.method == 'POST':
        phone = request.form.get('phone')
        name = request.form.get('name')
        password = request.form.get('password')
        IDnum = request.form.get('IDnum')
        ADMIN = request.form.get('ADMIN')
        balance = request.form.get('balance')
        payable = request.form.get('payable')
        basic_fee = request.form.get('basic_fee')
        extra_fee = request.form.get('extra_fee')
        basic_call = request.form.get('basic_call')
        basic_traffic = request.form.get('basic_traffic')
        total_call = request.form.get('total_call')
        total_traffic = request.form.get('total_traffic')
        VPN_service = request.form.get('VPN_service')
        extra_call = request.form.get('extra_call')
        extra_traffic = request.form.get('extra_traffic')
        # user = collection.find({}, {'_id': 0})这个好像没用到？
        # 加一个update
        collection.update_one(
            {'phone': phone},  # 筛选出指定数据
            {'$set': {
                'phone': phone, 'name': name, 'password': password,
                'IDnum': IDnum, 'ADMIN': ADMIN, 'balance': balance,
                'payable': payable, 'basic_fee': basic_fee,
                'extra_fee': extra_fee, 'basic_call': basic_call,
                'basic_traffic': basic_traffic,
                'total_call': total_call, 'total_traffic': total_traffic,
                'VPN_service': VPN_service, 'extra_call': extra_call,
                'extra_traffic': extra_traffic
                # $set:对当前字典满足筛选器的项进行修改，如果键名不存在则创建键值对
            }
            })
        return redirect('./admin')
    users = collection.find({}, {'_id': 0})
    for user in users:
        if user['phone'] == phone:
            # 需要在页面中渲染用户的数据
            return render_template('change.html', user=user)


@app.route('/userdb/?<string:phone>')
def userdb(phone):
    user = collection.find_one({'phone': phone})
    return render_template('userdb.html', user=user)


# #通过路由接收参数
# @app.route('/index/?<string:username>')  #这里指定了接收的username的类型,如果不符合会报错,
# 	def index(username):                     #可以将string改成path, 这样username就会被当成路径来接收,也就是说username可以是任意可键入路由的值了
# 	return username


# 需要实现其他功能，例如退出等其他的功能，该怎么实现
#
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
