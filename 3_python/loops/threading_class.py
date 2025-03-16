import threading
import time


class CountdownThread(threading.Thread):
    def __init__(self, count, name, t_to_sync=None, daemon=False):
        threading.Thread.__init__(self, name=name, daemon=daemon)
        self.count = count
        self.t = t_to_sync
        self.result = False
        self.trace = None

    def start(self):
        super(CountdownThread, self).start()

    def run(self):
        try:
            while True:
                print(threading.current_thread().getName())
                if self.t and not self.t.is_not_alive():
                    print(self.t.is_not_alive(), self.t.name)
                    self.t.setDaemon(True)
                    break
                print("CountdownThread ", self.count)
                self.count -= 1
                time.sleep(0.2)
            self.result = True
            return self.count
        except Exception as e:
            self.trace = e
            print(self.trace)


t1 = CountdownThread(10, "Ira")
t2 = CountdownThread(20, "Ira2", t1, daemon=True)
t1.setDaemon(True)

res1 = t1.start()
res2 = t2.start()
