import datetime, time
import random

class Phone:
    brand: str
    model: str
    issue_year: int
    call_history: list
    miss_call: list
    is_busy: bool
    incoming_sms: list
    start_call:time
    

    def __init__(self, brand, model,issue_year, is_busy = False):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.call_history = []
        self.miss_call = []
        self.is_busy = False
        self.incoming_sms = []
        self.start_call = 0

    def receive_call(self,name,tell):
        if self.is_busy is False:
            self.start_call = datetime.datetime.today()
            self.is_busy = True
            print(f'Звонит {name}\n')
            self.call_history.append([self.start_call,name, tell])
        else:
            print('Занято')
            self.miss_call.append([self.start_call,name, tell])
        

    def end_call(self):
        t2 = datetime.datetime.now()
        t = t2 - self.start_call
        self.is_busy = False
        print(f'Звонок завершен.Время разговора: {t}')
        self.start_call = 0
    
    def history(self):
        print('История звонков:')
        for i in self.call_history:
            print(i)

    def miss_history(self):
        for i in self.miss_call:
            print('Пропущенный звонок:', i)

    def get_info(self):
        s = ()
        s = self.brand, self.model, self.issue_year, self.call_history
        print(s)
        return ''

    def __str__(self):
        print(f'\nТелефон марки: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}\n История пропущенных звонков: {self.call_history}')
        return ''

    def recieve_sms(self,name,txt):
        time = datetime.datetime.today()
        t = time.strftime("%Y-%m-%d %H.%M.%S")
        self.incoming_sms.append([name, t, txt])
        print(f'new sms: from {name} : {txt}')

    def sms_history(self):
        print(f'\nsms history:')
        for i in self.incoming_sms:
            print(i)


def random_tel():
    str1 = '1234567890'
    l = list(str1)
    new_tel = '+375'
    for x in range(9):
        new_tel = new_tel + random.choice(l)   
    return new_tel

s21 = Phone('Samsung', 'S21', 2020)
x10 = Phone("Apple", "X10", 2021)
name1 = 'Alex'
name2 = 'Kate'
tell1 = random_tel()
tell2 = random_tel()
txt1 = 'hello'
txt2 = 'new sms'

# s21.recieve_sms(name1,txt1)
# s21.recieve_sms(name2,txt2)
# s21.sms_history()

# s21.receive_call(name1,tell1)
# time.sleep(2)
# s21.receive_call(name2,tell2)
# time.sleep(1)
# s21.receive_call(name2,tell2)
# time.sleep(1)
# s21.receive_call(name2,tell2)
# time.sleep(1)
# s21.end_call()

# s21.miss_history()
# s21.receive_call(name1,tell2)
# time.sleep(1)
# s21.receive_call(name1,tell1)
# time.sleep(1)
# s21.end_call()
# s21.miss_history()
# s21.history()








