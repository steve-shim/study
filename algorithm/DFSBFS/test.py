print(f'asdhi'.rjust(6))
import GPUtil
import time
from threading import Thread
class GpuMonitor(Thread):
  def init(self):
    super(GpuMonitor, self).init()
    self.use = False
    gpu = GPUtil.getGPUs()[0]
    self.memTotal = gpu.memoryTotal
    
    self.stopped = False
    self.delay = 0.5  # sec
    #self.max_util = 0
    self.start()
    
    # collect
    self.stats = []
    self.mems = []

  def run(self):
    while not self.stopped:
      gpu = GPUtil.getGPUs()[0]
      self.stats.append(gpu.load * 100)
      self.mems.append(gpu.memoryUsed)
      time.sleep(self.delay)
        
  def stop(self):
    self.stopped = True

  def avg_gpu_util(self):
    return sum(self.stats) / len(self.stats)

  def avg_mem_util(self):
    return sum(self.mems) / len(self.mems)
  
#!/usr/bin/env python
import psutil
# gives a single float value
print(psutil.cpu_percent())
# gives an object with many fields
print(psutil.virtual_memory())
# you can convert that object to a dictionary 
print(dict(psutil.virtual_memory()._asdict()))
# you can have the percentage of used RAM
print(psutil.virtual_memory().percent)
# you can calculate percentage of available memory
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)