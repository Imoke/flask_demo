from peewee import *

from package.base.database import *

from package.models.entities.exampleEntities import *


class ShelfModel(ModelSchema):

    books = Related()
    potentialBooks = Related()

    class Meta:
        model = Shelf

    # 这里如果不加only， 会把所有shelf的字段全部查出来，包括books和potentialBooks
    # 而且用的手段性能非常低下
    @classmethod
    def getAllShelf(cls):
        shelfs = Shelf.select()
        return ShelfModel(many=True, only=("id", "name")).dumps(shelfs)

    @classmethod
    def getAllShelfWithBooks(cls):
        # one to many
        # http://docs.peewee-orm.com/en/latest/peewee/relationships.html#list-users-and-all-their-tweets
        shelfs = Shelf.select()
        books = Book.select()

        query = prefetch(shelfs, books)
        return ShelfModel(many=True).dumps(query)

    @classmethod
    def getShelfById(cls, id):
        shelf = Shelf.get(Shelf.id == id)
        return ShelfModel(only=("id", "name")).dumps(shelf)

    @classmethod
    def getShelfWithBooks(cls, id):
        shelf = (Shelf
                 .select(Shelf, Book)
                 .join(Book)
                 .where(Shelf.id == id))
        for shelf3 in shelf:
            print(shelf3)
        return ShelfModel().dumps(shelf)
