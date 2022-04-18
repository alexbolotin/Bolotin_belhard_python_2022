from datetime import date,datetime, timedelta
import re
import random

class User():
    name: str
    login: str
    password: str
    is_blocked: bool
    subscription_date: int
    subscription_mode: int

    CURRENT_Data = date.today()
    q = date.today() + timedelta(days = 30)

    def __init__(self, name, login, password, is_blocked = False, subscription_date =  q, subscription_mode = 'free'):
       
        while User.check_name(name) is False:
            name = input('Введите новое имя:')
            User.check_name(name)
            self.name = name
            break 
        else:
            self.name = name

        while User.check_login(login, name) is False:
            login = input('Введите новый логин:')
            User.check_login(login,name)
            self.login = login
            break 
        else:
            self.login = login

        self.password = password
        self.is_blocked = is_blocked
        self.subscription_date = subscription_date
        self.subscription_mode = subscription_mode

    def get_info(self):
            if self.is_blocked is True:
                print(f'Извините, пользователь {self.name} заблокирован, обратитесь в техподдержку!')
            else:
                print(f'Name: {self.name}\nLogin: {self.login}\nPassword: {self.password}\nIs_blocked: {self.is_blocked}\nsub_date: {self.subscription_date}\nSub_mode: {self.subscription_mode}\n ')


    def block(self):
        self.is_blocked = True

    def unblock(self):
        self.is_blocked = False


    def check_subscr(self,val = CURRENT_Data):
        CURRENT_Data = date.today()
        if self.subscription_date <= val:
            print(f'{self.name} - пополните счет, подписка закончилась')
        else:
            data = self.subscription_date - CURRENT_Data
            print(f'{self.name} У вас осталось {data.days} дней подписки, вид подписки: {self.subscription_mode}')
    
    def check_name(name):
        if len(re.findall("[а-яА-Я]",name)) == len(name):
            return True
        else:
            print(f'{name} - Поменяйте Ваше имя!')
            return False
        

    def check_login(login,name):
        if re.match(r'[A-Za-z0-9_]{6,}', login):
            return True
        else:
           print(f'{name} - Поменяйте Ваш логин!')
           return False

    def check_password(self):
        val = self.password
        if (re.search(r'[A-Z]{1,}', val) and re.search(r'[a-z]{1,}', val) and re.search(r'[0-9]{1,}', val)):
            print(f'{self.name} Ваш пароль соответствует всем критериям')
        else:
           print(f'{self.name} - Поменяйте Ваш пароль!')

    def change_pass(self,val):
        if val == '':
            str1 = '1234567890'
            str2 = 'qwertyuiopasdfghjklzxcvbnm'
            str3 = str2.upper()
            str4 = str1+str2+str3
            l = list(str4)
            new_password = ''
            for x in range(15):
                new_password = new_password + random.choice(l)   
            val = new_password
        
        if (re.search(r'[A-Z]{1,}', val) and re.search(r'[a-z]{1,}', val) and re.search(r'[0-9]{1,}', val)):
            print(f'{self.name} - вот Ваш новый пароль, сохраните и запомните его:', val)
            self.password = val
        else:
           print(f'{self.name} - Поменяйте Ваш пароль!')


user_1 = User('Моби', 'rasskaz', 'qwe123qweQ')
user_2 = User('Есенин', 'stihiii', '1920qweqwe')
user_3 = User('Пушкин', 'skazka', 'qweQWEqwe1')
user_4 = User('Гоголь', 'poemaaa', 'asdhywGEEEW4')

user_1.get_info()
user_2.get_info()
user_2.block()
user_2.get_info()
user_2.unblock()
user_2.get_info()

# date1 = date(2020,3,20)
# date2 = date(2022,1,15)
# date3 = date(2023,5,31)
# data4 = date(2022,4,20)
# # user_1.check_subscr()
# # user_2.subscription_date = data4
# user_2.check_subscr()

user_1.check_password()
user_2.check_password()
new_password = ''
user_2.change_pass(new_password)




