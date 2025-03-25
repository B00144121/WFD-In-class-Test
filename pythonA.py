

#made the pet attributes like defined it more#
class Pet:
    def __init__(self, name, age, sex, pet_id, owner_name):
        self.name = name
        self.age = age
        self.sex = sex
        self.pet_id = pet_id
        self.owner_name = owner_name

   # All the info about pets are displayed here#
    def print_details(self):
        print("Pet Information:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Sex:", self.sex)
        print("Pet ID:", self.pet_id)
        print("Owner Name:", self.owner_name)

    # name chekced here and updates made#
    def update_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name

    def update_age(self, new_age):
        if isinstance(new_age, int):
            self.age = new_age

    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex

    def update_pet_id(self, new_id):
        if isinstance(new_id, int):
            self.pet_id = new_id

    def update_owner_name(self, new_owner_name):
        if isinstance(new_owner_name, str):
            self.owner_name = new_owner_name



class Dog(Pet):
    def __init__(self, name, age, sex, pet_id, owner_name, breed, is_vaccinated):
        super().__init__(name, age, sex, pet_id, owner_name)
        self.breed = breed
        self.is_vaccinated = is_vaccinated
#methods attemps to display the detials about the pet#
    def print_all_details(self):
        self.print_details()
        print("Breed:", self.breed)
        print("Vaccinated:", self.is_vaccinated)

    # A7: Update methods for new attributes
    def update_breed(self, new_breed):
        if isinstance(new_breed, str):
            self.breed = new_breed

    def update_vaccination_status(self, status):
        if isinstance(status, bool):
            self.is_vaccinated = status


# A8: Create instances
my_pet = Pet("Loki", 5, "Male", 1007, "Fuad")
my_dog = Dog("Buddy", 3, "Male", 2009, "Fuad", "Golden Retriever", True)

# A9: Call methods to print details
print("--- Pet Instance ---")
my_pet.print_details()

print("\n--- Dog Instance ---")
my_dog.print_all_details()

# A10: Demonstrate update methods with two examples for each class
print("\n--- Updating Attributes ---")
my_pet.update_name("Shadow")
my_pet.update_age(6)
print("Updated Pet:")
my_pet.print_details()



my_dog.update_breed("Labrador")
my_dog.update_vaccination_status(False)
print("\nUpdated Dog:")
my_dog.print_all_details()



