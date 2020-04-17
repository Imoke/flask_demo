from datetime import date, datetime
from package.base.app import scheduler

class ApScheduler():
    @classmethod
    def my_job(cls, name):
        print("Hello, ApScheduler: %s, time:%s" % (name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    @classmethod
    def fib_loop(cls, n):    
        a, b = 0, 1
        for i in range(n + 1):
            a, b = b, a + b
        
        return a

    @classmethod
    def call_fib(cls, n):
        n=int(n)
        begin=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for i in range(n):
            ApScheduler.fib_loop(i)
        print(n, "begin: ", begin, "end", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    @classmethod
    def add_job(self, name):
        job=scheduler.add_job(ApScheduler.call_fib, 'interval', minutes=1, start_date="2020-04-10 09:30:00", end_date="2020-04-27 11:00:00", executor='processpool', args=[name])
        return "add job success, job id: %s" % job.id

    @classmethod
    def add_iojob(self, name):
        job=scheduler.add_job(ApScheduler.my_job, 'interval', minutes=1, start_date="2020-04-10 09:30:00", end_date="2020-04-27 11:00:00", executor='default', args=[name])
        return "add job success, job id: %s" % job.id

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

    @classmethod
    def remove_job(self, id):
        scheduler.remove_job(id, 'default')
        return "pause job success, job id: %s" % id

    @classmethod
    def pause_job(self, id):
        job=scheduler.pause_job(id, 'default')
        return "pause job success, job id: %s" % job.id

    @classmethod
    def resume_job(self, id):
        job=scheduler.resume_job(id, 'default')
        return "resume job success, job id: %s" % job.id

    @classmethod
    def rescheduler_job(self, id):
        job=scheduler.reschedule_job(id, trigger='cron', minute='*/5')
        return "reschedule job success, job id: %s" % job.id