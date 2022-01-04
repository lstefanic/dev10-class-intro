class Book():
    """Book class"""
    def __init__(self,title,author,year,isbn):
        self._title = title
        self._author = author
        self._publication_year = year
        self._isbn = isbn
    
    def read(self):
        print("Reading")
    
    def bookmark(self):
        print("Bookmarking")