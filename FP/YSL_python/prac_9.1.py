from YSL_io import *

class Book:
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    
    def __init__(self, title: str, author: str, format: str, pages: int):
        super().__init__(title, author)
        self.format = format
        self.pages = pages
        if format not in ['PDF', 'EPUB', 'MOBI', 'AZW']:
            raise ValueError("Invalid EBook format")
    
    @property
    def display(self):
        printMGNTA('Title', end=' : ')
        print(self.title)
        printBLU('Author', end=' : ')
        print(self.author)
        printORNG('Format', end=' : ')
        print(self.format)
        printGRN('Number of pages', end=' : ')
        print(self.pages)

class Audiobook(Book):
    
    def __init__(self, title: str, author: str, format: str, length: int):
        super().__init__(title, author)
        self.format = format
        self.length = length
        if format not in ['MP3', 'WMA', 'WAV']:
            raise ValueError("Invalid Audiobook format")
        
    @property
    def display(self):
        printMGNTA('Title', end=' : ')
        print(self.title)
        printBLU('Author', end=' : ')
        print(self.author)
        printORNG('Format', end=' : ')
        print(self.format)
        printGRN('Track length', end=' : ')
        print(f'{self.length} minutes')

print()
bg = Audiobook(title='Bhagavad Gita AsItIs', author='A.C. Bhaktivedanta Swami Srila Prabhupada', format='MP3', length=1620)
bg.display

print()
sb = EBook(title='Srimad Bhagavatam', author='A.C. Bhaktivedanta Swami Srila Prabhupada', format='PDF', pages=12000)
sb.display