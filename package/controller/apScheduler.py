from package.base.app import webapp, helloBp
from package.services.apSchedulerService import *

@helloBp.route("/api/scheduler/job/<name>")
def addJob(name):
    return ApScheduler.add_job(name)

@helloBp.route("/api/scheduler/job/io/<name>")
def addIoJob(name):
    return ApScheduler.add_iojob(name)

@helloBp.route("/api/scheduler/job/list")
def jobList():
    return ApScheduler.list_jobs()

@helloBp.route("/api/scheduler/job/remove/<id>")
def removeJob(id):
    return ApScheduler.remove_job(id)

@helloBp.route("/api/scheduler/job/pause/<id>")
def pauseJob(id):
    return ApScheduler.pause_job(id)

@helloBp.route("/api/scheduler/job/resume/<id>")
def resumeJob(id):
    return ApScheduler.resume_job(id)

@helloBp.route("/api/scheduler/job/pause/<id>")
def rescheduleJob(id):
    return ApScheduler.rescheduler_job(id)
