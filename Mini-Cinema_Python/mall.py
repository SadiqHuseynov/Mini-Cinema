from datetime import datetime, time


class Mall:
    def __init__(self,location,floor,hall_count):
        self.location = location
        self.floor = floor
        self.hall_count = hall_count
        
    def working_time(self):
        self.current_time = datetime.now().time()
        self.open = time(10,00)
        self.close = time(23,00)
        
        if self.current_time > self.close or self.current_time < self.open:
            exit("Mall is closed!")
        else:
            return "Mall is open"
    
    def age(self,age_val):
        try:
            self.age_val = int(age_val)
            
            if self.age_val < 14:
                exit("Only those aged 14 and over can enter!")
                
        except ValueError:
            exit("Enter valid value")

    def vaccination(self, vaccinated):
        self.vaccinated = vaccinated

        if self.vaccinated == "Active":
            return "You are vaccinated"
        else:
            exit("Only those who have been vaccinated can enter!")

    def info(self):
        return """
1. Deniz_Mall
2. Ganjlik_Mall
3. Ganja_Mall
4. 28_Mall
5. Port_Baku_Mall"""             

class Deniz_Mall(Mall):
    pass

class Ganjlik_Mall(Mall):
    pass

class Ganja_Mall(Mall):
    pass

class Mall_28(Mall):
    pass

class Port_Baku_Mall(Mall):
    pass
