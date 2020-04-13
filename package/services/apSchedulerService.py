from datetime import date, datetime
from package.base.app import scheduler

class ApScheduler():
    @classmethod
    def my_job(cls, name):
        print("Hello, ApScheduler: %s, time:%s" % (name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    @classmethod
    def add_job(self, name):
        scheduler.add_job(ApScheduler.my_job, 'interval', minutes=1, start_date="2020-04-10 09:30:00", end_date="2020-04-27 11:00:00", args=[name])
        return "add scheduler success"

    @classmethod
    def list_jobs(self):
        jobs=scheduler.get_jobs()
        ret_jobs=[]
        for job in jobs:
            name=job.name
            id=job.id
            next_run_time=job.next_run_time
            ret_jobs.append("Job name: %s, id: %s, next_run_time: %s" % (name, id, next_run_time))
        return '\n'.join(ret_jobs)
