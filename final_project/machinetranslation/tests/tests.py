import unittest

from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Pepitoooo')
        self.assertNotEqual(english_to_french('Hello'), 'Ciao') 
        
class Test_french_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Ciao')
        
unittest.main()