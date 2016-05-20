#! /usr/bin/env python3
maxLength = 63

class binList():

    def __init__(self):
        self.length = 0
        self.totalLength = 0
        self.data = 0
        self.nextdata = None

    def __str__(self):
        result = []
        for i in self:
            result.append(i)
        return str(result)

    def __iter__(self):
        return binListIter(self)

    def __len__(self):
        return self.totalLength

    def __getitem__(self,index):
        if self.totalLength <= index:
            raise IndexError("list index "+str(index)+" out of range")
        elif self.length <= index:
            return self.nextdata[index-self.length]
        else:
            return bool(self.data & 1<<index)

    def __setitem__(self,index,value):
        if self.totalLength < index:
            raise IndexError("list index out of range")
        elif self.totalLength == index:
            self.pushBack(value)
        elif (self.__getitem__(index) != value):
            if self.length <= index:
                self.nextdata.__setitem__(index-self.length,value)
            else:
                if value:
                    self.data += 1<<index
                else:
                    self.data -= 1<<index

    def __delitem__(self,index):
        if self.length <= index:
            raise IndexError("list index out of range")
        else:
            self.data = self.data % (1<<index) + int(self.data / (2<<(index+1))) * (1<<index)
            self.length -= 1
            self.totalLength -= 1

    def attachList(self):
        if self.nextdata is None:
            self.nextdata = binList()
        else:
            self.nextdata.attachList()

    def pushBack(self,value):
        if self.length <= maxLength:
            if value:
                self.data += (1<<self.length)
            self.length += 1
            self.totalLength += 1
        else:
            self.totalLength += 1
            if self.nextdata is None:
                self.attachList()
            self.nextdata.pushBack(value)

    def popFront(self):
        if self.length < 1:
            raise IndexError("list index out of range")
        else:
            result = __getitem__(0)
            self.data = (self.data >> 1)
            self.length -= 1
            self.totalLength -= 1
        return result

    def remItem(self,index):
        self.__delitem__(index)

    def append(self,index):
        self.pushBack(index)

class binListIter():
    def __init__(self,list):
        self.i = 0
        self.d = list

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.d):
            result = self.d[self.i]
            self.i += 1
            return result
        elif self.d.nextdata is not None:
            self.i = 0
            self.d = self.d.nextdata
            return self.__next__()
        else:
            raise StopIteration()
