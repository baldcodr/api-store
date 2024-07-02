from api.store.schema import Person
import unittest


class SchemaValidationTest(unittest.TestCase):
    def test_schema_generator_works(self):
        person = Person("tf122324","John","Doe","email@email.com",25,{'zip': 'LL12 TW0', 'state': 'Manchester', 'city': 'Lagos', 'street': 'London'})
        expected = {
            'last_name': 'Doe', 
            'first_name': 'John', 
            'email': 'email@email.com', 
            'id': 'tf122324', 
            'age': 25, 
            'address': {
                'zip': 'LL12 TW0', 
                'state': 'Manchester', 
                'city': 'Lagos', 
                'street': 'London'
                }}
        self.assertEqual(person.to_dict(), expected)

if __name__ == '__main__':
    unittest.main()