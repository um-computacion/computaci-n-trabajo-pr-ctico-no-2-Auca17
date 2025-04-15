def is_palindrome(text):
    
    # Limpiar el texto (quitar espacios, puntuación y normalizar mayúsculas)
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    return cleaned_text == cleaned_text[::-1]