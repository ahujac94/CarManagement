import os
from collections import namedtuple
from datetime import datetime

from services.car import CarService
from utility.logcfg import setup_logger
from utility.utils import HelperUtility


class CarException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Car:

    def __init__(self):
        self.helper = HelperUtility()
        config_yaml = os.path.join(os.path.abspath("."), "config", "config.yaml")
        self.yaml_data = self.helper.read_yaml_file(config_yaml)
        log_file = "Log" + "_" + datetime.now().strftime("%y_%m_%d_%H_%M_%S") + ".log"
        self.log = setup_logger(os.path.join(os.path.abspath("."), "log", log_file), self.yaml_data["log"][0],
                                self.yaml_data["log"][1])
        self.car_service = CarService()

    def user_inputs(self):
        """Method to take inputs from user while adding new car entry"""
        try:
            self.log.info(f"Taking inputs from user")
            name = input("Enter name of the car : ")
            company = input("Enter company name : ")
            status = (input("Enter status of the car : ") or "free")
            model = int(input("Enter model of the car : "))
            Car = namedtuple("Car", ["name", "company", "status", "model"])
            self.log.info(f"Successfully take the inputs from user {Car(name, company, status, model)}")
            return Car(name, company, status, model)
        except ValueError:
            print(f"Please enter valid values")
            self.log.error(f"Please enter valid values")
            return
        except Exception as exc:
            self.log.error(f"Error occurred while taking iputs from user {exc}")
            raise CarException(f"Error occurred while taking iputs from user {exc}")

    def display_menu(self):
        """Method to display the user menu"""
        self.log.debug(f"Displaying the menu")
        print("\nOperations")
        print \
            ("1.Add new record"
             "\n2.Display records"
             "\n3.Search Record with status"
             "\n4.Search Record with Chassis no"
             "\n5.Update Record using chassis no"
             "\n6.Exit")
        self.log.debug(f"Successfully displayed the menu")

    def run(self):
        try:
            while True:
                    self.display_menu()
                    ch = int(input("\nEnter choice (1,2,3,4,5,6): "))
                    self.log.info(f"User input is {ch}")
                    car_service = CarService()

                    # Adding new records
                    if ch == 1:
                        self.log.info(f"Adding new records")
                        car = self.user_inputs()
                        if car:
                            entry = car_service.add(name=car.name, status=car.status, model=car.model, company=car.company)
                            print(f"Successfully added car entry {entry}")
                            self.log.info(f"Successfully added car entry {entry}")
                        else:
                            continue

                    # Displaying new records
                    elif ch == 2:
                        self.log.info(f"Displaying records")
                        print(f"Displaying all cars: ")
                        all_cars = car_service.get_all_cars()
                        for car in all_cars:
                            car_service.display_car(car)
                        self.log.info(f"Successfully displayed the records")

                    # Search record with status
                    elif ch == 3:
                        try:
                            self.log.info(f"Searching record with the status")
                            status = input("Please enter the status: ")
                            response = car_service.search_with_status(status)
                            print(response)
                        except ValueError:
                            self.log.error(f"Please enter valid values")
                            continue

                    # Search record with chassis no
                    elif ch == 4:
                        try:
                            self.log.info(f"Searching record with the Chassis no")
                            chassis_no = input("Please enter the chassis no: ")
                            response = car_service.search_with_chassis_no(chassis_no)
                            print(response)
                        except ValueError:
                            self.log.error(f"Please enter valid values")
                            continue

                    # Updating the status using chassis no
                    elif ch == 5:
                        try:
                            self.log.info(f"Updating status of the car using Chassis no")
                            chassis_no = input("Please enter the chassis no: ")
                            status = input("Enter updated status")
                            response = car_service.update(chassis_no, status)
                            print(f"Successfully update the record : \n{response.json()}")
                        except ValueError:
                            self.log.error(f"Please enter valid values")
                            continue

                    else:
                        print("Thank you")
                        break
        # TODO: Need to remove broad exception
        except Exception as exc:
            raise CarException(f"Exception occurred {exc}")
