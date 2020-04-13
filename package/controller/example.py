from package.base.app import webapp, helloBp
from package.services.exampleService import *

@helloBp.route("/api/hello")
def hello():
    return "Hello, Flask"

@helloBp.route("/api/hello/<name>")
def helloService(name):
    return ExampleService.hello(name)