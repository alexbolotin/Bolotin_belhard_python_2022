class Phone:
    
    def __init__(self, brand, model,issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
    
    def receive_call(name):
        print(f'Звонит {name}\n')
        return ''
    
    def get_info(self):
        s = ()
        s = self.brand, self.model, self.issue_year
        print(s)
        return ''

    def __str__(self):
        print(f'\nТелефон марки: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}\n')
        return ''
     
s21 = Phone('Samsung', 'S21', 2020)
x10 = Phone("Apple", "X10", 2021)
name1 = 'Alex'
name2 = 'Kate'

s21.get_info()
s21.__str__()
Phone.receive_call(name1)


x10.get_info()
x10.__str__()
Phone.receive_call(name2)




