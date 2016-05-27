import multiprocessing
import os

class processWrapper():
    def __init__(self,proc,res,brk=lambda x: False):
        self.process = proc
        self.result = res
        self.bp = brk
    def run(self,pid,data,bpflag):
        result = self.process(data)
        self.result.put([data,result])
        if self.bp(result):
            print(pid,data,result)
        bpflag.put(self.bp(result))

class bpHolder():
    def __init__(self):
        self.data = False
    def __repr__(self):
        return self.data.__repr__()
    def __bool__(self):
        return self.data
    def put(self,newData):
        self.data = self.data or newData

class resultGetter():
    def __init__(self,dataholder):
        self.data = dataholder
    def put(self,newData):
        self.data.put(newData[1])
    def get(self):
        return self.data

def rotatePool(targetProcess,dataPool,poolSize=os.cpu_count()):
    processPool = []
    breakCheck = bpHolder()
    for i in range(poolSize):
        tmpProcess = multiprocessing.Process(target=targetProcess.run,args=(i,dataPool.pop(),breakCheck))
        processPool.append(tmpProcess)
        processPool[i].start()
    while len(dataPool) > 0 and (not breakCheck):
        nextAvail = 0
        while nextAvail < poolSize and processPool[nextAvail].is_alive():
            nextAvail += 1
        if nextAvail < poolSize:
            processPool[nextAvail].join()
            tmpProcess = multiprocessing.Process(target=targetProcess.run,args=(nextAvail,dataPool.pop(),breakCheck))
            processPool[nextAvail]=tmpProcess
            processPool[nextAvail].start()
    for i in range(poolSize):
        processPool[i].join()

# Example Process Starts Below:
def procWrap(data):
    import example as test
    result = test.primeTest(data)
    print(data,result)
    return result

def bWrap(result):
    return result

def main():
    import example as test
    results=multiprocessing.SimpleQueue()
    processWrap = processWrapper(procWrap,results,bWrap)
    pendingPool = []
    for i in range(100):
        pendingPool.append(test.randNum(6))
    rotatePool(processWrap,pendingPool)
    while not results.empty():
        print(results.get())

if __name__ == '__main__':
    main()
