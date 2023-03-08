""" py thread local """

import time
import threading

mydata = threading.local()

def fn2() -> None:
    """ fn2 """
    time.sleep(1)
    print("fn2 " + str(threading.get_native_id()))
    print(mydata.msg)

def fn1(msg: str) -> None:
    """ fn1 """
    time.sleep(1)
    print("assign " + msg + " to thread local " + str(threading.get_native_id()))
    mydata.msg = "python is cool, " + msg + str(threading.get_native_id())
    time.sleep(1)
    fn2()


thread1 = threading.Thread(target=fn1, args=("thread1",))
thread1.start()

thread2 = threading.Thread(target=fn1, args=("thread2",))
thread2.start()


thread1.join()
thread2.join()



print("all done")