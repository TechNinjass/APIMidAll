import json
from datetime import datetime

from flask_apscheduler import APScheduler

import flaskr.cloud.set_parameters as sp
from flaskr.db import db_instance
from flaskr.services.file import FileModelService


def task_transfer_files(scheduler):
    with db_instance.app.app_context():
        with open(sp.PARAMETERS_TRANSFER) as f:
            parameters = json.load(f)
            minutes = int(parameters["minutes"])
            current_job = scheduler.get_job('task_transfer_files')
            if current_job is None:
                print(f"Creating new job with interval {minutes} minutes at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                scheduler.add_job(id='task_transfer_files', func=task_transfer_files, trigger='cron', minute=f'*/{minutes}', args=[scheduler])
            elif current_job.args[0] != minutes:
                print(f"Updating job interval from {current_job.args[0]} to {minutes} minutes at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                scheduler.remove_job('task_transfer_files')
                scheduler.add_job(id='task_transfer_files', func=task_transfer_files, trigger='cron', minute=f'*/{minutes}', args=[scheduler])
        fm = FileModelService()
        fm.transfer_files()
        print(fm)


def init_apscheduler(app, scheduler_enabled=False, job_id='task_transfer_files'):
    if scheduler_enabled:
        app.config['SCHEDULER_EXECUTORS'] = {"default": {"type": "threadpool", "max_workers": 10}}
        app.config['SCHEDULER_JOB_DEFAULTS'] = {"coalesce": False, "max_instances": 3}
        app.config['SCHEDULER_API_ENABLED'] = True

        with open(sp.PARAMETERS_TRANSFER) as f:
            parameters = json.load(f)
            minutes = int(parameters["minutes"])
        print(minutes, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        scheduler = APScheduler()
        scheduler.init_app(app)

        scheduler.add_job(id=job_id, func=task_transfer_files, trigger='cron', minute=f'*/{minutes}', args=[scheduler])

        print("Job task_tranfer_files registered and working...")
        print(scheduler.get_jobs())
        scheduler.start()