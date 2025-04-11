class Heap():
    def __init__(self):
        self.heap=[]

    def create_heap(self , data_list):
        for i in data_list:
            self.insert(i)

    def insert(self, data):
        index = len(self.heap)
        parentIndex = (index-1)//2
        while index>0 and self.heap[parentIndex]<data:
            if index==len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            
            index = parentIndex
            parentIndex=(index-1)//2
        if index==len(self.heap):
            self.heap.append(data)
        else:
            self.heap[index]=data

    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap(0)
    
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap)==1:
            return self.heap.pop()
        max_value = self.heap[0]
        temp=self.heap.pop()
        index=0
        leftChildIndex = 2*index+1
        rightChildIndex = 2*index+2

        while leftChildIndex<len(self.heap):
            if rightChildIndex<len(self.heap):
                if self.heap[leftChildIndex]>self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex]>temp:
                        self.heap[index]= self.heap[leftChildIndex]
                        index=leftChildIndex
                    else:
                        break
                else:
                    if self.heap[rightChildIndex]>temp:
                        self.heap[index] = self.heap[rightChildIndex]
                        index= rightChildIndex
                    else:
                        break
            else:
                if self.heap[leftChildIndex]>temp:
                        self.heap[index] = self.heap[leftChildIndex]
                        index= leftChildIndex
                else:
                    break
            leftChildIndex = 2*index+1
            rightChildIndex = 2*index+2
        self.heap[index] = temp
        return max_value
    def heapSort(self,data_list):
        self.create_heap(data_list)
        data_list_2= []
        try:
            while True:
                data_list_2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return data_list_2


class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg = msg
    def __str__(self):
        return self.msg
drive_list = [44,26,23,89,54,67,39,10]
h = Heap()
result = h.heapSort(drive_list)
print(result)#[10, 23, 26, 39, 44, 54, 67, 89]