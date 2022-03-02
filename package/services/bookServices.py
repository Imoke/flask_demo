from package.models.bookModel import *


class BookService():

    @classmethod
    def saveBook(cls, name):
        return BookModel.saveBook(name)

    @classmethod
    def getAllBooksWithShelf(cls):
        return BookModel.getAllBooksWithShelf()

    @classmethod
    def getBooksWithPotentialShelf(cls):
        return BookModel.getBooksWithPotentialShelf()
