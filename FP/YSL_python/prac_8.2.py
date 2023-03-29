import time

class StopWatch:
    def __init__(self):
        self.__strt = time.time()
        self.__end = 0
        
    def start(self):
        self.__strt = time.time()
        
    def stop(self):
        self.__end = time.time()
        
    @property
    def calculate_time(self):
        return int((self.__end - self.__strt) * 1000)
        
stpwtch = StopWatch()
total = 0

stpwtch.start()
for i in range(1, 1000001):
    total += i
stpwtch.stop()

print(f"Time taken to add numbers from 1 to 1,000,000: {stpwtch.calculate_time} ms")
