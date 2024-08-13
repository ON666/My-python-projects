def caesar_cipher(text, shift, mode='encrypt'):
    result = []
    shift = shift % 26  
    if mode == 'decrypt':
        shift = -shift 
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

def main():
    print("Caesar Cipher Encryption/Decryption")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    
    if mode not in ('encrypt', 'decrypt'):
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return
    result = caesar_cipher(message, shift, mode)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
