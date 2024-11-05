import os
from time import sleep
# from tabulate import tabulate
from mongo_connection import MongoConnection


class Drone:
    def __init__(self, drone_model:str):
        # self.drone_brand = drone_brand
        self.drone_model = drone_model
    pass

    def checkdrone_model(self):
        modeldb = dronesDB.copy()
        # condition to check whether the drone is in the database
        if self.drone_model in modeldb:
            sleep(3)
            print("Wait a second....")
            sleep(2)
            print("Printing out info on Drone")
            sleep(3)
            os.system('cls')
            sleep(2)
            self.getinfo()

        else:
            os.system('cls')
            print("Enter a valid drone Model")
            print(f'Available Drone Model are: ')
            for model in modeldb:
                sleep(1)
                print(f'{">."} {model}')
        pass

    def getinfo(self):  #get information of specific drone model
        os.system('cls')
        sleep(3)

    pass

    def program(self):  #main program running all other methods/funtions in the class
        self.checkdrone_model()
        pass


class Compare(Drone):
    def __init__(self, model1: str, model2: str, drone_model):
        super().__init__(drone_model)
        self.model1 = model1
        self.model2 = model2

    pass

    def compare_models(self):
        col_names = dronesDB[self.model1][0]["brand"]
        brand_model1 = dronesDB[self.model1][0]["brand"]
        data = [["Mavs", 99], ["Suns", 91], ["Spurs", 94], ["Nets", 88]]
        print(tabulate(data, headers=col_names, tablefmt="grid"))
        pass


def main():
    """Drives the program interaction."""
    print(f'{MongoConnection()}')
    while True:
        user_input = input(
            "What would you like to learn about drones? (models, compare, or quit) : ").lower()
        if user_input == "models" or user_input == "m":
            drone_model = input("Enter Drone Model: ")
            print(Drone(drone_model).program())
        elif user_input == "compare" or user_input == "c":
            model1 = input("Enter the first model name: ").lower()
            model2 = input("Enter the second model name: ").lower()
            Compare(model1, model2).compare_models()
        elif user_input == "quit":
            os.system("cls")
            print("Thank you for using Drone Explore")
            break
        else:
            print("Invalid input. Please try again.")
    pass

if __name__ == "__main__":
    main()



'''ignore'''
# print(f'......................................................')
# print(f'This drone was developed by {dronesDB[self.drone_model][0]["brand"]}'
#       f' also {self.drone_model} cost about ${dronesDB[self.drone_model][0]["price"]} \n'
#       f'{self.drone_model} has specs of 1.Camera:{dronesDB[self.drone_model][0]["specs"]["camera"]} '
#       f' 2.Flight time:{dronesDB[self.drone_model][0]["specs"]["flight_time"]} '
#       f' 3.Range:{dronesDB[self.drone_model][0]["specs"]["range"]} \n'
#       f'Its has its applications, which are: 1.{dronesDB[self.drone_model][0]["applications"][0]}'
#       f' 2.{dronesDB[self.drone_model][0]["applications"][1]} , 3.{dronesDB[self.drone_model][0]["applications"][2]}\n'
#       f'........................................................................ \n'
#       f'What people have to say about the product: {dronesDB[self.drone_model][0]["review"]} \n'
#       f'Link : {dronesDB[self.drone_model][0]["link"]} \n'
#       f'          \n'
#       f'Thank You for Reading')