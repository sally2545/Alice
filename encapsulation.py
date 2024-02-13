class Bike:
    def __init__(self) -> None:
        self._maximumspeed = 180

    def drive(self) -> None:
        print(f"Maximum speed is {self._maximumspeed}.")

#maxspeed is 180
blackbike = Bike()
blackbike.drive()

#maxspeed is 15
blackbike._maximumspeed = 15
blackbike.drive()





