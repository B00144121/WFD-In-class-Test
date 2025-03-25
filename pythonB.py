import unittest

#structure of a test file#

#The start of creating the test class
class Pet:
    def __init__(self, name, age, sex, petID, owner_name):
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID
        self.owner_name = owner_name

    def update_name(self, new_name):
        self.name = new_name

    def update_age(self, new_age):
        self.age = new_age

    def update_sex(self, new_sex):
        self.sex = new_sex

    def update_petID(self, new_petID):
        self.petID = new_petID

    def update_owner_name(self, new_owner_name):
        self.owner_name = new_owner_name


# Test if this object actually belongs to the test class#
class TestIsInstance(unittest.TestCase):
    def test_is_instance(self):
        pet = Pet("Max", 3, "Male", "P123", "Fuad")
        self.assertIsInstance(pet, Pet)


#checks if the object does not belong to this test class#
class TestIsNotInstance(unittest.TestCase):
    def test_is_not_instance(self):
        pet = Pet("Luna", 2, "Female", "P456", "Ali")
        self.assertNotIsInstance(pet, str)


# Test if the two objects are the same#
#pet 1 and pet 2 are used in this case#
class TestObjectIdentity(unittest.TestCase):
    def test_objects_are_same(self):
        pet1 = Pet("Bella", 4, "Female", "P789", "Sara")
        pet2 = pet1
        self.assertIs(pet1, pet2)
#Then tests if the objects are different#
    def test_objects_are_different(self):
        pet1 = Pet("Bella", 4, "Female", "P789", "Sara")
        pet2 = Pet("Bella", 4, "Female", "P789", "Sara")
        self.assertIsNot(pet1, pet2)


# Test the update methods with variables such as self.pet#
class TestUpdateMethods(unittest.TestCase):
    def setUp(self):
        self.pet = Pet("Rocky", 5, "Male", "P101", "John")
## fucntions used are test update name, test update age and test update sex and more#
    def test_update_name(self):
        self.pet.update_name("Buddy")
        self.assertEqual(self.pet.name, "Buddy")

    def test_update_age(self):
        self.pet.update_age(6)
        self.assertEqual(self.pet.age, 6)

    def test_update_sex(self):
        self.pet.update_sex("Female")
        self.assertEqual(self.pet.sex, "Female")

    def test_update_petID(self):
        self.pet.update_petID("P202")
        self.assertEqual(self.pet.petID, "P202")

    def test_update_owner_name(self):
        self.pet.update_owner_name("Jane")
        self.assertEqual(self.pet.owner_name, "Jane")

#main functions to run the test in the first place
if __name__ == '__main__':
    unittest.main()
