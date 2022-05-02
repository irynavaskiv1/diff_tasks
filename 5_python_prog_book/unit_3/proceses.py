import signal
import time


def now(): return time.asctime()


def on_signal(signum, stackframe=None):
    print('Go alarm ', signum, 'at ', now())


while True:
    print('Setting at,', now())
    signal.signal(signal.SIGALRM, on_signal)
    signal.alarm(5)
    signal.pause()
