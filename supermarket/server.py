import sys

class LoginMaster(object):
    def __init__(self):
        data = open('data/users', 'r')
        self.user_lib = {}
        for line in data.readlines():
            line = line.rstrip()
            if not line:
                break
            (login_type, username, password) = line.split('\t')
            self.user_lib[username] = (login_type, password)
        data.close()

    def check_user(self, user_name, pass_word):
        if user_name in self.user_lib:
            if pass_word == str(self.user_lib[user_name][1]):
                return self.user_lib[user_name][0]
        return None

class GoodsMaster(object):
    def __init__(self):
        data = open('data/goods', 'r')
        self.good_list = []
        cnt = 0
        for line in data.readlines():
            if not line:
                break
            (gid, good_name, value, number, in_time, f_name) = line.split('\t')
            number = int(number)
            cnt += 1
            self.good_list.append((cnt, gid, good_name, value, number, in_time, f_name))

    def gettime(self, date_time):
        s = date_time.split('-')
        if len(s) < 3:
            return 0
        t = s[0] + s[1] + s[2]
        return int(t)

    def check_good(self, limit):
        result = []
        cnt = 0
        print limit
        (gid, gname, gnumber, s_t, e_t, s_name) = limit
        print s_t
        for item in limit:
            if len(item) != 0:
                cnt += 1

        s_t = self.gettime(s_t)
        e_t = self.gettime(e_t)
        for good in self.good_list:
            check_number = 0
            (_, g_id, g_name, g_value, g_number, g_t, s_name) = good
            g_t = self.gettime(g_t)
            print g_t, s_t, e_t
            if g_id == gid:
                check_number += 1

            if gnumber != '' and int(gnumber) >= int(g_number):
                check_number += 1

            if g_t >= s_t and s_t != 0:
                check_number += 1

            if g_t <= e_t and e_t != 0:
                check_number += 1

            if check_number == cnt:
                result.append(good)
            print 'cnt = %s check_number = %s' %(cnt, check_number)
        return result
                
    def get_info(self, limit):
        print limit
        return self.check_good(limit)
    
    def modify_info(self, good_info):
        data = open('data/goods', 'a')
        (gid, good_name, value, number, in_time, f_name) = good_info
        if len(gid) <= 0:
            return
        try:
            number = int(number)
        except:
            return
        data.write('%s\t%s\t%s\t%s\t%s\t%s\n' %(gid, good_name, value, number, in_time, f_name))

class CashierMaster(object):
    def __init__(self):
        self.cnt = 0

    def add_result(self, goods):
        result = open('data/cashier', 'a')
        (gid, name, value, number) = goods
        if number == '':
            result = open('data/cashier', 'w')
        else:
            if len(gid) != 0:
                result.write('%s\t%s\t%s\t%s\t%s\n' %(self.cnt, gid, name, value, number));

    def show(self):
        result = open('data/cashier', 'r')
        tt = []
        self.total = 0
        cnt = 0
        for i in result.readlines():
            i = i.rstrip()
            if not i:
                break
            cnt += 1
            ttt = i.split('\t')
            ttt[0] = cnt
            self.total += int(ttt[3]) * int(ttt[4])
            tt.append(ttt)
            
        return (tt, self.total)

        
if __name__ == '__main__':
    lm = LoginMaster()
    s = lm.check_user('soso', '12356')
