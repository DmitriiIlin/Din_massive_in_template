import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        # добавляем объект itm в позицию i, начиная с 0
        if i<0 or i>self.count:
            raise IndexError("Index is out of bounds")
        else:
            new_array=self.make_array(self.capacity)
            if self.count>=self.capacity:
                self.capacity=2*self.capacity
                self.resize(self.capacity)
                new_array=self.make_array(self.capacity) 
            if i==self.count:
                for j in range(self.count+1):
                    if j==i:
                        new_array[j]=itm 
                    else:
                        new_array[j]=self.array[j]
                self.array=new_array
                #print("вставка в конец")
            else:
                #print("вставка в начало-центр")
                for j in range(self.count+1):
                    if (i!=self.count) and (i==j):
                        new_array[j]=itm
                        for jj in range(j+1,self.count+1):
                            new_array[jj]=self.array[jj-1]
                        break
                    new_array[j]=self.array[j]
                self.array=new_array
        self.count+=1
        #print("self.capacity",self.capacity)
        #print("self.count",self.count)
    
    def delete(self, i):
        # удаляем объект в позиции i
        if i < 0 or i >=(self.count):
            raise IndexError('Index is out of bounds')
        else:
            if (2*(self.count-1))<self.capacity and (self.capacity)>16:
                new_capacity=int(self.capacity/(3/2))
               # print("Уменьшили в 1,5 раза", self.capacity,self.count)
            elif ((2)*(self.count-1))>=self.capacity and self.capacity>16:
                new_capacity=self.capacity 
               # print("Оставили как есть",self.capacity,self.count)   
            else:
               # print("Сделали 16",self.capacity,self.count)
                new_capacity=16
            new_array=self.make_array(new_capacity)
            for j in range(self.count-1):
                new_array[j]=self.array[j]
                if (j==i):
                    for jj in range(j,self.count-1):
                        new_array[jj]=self.array[jj+1]
                    break
        self.count-=1
        self.resize(new_capacity)
        self.array=new_array
        #print("self.capacity",self.capacity)
        #print("self.count",self.count)



#dy = DynArray()

#for t in range(1000):
 #   dy.insert(dy.count,t)
 #   print(dy.capacity,dy.count)
#print("$$$$")
#dy.delete(dy.count)
#try:
#    for i in range(1001): 
#        dy.delete(dy.count-1)
        #print(dy.capacity,dy.count)
#except Exception:
#    print("error")




