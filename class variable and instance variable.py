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


******************************************************************************************************************************************************

class Matter:
    boiling_temperature = None
    freezing_temperature = None

    def __init__(self, temperature):
        self.temperature = temperature

    def state(self):
        if self.temperature <= self.freezing_temperature:
            return 'solid'
        elif self.freezing_temperature < self.temperature < self.boiling_temperature:
            return 'liquid'
        else:
            return 'gas'


class Water(Matter):
    boiling_temperature = 100
    freezing_temperature = 0


class Mercury(Matter):
    boiling_temperature = 356.7
    freezing_temperature = -38.83
