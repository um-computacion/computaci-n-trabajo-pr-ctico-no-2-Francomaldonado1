import re 

def clean_text(word):    
    cleaned = re.sub(r'[^A-Za-z0-9]', '', word).lower()  
    return cleaned  

def is_palindrome(word):  
    cleaned = clean_text(word)  
    return cleaned == cleaned[::-1]  

def main():  

    user_input = input("Ingrese una palabra o frase: ")  
    if is_palindrome(user_input):  
        print("Es un palíndromo.")  
    else:  
        print("No es un palíndromo.")  

if __name__ == '__main__':  
    main()  