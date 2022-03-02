from package.base.app import webapp, commonBp, nacosClient, apolloClient
from package.models.shelfModal import ShelfModel
from package.services.bookServices import BookService


@commonBp.route("/")
def home():
    return "Hello, Flask!"


@commonBp.route("/addbook/<name>")
def saveBook(name):
    return BookService.saveBook(name)


@commonBp.route("/booksPoentailShelfs")
def booksPoentailShelfs():
    return BookService.getBooksWithPotentialShelf()


@commonBp.route("/books")
def booksWithshelf():
    return BookService.getAllBooksWithShelf()


@commonBp.route("/shelfs")
def shelfs():
    return ShelfModel.getAllShelf()


@commonBp.route("/shelf/<id>")
def shelfById(id):
    return ShelfModel.getShelfById(id)


@commonBp.route("/shelfbooks")
def shelfWithBbooks():
    return ShelfModel.getAllShelfWithBooks()


@commonBp.route("/shelfbooks/<id>")
def shelfWithBooksById(id):
    return ShelfModel.getShelfWithBooks(id)

# example for remote call
@commonBp.route("/nodejs")
def nodejs():
    return nacosClient.remoteCall("nodejs.test.domain", '/')

# exmaple for get apollo value
@commonBp.route("/hello/<name>")
def hello_there(name):
    return {
        "timeout": apolloClient.get_value("timeout"),
        #"common": apolloClient.get_value("common", namespace="TEST1.common")
    }
