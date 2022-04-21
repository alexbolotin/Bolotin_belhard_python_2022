from datetime import date, datetime, timedelta, time
import re
import random
import time
class User():
    __name: str
    __login: str
    __password: str
    is_blocked: bool
    subscription_date: date
    subscription_mode: int
    
    def __init__(self, __name, __login, __password = '', is_blocked = False, subscription_date = None, subscription_mode = 'free'):
        
        while not self.__check___name(__name):
            __name = input('Введите новое имя:')
            self.__check___name(__name)
            self.__name = __name
            break 
        else:
            self.__name = __name

        while not self.__check___login(__login, __name):
            __login = input('Введите новый логин:')
            self.__check___login(__login, __name)
            self.__login = __login
            break 
        else:
            self.__login = __login
        
        self.__password = self.__check___password(__password)

        self.is_blocked = is_blocked

        if subscription_date is None:
            self.subscription_date = date.today() + timedelta(days = 30)
        else:
            self.subscription_date = subscription_date
    
        self.subscription_mode = subscription_mode

    def get_info(self):
            if self.is_blocked:
                print(f'Извините, пользователь {self.__name} заблокирован, обратитесь в техподдержку!')
            else:
                print(f'name: {self.__name}\nlogin: {self.__login}\npassword: ******\nIs_blocked: {self.is_blocked}\nsub_date: {self.subscription_date}\nSub_mode: {self.subscription_mode}\n ')

    def block(self):
        self.is_blocked = True

    def unblock(self):
        self.is_blocked = False

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
        if re.match(r'[A-Za-z0-9_]{6,}$', __login):
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


user_1 = User('Моби', 'rasskaz')
user_2 = User('Есенин', 'stihiii', '1920qweQwe')
user_3 = User('Пушкин', 'skazka', 'qweQWEqwe1')
user_4 = User('Гоголь', 'poemaaa', 'asdhywGEEEW4')

user_1.get_info()
# user_2.get_info()
# user_2.block()
# user_2.get_info()
# user_2.unblock()
# user_2.get_info()

# date1 = date(2020,3,20)
# date2 = date(2022,1,15)
# date3 = date(2023,5,31)
# data4 = date(2022,4,23)
# user_1.check_subscr()
# user_2.subscription_date = data4
# user_2.check_subscr()
# user_1.donate(10)
# user_1.get_info()

# user_1.check___password()
# user_2.check___password()
# new___password = '123'
# user_2.change_pass(new___password)




