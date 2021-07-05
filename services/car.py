""" Car module having all its information """
import logging
from typing import List, Optional
from uuid import UUID, uuid1

from models.car import Car, Status


class CarService:

    # Added two static entry
    car_records: List[Car] = [Car(name="Creta", company="Hyundai", model=2021, status="free",
                                  chassis_no="54cf2c55-da95-11eb-9652-d89c67b7662e"),
                              Car(name="Harrier", company="TATA", model=2021, status="reserved",
                                  chassis_no="55cf2c56-da95-11eb-9652-d89c77c7662e")
                              ]

    def __init__(self):
        self.log = logging.getLogger(__name__)

    def search_with_chassis_no(self, chassis_no: str):
        """
        Method to search the car record with its chassis no
        Args:
            chassis_no: Chassis no of the car, which is the unique identity of the car

        Returns:

        """
        if len(CarService.car_records) > 0:
            for record in CarService.car_records:
                if str(record.chassis_no) == chassis_no:
                    return record.json()
        return "No records found"

    def search_with_status(self, status: str):
        """
        Method to search the car record with its status
        Args:
            status: Status of the car, possible values are free/reserved
        Returns:

        """
        if len(CarService.car_records) > 0:
            return [record for record in CarService.car_records if record.status.lower() == status.lower()]
        return f"No records found with the given status {status}"

    def get_all_cars(self):
        return CarService.car_records

    def display_car(self, car: Car):
        """
        Method to display the car information
        Args:
            car: Car object having all the car info
        """
        print("Car Name : ", car.name)
        print("Company Name : ", car.company)
        print("Status : ", car.status.value)
        print("Model : ", car.model)
        print("Chassis No. : ", car.chassis_no)
        print("\n")

    def add(self, name: str, company: str, status: str, chassis_no: Optional[UUID] = None, model: int = 2021):
        """
        Method to add the new record
        Args:
            name: Car name
            company: Company name
            status: Status of the car
            chassis_no: Chassis no. of the car
            model: Year of manufacture
        Returns:

        """
        if chassis_no is None:
            chassis_no = uuid1()
        car_entry = Car(name=f"{name}", company=f"{company}",
                        model=model, status=status.lower(),
                        chassis_no=f"{chassis_no}")
        # Adding record into the list
        CarService.car_records.append(car_entry)
        return car_entry

    def delete(self, chassis_no: str):
        """
        Method to delete the record
        Args:
            chassis_no: Chassis no of the car which needs to be delete
        Returns:
            Message to tell the user whether the request is successful or not
        """
        if len(CarService.car_records) > 0:
            for record in CarService.car_records:
                if str(record.chassis_no) == chassis_no:
                    # Removing element from the list
                    CarService.car_records.remove(record)
                    return f"Successfully delete the record with chassis no {chassis_no}"
        return "No records found to delete"

    def update(self, chassis_no, status: str):
        """
        Method to update the status using chassis no
        Args:
            chassis_no: Unique no of an car engine
            status: Status of the car, Either it can be reserved or free
        Returns:
            Update Record
        """
        u_record = None
        for record in CarService.car_records:
            if str(record.chassis_no) == str(chassis_no):
                record.status = Status.reserved if status == "reserved" else Status.free
                u_record = record
                break
        return u_record



