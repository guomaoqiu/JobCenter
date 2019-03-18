from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(sensor, 'interval', seconds=2)
scheduler.start()

app = Flask(__name__)


@app.route("/home")
def home():
    """ Function for test purposes. """
    return "Welcome Home :) !"


if __name__ == "__main__":
    app.run()