from package.base.app import *
from package.controller import *

webapp.register_blueprint(blueprint=helloBp, url_prefix='/hello')
webapp.register_blueprint(blueprint=viewBp, url_prefix='/view')