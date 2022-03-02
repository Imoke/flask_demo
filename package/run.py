# 实例化flask app
from package.base.app import *
# 初始化数据库
from package.base.database import *
# 挂在路由
from package.controller import *

# 蓝图必须放在所有视图后面注册
webapp.register_blueprint(blueprint=commonBp, url_prefix='/kpi')
