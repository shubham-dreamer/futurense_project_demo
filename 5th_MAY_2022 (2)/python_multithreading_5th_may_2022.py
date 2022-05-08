import time
import threading

def fun1(name):
   # print("one")
    print(name)
    print(time.ctime())
    time.sleep(2)

def fun2(name):
    #print("two")
    print(name)
    print(time.ctime())
# fun1()
# fun2()

#creating threads

t1=threading.Thread(target=fun1,args=("dhoni",))
t2=threading.Thread(target=fun2,args=("Kholi",))


#running threads
t1.start()
t2.start()


#use join to close the threads so that all child's thread get completed their task and close and then only parent's thread close
t1.join()
t2.join()