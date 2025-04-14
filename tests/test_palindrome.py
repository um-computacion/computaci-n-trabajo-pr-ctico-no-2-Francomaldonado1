import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):  
    def test_simple_palindromes(self):  
        self.assertTrue(is_palindrome("madam"))  
        self.assertTrue(is_palindrome("racecar"))  
        self.assertTrue(is_palindrome("level"))  
        self.assertTrue(is_palindrome("neuquen"))  
        self.assertTrue(is_palindrome("rotor"))  
        self.assertTrue(is_palindrome("deified"))  
        self.assertTrue(is_palindrome("civic"))  
        self.assertTrue(is_palindrome("refer"))  
        self.assertTrue(is_palindrome("kayak"))  

class TestFrasesPalindromas(unittest.TestCase):  
    def test_frases_palindromas(self):  
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))  
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))  
        self.assertTrue(is_palindrome("No lemon, no melon."))  
        self.assertTrue(is_palindrome("Doc, note I dissent. A fast never prevents a fatness. I diet on cod."))  
        self.assertTrue(is_palindrome("Eva, can I see bees in a cave?"))  
        self.assertTrue(is_palindrome("Able was I ere I saw Elba."))  
        self.assertTrue(is_palindrome("Madam, in Eden, I'm Adam."))  
        self.assertTrue(is_palindrome("Step on no pets."))  
        self.assertTrue(is_palindrome("Mr. Owl ate my metal worm!"))  
        self.assertTrue(is_palindrome("A Santa at NASA."))  

class TestNoPalindromes(unittest.TestCase):
    def test_no_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))
        self.assertFalse(is_palindrome("hola mundo"))
        self.assertFalse(is_palindrome("palindrome"))
        self.assertFalse(is_palindrome("Mendoza"))
        self.assertFalse(is_palindrome("practicando TDD"))

class TestEdgeCases(unittest.TestCase):
    def test_edge_cases(self):  
        self.assertTrue(is_palindrome(""))            
        self.assertTrue(is_palindrome("a"))             
        self.assertTrue(is_palindrome("A"))             
        self.assertTrue(is_palindrome("aa"))         
        self.assertFalse(is_palindrome("ab"))           
        self.assertTrue(is_palindrome("   "))        
        self.assertTrue(is_palindrome(" A "))           
        self.assertTrue(is_palindrome(" Racecar "))
                        
if __name__ == '__main__':  
    unittest.main()  