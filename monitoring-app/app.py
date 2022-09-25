from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape
from modules.usage_db_i import *
from modules.usage import *
from crontab import CronTab
import os


def start_crontab():
    # get working dir
    work_dir = os.getcwd()
    # setup crontabz
    cron = CronTab(user=True)
    job = cron.new(
        command=f"python3 {work_dir}/monitoring-app/collect_data.py")
    job.minute.every(1)
    cron.write()
    print("Started crontab")


class FlaskApp(Flask):
    def run(self, host='0.0.0.0', port=None, debug=None, load_dotenv=True, **options):
        if not self.debug or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
            with self.app_context():
                init()
                start_crontab()
        super(FlaskApp, self).run(host=host, port=port,
                                  debug=debug, load_dotenv=load_dotenv, **options)


app = FlaskApp(__name__)


# @app.route("/greet/<name>")
# def hello(name=None):
#     return render_template("hello.html", name=name)


# api for getting cpu utilization stored in database
@app.route("/api/cpu_util")
def cpu_util():
    all_param = request.args.get('all', default=False, type=bool)
    hour_param = request.args.get('hour', default=None, type=int)
    if all_param:
        return get_all_usage("c")
    return get_usage("c", hour_param)

# api for getting current cpu utilization


@app.route("/api/cpu_util_current")
def cpu_util_current():
    return get_cpu_util()


# api for getting disk usage stored in database
@app.route("/api/disk_usage")
def cpu_disk():
    all_param = request.args.get('all', default=False, type=bool)
    hour_param = request.args.get('hour', default=None, type=int)
    if all_param:
        return get_all_usage("d")
    return get_usage("d", hour_param)


# api for getting current disk usage
@app.route("/api/disk_usage_current")
def disk_usage_current():
    return get_disk_usage()

# api for memory usage


@app.route("/api/memory_usage")
def memory_usage():
    all_param = request.args.get('all', default=False, type=bool)
    hour_param = request.args.get('hour', default=None, type=int)
    if all_param:
        return get_all_usage("m")
    return get_usage("m", hour_param)

    # api for current memory usage


@app.route("/api/memory_usage_current")
def memory_usage_current():
    return get_memory_usage()

# api to setup database


@app.route("/api/setup")
def reset():
    init()
    return {"message": "database setup"}


app.run()
