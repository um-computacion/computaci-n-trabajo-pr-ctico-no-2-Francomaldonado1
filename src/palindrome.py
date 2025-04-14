import re 
def is_palindrome(word):  
    pass 
def clean_text(word):    
    cleaned = re.sub(r'[^A-Za-z0-9]', '', word).lower()  
    return cleaned  