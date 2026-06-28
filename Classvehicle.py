class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modeIX = Vehicle(240, 10)
print("Model Max Speed,", modeIX.max_speed)
print("Model Mileage", modeIX.mileage)