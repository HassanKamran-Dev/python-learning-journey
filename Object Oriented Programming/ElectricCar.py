class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_name(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
    
    def read_odometer(self):
        print("This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles
    
    def fill_gas_tank(self):
        print("Filling the gas tank")

class Battery:
    def __init__(self,battery_size=70):
        self.btry_size = battery_size

    def get_batterysize(self):
        print(f"Battery size is {self.btry_size}")

    def get_range(self):
        range=0
        if self.btry_size == 70:
            range = 240
        elif self.btry_size == 85:
            range = 270
        print(f"This car can go {range} miles on full charge!")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar,self).__init__(make, model, year)
        self.battery = Battery(85)
    
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")

my_tesla = ElectricCar("Tesla","Model S",2016)

my_tesla.get_name()
my_tesla.fill_gas_tank()

my_tesla.battery.get_batterysize()
my_tesla.battery.get_range()