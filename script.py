import sched, time
import requests
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    # print("Doing stuff...")
    requests.get('http://103.142.174.170:8000/ping/')
    # do your stuff
    s.enter(120, 1, do_something, (sc,))

s.enter(120, 1, do_something, (s,))
s.run()