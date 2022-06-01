from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    # https://python-course.eu/oop/the-abc-of-abstract-base-classes.php
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title, author, price):
        super().__init__(title, author, price)
        self.price = price

    
    def display():
        super().display()
        print("Some implementation!")


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()