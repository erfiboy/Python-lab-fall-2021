import unittest
from set import Set


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        test_object = Set()
        test_object.add(2)
        test_object.add("golabi")
        test_object.add("ghamar")
        test_object.add("golam")
        expectedanswer = [2, "golabi", "ghamar", "golam"]
        self.assertEqual(expectedanswer, test_object.set)
        
    def test_delete(self):
        test_object = Set()
        test_object.add(2)
        test_object.add("golabi")
        test_object.add("ghamar")
        test_object.add("golam")
        test_object.delete("golabi")
        expectedanswer = [2, "ghamar", "golam"]
        self.assertEqual(expectedanswer, test_object.set)
        
    def test_equal(self):
        test_object = Set()
        test_object.add(2)
        test_object.add("golabi")
        test_object.add("ghamar")
        test_object.add("golam")
        
        test_object1 = Set()
        test_object1.add(2)
        test_object1.add("golabi")
        test_object1.add("ghamar")
        test_object1.add("golam")
        
        self.assertTrue(test_object1 == test_object)
        
    def test_equal1(self):
        test_object = Set()
        test_object.add(2)
        test_object.add("golabi")
        test_object.add("ghamar")
        test_object.add("golam")
        
        test_object1 = Set()
        test_object1.add(2)
        test_object1.add("ghamar")
        test_object1.add("golam")
        
        self.assertFalse(test_object1 == test_object)
            
    def test_union(self):
        test_object = Set()
        test_object.add(2)
        test_object.add("golabi")

        test_object1 = Set()
        test_object1.add("ghamar")
        test_object1.add("golam")
        
        answer = test_object | test_object1
        expectedanswer = [2, "golabi", "ghamar", "golam"]
        
        self.assertEqual(answer, expectedanswer)  

    def test_join(self):
        test_object = Set()
        test_object.add(2)
        test_object.add("golabi")

        
        test_object1 = Set()
        test_object1.add("ghamar")
        test_object1.add("golabi")
        
        answer = test_object & test_object1
        expectedanswer = ["golabi"]
        
        self.assertEqual(answer, expectedanswer)  

    def test_join1(self):
        test_object = Set()
        test_object.add(2)
        test_object.add("golabi")

        
        test_object1 = Set()
        test_object1.add("ghamar")
        test_object1.add("golabi")
        
        answer = test_object & test_object1
        expectedanswer = ["ghamar"]
        
        self.assertNotEqual(answer, expectedanswer) 
        

if __name__ == '__main__':
    unittest.main()