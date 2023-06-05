import math 
class Balloon:
    global pi
    pi = 3.14115926535
    def __init__(self, a, c, d, k) -> None:
        self.a = a
        self.c = c
        self.d = d
        self.k = k
        
    def get_y(self, x):
        sin_parameter = (pi * x  + self.c) / (11 + self.d)
        return (self.a * x * math.sin(sin_parameter)) + self.k
    
    def get_derivative(self, x):
        denominator = (11 + self.d)
        parameter = (pi * x + self.c) / denominator
        unscaled_value = ((pi * x * math.cos(parameter)) / denominator) + math.sin(parameter)
        return self.a * unscaled_value
    
    def get_arc_length(self, a, b, scale):
        total_accumulated_length = 0
        while(a < b):
            total_accumulated_length += math.sqrt(1 + (self.get_derivative(a) * self.get_derivative(a))) * scale
            a += scale
        
        return total_accumulated_length
    
    def get_width(self, x):
        return (2 * pi * self.get_y(x) / 8)
    
    def get_everything(self):
        y = []
        circumference = []
        widths = []
        arc_length = []
        for i in range(0, 12):
            widths.append(self.get_width(i))
            y.append(self.get_y(i))
            circumference.append(self.get_y(i) * pi * 2)
            if(i != 11):
                arc_length.append(self.get_arc_length(i, i + 1, 0.00001))
       

    
     
    

newThing = Balloon(0.79, 1, 0, 1.3)
print(newThing.get_arc_length(0, 11.198, 0.00001) * 3)
