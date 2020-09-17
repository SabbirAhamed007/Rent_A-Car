import sys

class Rent_A_Car:
    def __init__(self, list_of_cars):  #this init method is the first method to be invoked when you create an object
        # what attributes does a Rent A Car in general have? - for now, let's abstract and just say it has availablebooks (we're not going to program the shelves, and walls in!)
        self.availbale_cars = list_of_cars

    def display_Available_car(self):
        print("The cars we have for rent are as follows:")
        print("============================")
        for car in self.availbale_cars:
            print(car)

    def lend_Car(self, requestedCar):
        if requestedCar in self.availbale_cars:
            print("The car you requested has now been rented")
            self.availbale_cars.remove(requestedCar)
        else:
            print("Sorry the car you have requested is currently not in the available")

    def addCar(self, returnedCar):
        self.availbale_cars.append(returnedCar)
        print("Thank you for renting our car. You are most welcome")

class Customer:
    def requestCar(self):
        print("Select the car from available car list>>")
        self.car= input()
        return self.car

    def returnCar(self):
        print("Enter the name of the car you'd like to return>>")
        self.car = input()
        return self.car

def main():
    rent_a_car = Rent_A_Car(["Sentra", "Altima", "Maxima", "Murano", "Pathfinder", "Civic", "Accord", "CRV", "Pilot", "Odyssey", "Corolla", "Camry", "Rav4", "Highlander", "BMW 330", "BMW 540", "BMW 740", "X3", "X5", "Mercedes-Benz C", "Mercedes-Benz E", "Mercedes-Benz S", "Mercedes-Benz ML", "Mercedes-Benz GL", "Audi A4", "Audi A6", "Audi A8", "Audi Q5", "Audi Q7"])
    customer = Customer()
    done = False
    while done == False:
        print("""=====List Of Available Cars====="
             1. Display all availbale cars
             2. Request a car
             3. Return a car
             4. Exit
              """)

        choice = int(input("Enter Choice:"))
        if choice == 1:
            rent_a_car.display_Available_car()
        elif choice == 2:
            rent_a_car.lend_Car(customer.requestCar())
        elif choice == 3:
            rent_a_car.addCar(customer.returnCar())
        elif choice == 4:
            sys.exit()
main()