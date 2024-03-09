import ctypes


class MyList:
    
    def __init__(self) -> None:
        
        self.size = 1
        self.n = 0
        
        # create a ctype array with size=self.size()
        self.A = self.__make_array(self.size)
        
    #magic method
    def __len__(self):
        return (self.n)
    
    def append(self,item):
        
        #checks if the list is full. Sizeindicates the total size of the objects and n indicates the total elements in the list
        if self.n == self.size :
            self.__resize(self.size * 2)
        
        #if not, then append/add the item at the nth location
        self.A[self.n] = item
        self.n = self.n + 1
    
    def __resize(self,new_capacity):
        #create a new array with newcapacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        
        #copy elements from olf array to new array with bigger size, copy array A to B
        for i in range(self.n):
            B[i] = self.A[i]
            #reassign B to A
        self.A = B
            
    #magic method to print the elements of the list
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    #magic code to return the item at the index
    def __getitem__(self,item):
        #check if the mentioned item is within the rang
        if 0<= item <= self.size:
            return self.A[item]
        else:
            return "Index out of range"
    
    # code to implement POP 
    def pop(self):
        if self.n == 0:
            return 'Empty list'
        print(self.A[self.n-1])
        self.n = self.n-1
        
    #code to clear the list
    def clear(self):
        self.size = 1
        self.n = 0    
        
    #find the element  
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
              return i
        return "Value Error"   
    
    def insert(self,item,position):
        if self.n == self.size:
            self.__resize
        
        for i in range(self.n,position,-1):
            self.A[i] = self.A[i-1]
        
        self.A[position]     = item
        self.n = self.n + 1
        
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
L = MyList()
L.append(3)
L.append("hello")
L.append("bye")
L.append("tata")
L.append("toodles")
L.insert(200,3)


print(len(L))
print(L)
print(L[2])
L.pop()
print(L)
print(L.find("hello"))
