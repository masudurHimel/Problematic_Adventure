import time
import datetime
import sched

scheduler = sched.scheduler(datetime.datetime.now, time.sleep)
t = datetime.datetime.now() + datetime.timedelta(minutes=1)

a = time.mktime(t.timetuple()) + t.microsecond / 1E6


def test_okay():
    print("Hello Masud")


e_x = scheduler.enterabs(t, 0, test_okay, argument=())

print("asdad")
scheduler.run()

print("asdagvvvv")
