import psutil
import numpy as np
from threading import Thread
import time

class cpu_monitor(Thread):
    def __init__(self):
        super(cpu_monitor, self).__init__()
        self.cpus = list()
        self.mems = list()
        self.stop_ = False
        self.delay = 0.3
        self.start()
        
    def run(self):
        while True:
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory()._asdict()['used']
            self.cpus.append(cpu)
            self.mems.append(mem)
            time.sleep(self.delay)
            if self.stop_:
                break
    
    def stop(self):
        self.stop_ = True

    def summary(self):
        print('cpus', sum(self.cpus) / len(self.cpus))
        print('mems', sum(self.mems) / len(self.mems))

monitor = cpu_monitor()
def function():
    print('function call')
    for _ in range(10):
        #monitor.check()
        a = np.random.randn(200, 400)
        b = np.random.randn(200, 400)
        c = a*b
    

if __name__ == '__main__':
    function()
    function()
    function()
    function()
    function()
    function()
    function()
    function()
    monitor.stop()
    monitor.summary()