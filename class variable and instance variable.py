class Water:
    boiling_temperature = 100 # class variable
    freezing_temperature = 0 # class variable
    
    def __init__(self,temperature):
        self.temperature = temperature # instance variable
        
    def state(self):
        if self.temperature <= self.freezing_temperature:
            return 'solid'
        if self.freezing_temperature < self.temperature < self.boiling_temperature:
            return 'liquid'
        if self.temperature > self.boiling_temperature:
            return 'gas'
        

# if a user of your class uses a different temperature system (e.g., Fahrenheit), 
water = Water(temperature=20)
water.boiling_temperature = 212
water.freezing_temperature = 32
print(water.state())
