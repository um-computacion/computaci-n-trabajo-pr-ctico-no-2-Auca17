def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    try:
        while True:
            text = input("Ingrese una palabra o frase: ")
            if is_palindrome(text):
                print(f'"{text}" es un palíndromo')
            else:
                print(f'"{text}" no es un palíndromo')
    except KeyboardInterrupt:
        print("\nPrograma finalizado")