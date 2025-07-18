class polygon:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self, *params):
        return self


class rectangle(polygon):

    def __init__(self,x,y,width,height):
        polygon.__init__(self,x,y)
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area
