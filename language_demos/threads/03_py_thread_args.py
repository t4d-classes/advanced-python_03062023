""" py thread """

import time
import threading

def do_it(msg: str, msg2: str) -> None:
    """ do it """
    print("start it: ", msg)
    time.sleep(2)
    print("finish it: ", msg2)

thread1 = threading.Thread(
    target=do_it, args=('hello', 'goodbye'), name="thread1")
thread1.start()

thread2 = threading.Thread(
    target=do_it, args=('python is fun', 'fun'), name="thread2")
thread2.start()

thread1.join()
thread2.join()

print("made it here: " + threading.current_thread().name)