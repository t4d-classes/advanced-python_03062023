""" py thread class """

import threading


class DoItThread(threading.Thread):
    """ do it thread """

    def __init__(self, msg: str):
        threading.Thread.__init__(self)
        self.msg = msg

    def run(self) -> None:

        print(self.msg + " " + str(threading.get_native_id()))
        self.whoami("run method")

    def whoami(self, location: str) -> None:
        """ whoami """
        print(f"{self.msg}, {location}, {str(threading.get_native_id())}")


print("main thread id: " + str(threading.get_native_id()))

some_thread = DoItThread("a message of hope and peace")

some_thread.start()

some_thread.whoami("main script")

some_thread.join()