import threading, logging

logging.basicConfig(level=logging.INFO, format="[-] %(threadName)s %(message)s")


def work(barrier: threading.Barrier):
    logging.info("n_waiting = {}".format(barrier.n_waiting))  # 等待的线程数
    bid = barrier.wait()  # 参与者的id，返回0到线程数减1的数值
    logging.info("after barrier {}".format(bid))  # 栅栏之后


barrier = threading.Barrier(3)  # 3个参与者，每3个开闸放行，0,1,2  4,5,6

for x in range(1, 4):  # 所有参数者个数，4,5,6,10,15
    threading.Event().wait(1)
    threading.Thread(target=work, args=(barrier,), name="Barrier-{}".format(x)).start()
