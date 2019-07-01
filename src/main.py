from datetime import datetime
import time
import threading

currentStatus = 0
running = True

def thread_execute():
    while True:
        if running == False:
            break
        print('>> thread: current status: {}'.format(currentStatus))
        time.sleep(1)

    print('thread is over')

def main():
    global currentStatus
    global running

    athread = threading.Thread(target = thread_execute)
    athread.start()

    index = 0
    maxindex = 5
    while True:
        index += 1
        dt = datetime.now()
        sec = dt.second
        currentStatus = sec
        print("index {}, current second: {}".format(index, sec))
        if index > maxindex:
            break
        time.sleep(3)

    running = False
    print('main thread is over')
    time.sleep(3)
    print('end')


if __name__ == '__main__':
    main()