from datetime import date, datetime, timedelta, time
import re
import random
import time
import sqlite3

class User():
    __name: str
    __login: str
    __password: str
    is_blocked: bool
    subscription_date: date
    subscription_mode: int
    
    def __init__(self, __name, __login, __password = '', is_blocked = False, subscription_date = None, subscription_mode = 'free'):
        
        while not self.__check___name(__name):
            __name = self.__new_name()
        else:
            self.__name = __name

        while not self.__check___login(__login, __name):
            __login = self.__new_login()
        else:
            self.__login = __login
        
        self.__password = self.__check___password(__password)

        self.is_blocked = is_blocked

        if subscription_date is None:
            self.subscription_date = date.today() + timedelta(days = 30)
        else:
            self.subscription_date = subscription_date
    
        self.subscription_mode = subscription_mode

        self.info_to_sql()

    def info_to_sql(self):
        db = sqlite3.connect('user.db')
        c = db.cursor()
        c.execute(f"""INSERT INTO user (name, login, password, is_blocked, sub_date, sub_mode) 
            VALUES( '{self.__name}', '{self.__login}', '{'123' + self.__password + '123'}', '{self.is_blocked}','{self.subscription_date}','{self.subscription_mode}')""")
        db.commit()
        db.close()

    def update_data(self):

        db = sqlite3.connect('user.db')
        c = db.cursor()
        c.execute(f"""UPDATE user SET name = '{self.__name}', login = '{self.__login}', password ='{'123' + self.__password + '123'}', is_blocked = '{self.is_blocked}', 
        sub_date = '{self.subscription_date}', sub_mode = '{self.subscription_mode}' WHERE name  = '{self.__name}' """)
        db.commit()
        db.close()

    def get_info(self):
            if self.is_blocked:
                print(f'Извините, пользователь {self.__name} заблокирован, обратитесь в техподдержку!')
            else:
                print(f'name: {self.__name}\nlogin: {self.__login}\npassword: ******\nIs_blocked: {self.is_blocked}\nsub_date: {self.subscription_date}\nSub_mode: {self.subscription_mode}\n ')
    
    def block(self):
        self.is_blocked = True
        db = sqlite3.connect('user.db')
        c = db.cursor()
        c.execute("SELECT rowid, * FROM user")

    def unblock(self):
        self.is_blocked = False

    def __new_name(self):
        return input('Введите новое имя:')

    def __new_login(self):
        return input('Введите новый логин:')

    def check_subscr(self):
        
        if self.subscription_date <= date.today():
            print(f'{self.__name} - пополните счет, подписка закончилась')
        else:
            data = self.subscription_date - date.today()
            print(f'{self.__name} У вас осталось {data.days} дней подписки, вид подписки: {self.subscription_mode}')
    
    def donate(self,val:int):
        self.subscription_mode = 'paid'
        self.subscription_date += timedelta(days = val)

    def __check___name(self, __name):
        if len(re.findall("[а-яА-Я]",__name)) == len(__name):
            return True
        else:
            print(f'{__name} - Поменяйте Ваше имя!')
            return False
        
    def __check___login(self,__login,__name):
        if re.match(r'^[A-Za-z0-9_]{6,}$', __login):
            return True
        else:
           print(f'{__name} - Поменяйте Ваш логин!')
           return False

    def __check___password(self, __password):
        if self.__check___password_pattern(__password):
            return __password
        else:
            __password = ''
            __password = self.__change_pass(__password)
            return __password

    def __check___password_pattern(self, __password):
            if re.search(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z_-]{6,}$', __password):
                return True
            else:
                return False

    def __change_pass(self,__password):
            if self.__check___password_pattern(__password):
                print('Вы успешно сменили пароль.')
                return ''
            else:
                print(f'{self.__name} - Пароль небезопасен. Пароль будет сгенерирован системой.')
                time.sleep(1)
            while not self.__check___password_pattern(__password):
                str1 = '1234567890'
                str2 = 'qwertyuiopasdfghjklzxcvbnm'
                str3 = str2.upper()
                str4 = str1+str2+str3
                l = list(str4)
                new___password = ''
                for x in range(10):
                    new___password = new___password + random.choice(l)   
                __password = new___password
            print(f'{self.__name} - вот Ваш новый пароль, сохраните и запомните его: {__password}\n')
            return __password

def print_sql():
    db = sqlite3.connect('user.db')
    c = db.cursor()
    c.execute("SELECT rowid, * FROM user")
    for i in c.fetchall():
        print('\n', i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    print('\n')
    db.commit()
    db.close()


# db = sqlite3.connect('user.db')
# c = db.cursor()
# c.execute("""CREATE TABLE user (
#                         name text,
#                         login text,
#                         password text,
#                         is_blocked text,
#                         sub_date date,
#                         sub_mode text
# )""")
# db.commit()
# db.close()

db = sqlite3.connect('user.db')
c = db.cursor()
c.execute("DELETE FROM user")
db.commit()
db.close()

user_1 = User('Моби', 'rasskaz')
user_2 = User('Есенин', 'stihiii', '1920qweQwe')
user_3 = User('Пушкин', 'skazka', 'qweQWEqwe1')
user_4 = User('Гоголь', 'poemaaa', 'asdhywGEEEW4')

print_sql()

user_2.block()
User.update_data(user_2)
user_3.subscription_date = date(2022,4,23)
User.update_data(user_3)
user_1.donate(10)
User.update_data(user_1)

print_sql()



