import threading


def do_some_work(val):
    print("doing some work in thread")
    print("echo: {}".format(val))
    return


val = "text"
# t = threading.Thread(target=do_some_work, args=(val,))
# t.start()
# t.join()


class FibonacciThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self) -> None:
        fib = [0] * (self.num + 1)
        fib[0] = 0
        fib[1] = 1
        for i in range(2, self.num + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        print(fib[self.num])


myFibTask1 = FibonacciThread(9)
myFibTask2 = FibonacciThread(2)

myFibTask1.start()
myFibTask2.start()

myFibTask1.join()
myFibTask2.join()
