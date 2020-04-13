from flask import Flask, Blueprint
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
webapp = Flask(__name__)
## scheduler = BackgroundScheduler()



jobstores = {
    'default': SQLAlchemyJobStore(url='postgres://pgsql:pswd@192.168.1.61:5433/python')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

scheduler.start()
helloBp = Blueprint('hello', __name__)
viewBp = Blueprint('view', __name__)
