class polygon():
    def __init__(self,num_of_sides):
        self.num_of_sides = num_of_sides
       

class rectangle(polygon):
    def __init__(self,length,width,num_of_sides = 4):
        super().__init__(num_of_sides)
        self.length = length
        self.width = width
        
    def square (self):
        return self.length*self.width

rectang = rectangle(2,8)
print(rectang.square())

    
        
        
    