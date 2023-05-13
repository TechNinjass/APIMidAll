from flask_apscheduler import APScheduler

from flaskr.db import db_instance
from flaskr.services.file import FileModelService


def task_tranfer_files():
    with db_instance.app.app_context():
        fm = FileModelService()
        fm.transfer_files()
        print(fm)

def init_apscheduler(app, scheduler_enabled=False):
    if scheduler_enabled:
        app.config['SCHEDULER_EXECUTORS'] = {"default": {"type": "threadpool", "max_workers": 10}}
        app.config['SCHEDULER_JOB_DEFAULTS'] = {"coalesce": False, "max_instances": 3}
        app.config['SCHEDULER_API_ENABLED'] = True

        scheduler = APScheduler()
        scheduler.init_app(app)
        # Set and config task jobs
        scheduler.add_job(id='task_tranfer_files', func=task_tranfer_files, trigger='cron', minute='*/1')
                         

        print("Job task_tranfer_files registered and working...")
        print(scheduler.get_jobs())
        scheduler.start()
