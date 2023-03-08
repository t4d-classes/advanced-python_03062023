""" py thread """

import time
import threading

def do_it() -> None:
    """ do it """
    print("start it: " + threading.current_thread().name + ", " + str(threading.get_native_id()))
    time.sleep(2)
    print("finish it: " + threading.current_thread().name + ", " + str(threading.get_native_id()))

thread1 = threading.Thread(target=do_it, args=tuple(), name="thread1")
thread1.start()

thread2 = threading.Thread(target=do_it, args=tuple(), name="thread2")
thread2.start()

thread1.join()
thread2.join()

print("made it here: " + threading.current_thread().name)