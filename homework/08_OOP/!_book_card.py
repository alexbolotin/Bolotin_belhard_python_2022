class BookCard():
    def __init__(self,author:str, title:str, year:int):
        self.__author = author
        self.__title = title
        self.__year = year

    def get_info(self):
        print(f'Книга автора: {self.__author}\nОписание: {self.__title}\nГод впуска: {self.__year}\n ')
        return ''

    def __repr__(self):
        return self.__author

    @property
    def year(self):
        return self.__year

class Books:
    def __init__(self, l):
        self.books = l

    def __getitem__(self,item):
        return self.books[item]

    def sort(self,q):
        return sorted(books1, key =  q)


book1 = BookCard('moby', 'rasskaz', 1860)
book2 = BookCard('esenin', 'stihi', 1920)
book3 = BookCard('pushkin', 'skazka', 1830)

book1.get_info()
book2.get_info()
book3.get_info()

books1 = Books([book1,book2,book3])


print(books1.sort( lambda x: x.year))

