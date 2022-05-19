import os
import time, random
from multiprocessing import Process, Pool, Queue, Pipe

import subprocess

import threading


def run_proc(name, delay=0):
    time.sleep(delay)
    print("Run child process: %s(%s)" % (name, os.getpid()))


def write(q):
    print("%s is writing..." % os.getpid())
    for value in ['A', 'B', 'C']:
        q.put(value)
        print(value, "has put to queue")
        time.sleep(random.random())


def read(q):
    print("%s is reading..." % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue" % value)


def loop(n):
    while n > 0:
        n -= 1
        print("%s==> now n is %d" % (threading.current_thread().name, n))
        time.sleep(random.random())


def demo_process():
    print("Parent process: ", os.getpid())
    p = Process(target=run_proc, args=('test', 0.2))
    p2 = Process(target=run_proc, args=('test2', 0.5))
    print("Child process will start")
    p.start()
    p2.start()
    while p.join() or p2.join():
        print("no")
    print("Child process end")

    pl = Pool(4)
    for i in range(5):
        pl.apply_async(run_proc, args=('test:%d' % i, i * 0.1))

    print("pool apply")

    pl.close()
    pl.join()
    print("All done!")

    r = subprocess.call(['nslookup', 'www.python.org'])
    print(r)

    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


count = 0


def add_count():
    for i in range(10):
        time.sleep(random.random())
        global count
        count += 1

    print("count执行加法了：", count)


def sub_count():
    for i in range(10):
        time.sleep(random.random())
        global count
        count -= 1
    print("count执行减法了：", count)


def wait_ts(l):
    for t in l:
        t.join()


if __name__ == "__main__":
    t = threading.Thread(target=loop, args=(3,), name='LoopThread')
    t.start()
    t.join()
    print('Thread finish.')

    L = []
    for i in range(4):
        t1 = threading.Thread(target=add_count if i % 2 == 0 else sub_count, name='T-%d' % i)
        L.append(t1)
        t1.start()

    wait = threading.Thread(target=wait_ts, args=(L,), name='Wait_Thread')
    wait.start()
    wait.join()
    print("完成了，count = ", count)

    lock = threading.Lock()

    # 假定这是你的银行存款:
    balance = 0


    def change_it(n):
        lock.acquire()
        # 先存后取，结果应该为0:
        global balance
        balance = balance + n
        balance = balance - n
        lock.release()


    def run_thread(n):
        for i in range(2000000):
            change_it(n)


    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
