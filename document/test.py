import schedule
import time

def do_nothing():
    print('Hello Conan')

schedule.every(5).seconds.do(do_nothing)

while 1:
    schedule.run_pending()
    time.sleep(1)