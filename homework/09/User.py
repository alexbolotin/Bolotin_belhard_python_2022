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
    
    def __init__(self, name, login, password = '', is_blocked = False, subscription_date = None, subscription_mode = 'free'):
        
        while not self.__check__name(name):
            name = self.__new_name()
        else:
            self.__name = name

        while not self.__check__login(login, name):
            login = self.__new_login()
        else:
            self.__login = login
        
        self.__password = self.__check__password(password)

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

    def __new_name(self):
        return input('Введите новое имя:')

    def __new_login(self):
        return input('Введите новый логин:')

    def check_subscr(self):
        
        if self.subscription_date <= date.today():
            print(f'{self.__name} - пополните счет, подписка закончилась\n')
        else:
            data = self.subscription_date - date.today()
            print(f'{self.__name} У вас осталось {data.days} дней подписки, вид подписки: {self.subscription_mode}')
    
    def donate(self,val:int):
        self.subscription_mode = 'paid'
        self.subscription_date += timedelta(days = val)

    def __check__name(self, name):
        if len(re.findall("[а-яА-Я]",name)) == len(name):
            return True
        else:
            print(f'{name} - Поменяйте Ваше имя!')
            return False
        
    def __check__login(self,login,name):
        if re.match(r'^[A-Za-z0-9_]{6,}$', login):
            return True
        else:
           print(f'{name} - Поменяйте Ваш логин!')
           return False

    def __check__password(self, password):
        if self.__check__password_pattern(password):
            return password
        else:
            return self.__change_pass(password)

    def __check__password_pattern(self, password):
            if re.search(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z_-]{6,}$', password):
                return True
            else:
                return False

    def __change_pass(self,password):
            if self.__check__password_pattern(password):
                print('Вы успешно сменили пароль.')
                return ''
            else:
                print(f'{self.__name} - Пароль небезопасен. Пароль будет сгенерирован системой.')
                time.sleep(1)
            while not self.__check__password_pattern(password):
                str1 = '1234567890'
                str2 = 'qwertyuiopasdfghjklzxcvbnm'
                str3 = str2.upper()
                str4 = str1+str2+str3
                l = list(str4)
                new__password = ''
                for x in range(10):
                    new__password = new__password + random.choice(l)   
                password = new__password
            print(f'{self.__name} - вот Ваш новый пароль, сохраните и запомните его: {password}\n')
            return password


user_1 = User('Моби', 'rasskaz')
user_2 = User('Есенин', 'stihiii', '1920qweQwe')
user_3 = User('Пушкин', 'skazka', 'qweQWEqwe1')
user_4 = User('Гоголь', 'poemaaa', 'asdhywGEEEW4')

user_1.get_info()
user_2.get_info()
user_2.block()
user_2.get_info()
user_2.unblock()
user_2.get_info()


data4 = date(2022,4,23)
user_1.check_subscr()
user_2.subscription_date = data4
user_2.check_subscr()
user_1.donate(10)

user_1.get_info()





