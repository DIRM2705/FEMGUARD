import datetime

class UserData:
    def __init__(self, name : str, birthdate : datetime.date, phone_number : str, blood_type : str, height : int, weight : float, allergies : str, emergency_contacts : list[str]):
        self.name = name
        self.birthdate = birthdate
        self.phone_number = phone_number
        self.blood_type = blood_type
        self.height = height
        self.weigth = weight
        self.allergies = allergies
        self.emergency_contacts = emergency_contacts
        