from drones import Drone

fuel = 18
max_speed = 60
refuel_quantity = 15
drone= Drone(fuel, max_speed)
###
print("Current fuel is "+str(drone.get_fuel()))
print("Current speed is "+str(drone.get_speed()))
drone.add_fuel(refuel_quantity)
print("Now the fuel is "+str(drone.get_fuel()))
drone.set_speed(55)
print("Current speed is "+str(drone.get_speed()))
drone.fly()
