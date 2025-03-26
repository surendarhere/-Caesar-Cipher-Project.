# Caesar Cipher Project

# caesar_cipher.py

def caesar_cipher(text, shift, mode="encrypt"):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.
    
    Parameters:
    text (str): The message to be encrypted or decrypted.
    shift (int): The number of positions to shift each letter.
    mode (str): "encrypt" or "decrypt".

    Returns:
    str: The encrypted or decrypted message.
    """
    result = ""

    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char  # Keep spaces, numbers, and symbols unchanged

    return result

if __name__ == "__main__":
    print("Welcome to the Caesar Cipher Encryption/Decryption Tool!")
    mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value (1-25): "))

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    else:
        output = caesar_cipher(message, shift_value, mode)
        print(f"\nResult: {output}")

