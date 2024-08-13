from PIL import Image

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)
    
    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)
    
    image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    image_path = r'E:\video\photo\test.jpg'
    encrypted_path = r'encrypted_image.jpg'
    decrypted_path = r'decrypted_image.jpg'
    key = 50

    print("Encrypting the image...")
    encrypt_image(image_path, encrypted_path, key)
    
    print("Decrypting the image...")
    decrypt_image(encrypted_path, decrypted_path, key)

if __name__ == "__main__":
    main()
