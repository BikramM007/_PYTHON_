from time import sleep

class A:
    def run(self):
        for i in range(5):
            print("Bikram")
            sleep(1)

class B:
    def run(self):
        for i in range(5):
            print("Ankur")
            sleep(1)

t1 = A()
t2 = B()

t1.run()
t2.run()






# from threading import Thread
# from time import sleep

# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("1stThread")
#             sleep(1)
        
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("2ndThread")
#             sleep(1)

# t1 = A()
# t2 = B()

# t1.start()
# t2.start()