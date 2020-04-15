"""
Create a class called Car.
- It should have a method to
   - reset its odometer reading,
   - set its mileage and
   - set its fuel tank capacity.

Create an object of this Car class and perform the following steps.

Prompt the user to set the mileage and fuel tank capacity of the car.
Then ask the user to enter the odometer reading at the end his travel.
Store these values in the Car object created above.

Read the values from the Car object and
   - find out the distance travelled
   - the number of stops they had to make for re-fuelling the car.
"""
def get_user_inputs():
    mil = int(input("Please enter the car's mileage : "))
    cap = int(input("Please enter the car's tank capacity : "))
    return (mil), (cap)


def get_odo_reading():
    first = -1
    answer = input("Did you reset the odometer at the start of journey ?").lower()
    if answer == "no":
        first = int(input("Please enter starting odometer reading : "))
    # Ask for the starting value of odometer, only if the user says "No" for
    # the above question
    last = int(input("Please enter the final100 odometer reading : "))
    return first, last


class Car:
    def reset_odometer(self, value=0):
        """ This method should set the starting value of odometer
            By default, this value is set to zero
        """
        self.start = value

    def set_mileage(self, value):
        """ This method should set the mileage of the car
        """
        self.mileage = value

    def set_tank_capacity(self, value):
        """ This method should set the tank capacity of the car
        """
        self.capacity = value

    def set_last_reading(self, value):
        """ This method should set the ending value of odometer
        """
        self.final = value

    def find_distance(self):
        """ This method should calculate the distance travelled
            based on the starting and ending values of odometer
            Note : This method, does not take any inputs
            Return : The distance travelled
        """
        self.distance_traveled = self.final - self.start
        return self.distance_traveled

    def find_stops(self):
        """ This method should calculate the number of stops
            required for refuelling the car based on its
            mileage, tank capacity and distance travelled
            Note : This method, does not take any inputs
            Return : The number of stops for refuelling [int]
        """
        self.dist_without_refuel = self.capacity*self.mileage
        self.no_of_stops_req = self.distance_traveled//self.dist_without_refuel
        return self.no_of_stops_req

# Main starts from below
zen = Car()
mileage, tank_capacity = get_user_inputs()
zen.set_mileage(mileage)
zen.set_tank_capacity(tank_capacity)

start, finish = get_odo_reading()
if start < 0:
    zen.reset_odometer()
else:
    zen.reset_odometer(start)

zen.set_last_reading(finish)

print ("Distance travelled : ", zen.find_distance())
print ("No.of stops for refuelling", zen.find_stops())
