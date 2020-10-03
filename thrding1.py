from threading import Thread


def func1():
    result_sum = 0
    for i in range(1, 2000000000):
        result_sum += i
    print("Sum from func1:", result_sum)


def func2():
    result_sum = 0
    num = 0
    while num < 5:
        num += 1
        result_sum += (int(input("Enter a number: ")))

    print("Sum from func2:", result_sum)


# Modify the code given below to execute func1() and func2() in two separate threads
thread1 = Thread(target=func1)
thread1.start()
thread2 = Thread(target=func2)
thread2.start()
thread1.join()
thread2.join()
