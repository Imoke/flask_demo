from package.base.app import webapp, helloBp
from package.services.apSchedulerService import *

@helloBp.route("/api/scheduler/<name>")
def addJob(name):
    return ApScheduler.add_job(name)

@helloBp.route("/api/scheduler/list")
def jobList():
    return ApScheduler.list_jobs()