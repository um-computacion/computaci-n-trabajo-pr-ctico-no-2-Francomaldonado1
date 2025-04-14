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

if __name__ == '__main__':  
    unittest.main()  