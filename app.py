from prettytable import PrettyTable
import sqlite3
#drone_explore

class Drone:
    def __init__(self, brand_name = None,  model_name = None):
            self.model_name = model_name
            self.brand_name = brand_name
    pass

    # FUNCTION CHECKS WHETHER THE brand_name exist in database

    def drone_brand(self):
        if str(self.brand_name) in dronesDB:
            print(f'{self.brand_name} is in Database')
        else:
            print(f'{self.brand_name} is not Database')


    pass

    # FUNCTION CHECKS WHETHER THE model_name exist in database
    def drone_model(self):
        model_name = dronesDB[self.brand_name]["model"]
        print(f'{dronesDB[self.brand_name]["model"]}')
    pass

    def display_model(self):
        count = 0
        print(f'Available models under {self.brand_name} ')
        for model in dronesDB:
            count += 1
            print(f'{count}. {model}')
            return model


    def checker(self):
        self.drone_brand()
        os.system('clear')
        self.drone_model()
        self.display_model()
        self.getinfo()
    pass

    def getinfo(self):
        os.system('cls')
        print(f'{self.model_name} is in Database')
        sleep(3)
        print(f'...............')
        print(f'This drone cost {dronesDB[str(self.brand_name)]["price"]}$\n'
              f'It can be used for {dronesDB[str(self.brand_name)]["applications"][0]},{dronesDB[str(self.brand_name)]["applications"][1]},{dronesDB[str(self.brand_name)]["applications"][2]}')
        print(f'---------------------------')
        print(f'Peoples review: {dronesDB[str(self.brand_name)]["review"]}')
        pass















# drone_B = str(input("Enter Drone Brand: "))
# drone_M = str(input("Enter Drone Model: "))
# Drone(drone_B,drone_M).drone_model()
# Drone(drone_B,drone_M).drone_brand()


# bame = "dji"
# if bame in dronesDB:
#     print("dronesDB")
# else:
#     print("error")
