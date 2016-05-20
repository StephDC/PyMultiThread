class calcList():
    def __init__(self,inputData=[]):
        self.data = list(inputData)
    def __mul__(self,a):
        tmp = []
        for i in range(len(self.data)):
            tmp.append(a*self.data[i])
        return calcList(tmp)
    def __add__(self,a):
        tmp = []
        for i in range(len(self.data)):
            tmp.append(a+self.data[i])
        return calcList(tmp)
    def __truediv__(self,a):
        return self.__mul__(1/a)
    def __floordiv__(self,a):
        tmp = []
        for i in range(len(self.data)):
            tmp.append(self.data[i]//a)
    def __iter__(self):
        return self.data.__iter__()
    def __repr__(self):
        return self.data.__repr__()
    def __append__(self,a):
        return self.data.append(a)
