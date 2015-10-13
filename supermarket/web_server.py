# -*- coding:gbk
import sys
import os.path

import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.web
import json
from tornado import gen
from tornado.options import define, options, parse_command_line

from server import LoginMaster #登陆校验
from server import GoodsMaster #商品相关
from server import CashierMaster #收银

define("port", default=8888, help="run on the given port", type = int)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_json = self.get_secure_cookie("login_user")
        if not user_json: 
            return None
        return tornado.escape.json_decode(user_json)

class AuthLoginHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        self.render('login.html')

    def post(self):
        user = {
                "user_name" : self.get_argument('user_name'),
                "pass_word" : self.get_argument('pass_word')
        }
        #TODO 密码验证
        login_master = LoginMaster()
        if login_master.check_user(user['user_name'], user['pass_word']) == 'master':
            self.set_secure_cookie('login_user', tornado.escape.json_encode(user))
            self.redirect('/')
        elif login_master.check_user(user['user_name'], user['pass_word']) == 'cashier':
            self.set_secure_cookie('login_user', tornado.escape.json_encode(user))
            self.redirect('/cashier')
        else:
            self.redirect('/auth/login')


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("login_user")
        self.render("login.html")

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_name = self.get_secure_cookie("login_user")
        user_info = json.loads(user_name)
        self.render("index.html", user_name=user_info['user_name'])

class CashierHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user_name = self.get_secure_cookie("login_user")
        user_info = json.loads(user_name)
        self.render("cashier.html", user_name=user_info['user_name'])

class ModifyHandler(BaseHandler):
    def get(self):
        user_name = self.get_secure_cookie("login_user")
        user_info = json.loads(user_name)

        gid = self.get_argument('gid')
        name = self.get_argument('name')
        value = self.get_argument('value')
        number = self.get_argument('number')
        in_time = self.get_argument('in_time')
        s_name = self.get_argument('s_name')
        self.render("modify.html", user_name=user_info['user_name'])
        good_master = GoodsMaster()
        good_master.modify_info((gid, name, value, number, in_time, s_name))

class MoneyHandler(BaseHandler):
    def get(self):
        user_name = self.get_secure_cookie("login_user")
        user_info = json.loads(user_name)

        gid = self.get_argument('gid')
        name = self.get_argument('name')
        value = self.get_argument('value')
        number = self.get_argument('number')
        cm = CashierMaster()
        cm.add_result((gid, name, value, number))
        (result, total) = cm.show()
        self.render("money.html", user_name=user_info['user_name'], result=result, total=total)

class SearchHandler(BaseHandler):
    def get(self):
        user_name = self.get_secure_cookie("login_user")
        user_info = json.loads(user_name)
        good_master = GoodsMaster()

        good_id = self.get_argument('g')
        good_name = self.get_argument('n')
        good_number = self.get_argument('num')
        start_time = self.get_argument('s_t')
        end_time = self.get_argument('e_t')
        supplier_name = self.get_argument('s_n')
        print 'gid = %s gname= %s gnunber = %s s_t = %s e_t = %s s_name = %s' %(good_id, good_name, good_number, start_time, end_time, supplier_name)

        
        good_info = good_master.get_info((good_id, good_name, good_number, start_time, end_time, supplier_name))
        self.render("search.html", user_name=user_info['user_name'], good_info=good_info)

class SupplyHandler(BaseHandler):
    def get(self):
        user_name = self.get_secure_cookie("login_user")
        user_info = json.loads(user_name)
        self.render("supplier.html", user_name=user_info['user_name'])

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        user_name = self.get_secure_cookie("login_user")
        user_info = json.loads(user_name)
        self.render("test.html")

def main():
    parse_command_line()
    app = tornado.web.Application(
        [   (r'/', MainHandler),
            (r'/auth/login', AuthLoginHandler),
            (r'/auth/logout', AuthLogoutHandler),
            (r'/modify', ModifyHandler),
            (r'/search', SearchHandler),
            (r'/supplier', SupplyHandler),
            (r'/cashier', CashierHandler),
            (r'/money', MoneyHandler),
            ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        login_url = "/auth/login",
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies = True,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
