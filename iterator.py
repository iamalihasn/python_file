class My_count:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.start < self.end:
            val = self.start
            self.start += 1
            return val
        else:
            raise StopIteration


class My_range:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return My_count(self.start,self.end)

c = My_range(1,20)

for i in c:
    print(i)

for i in c:
    print(i)