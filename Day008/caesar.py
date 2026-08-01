import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
running = True

print(art.logo)

def encrypt(original_text, shift):
    new_text = ""

    for letter in original_text:
        if letter not in alphabet:
            new_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift

            if shifted_position > 25:
                shifted_position = shifted_position - 26
                # shifted_position %= len(alphabet) 0-25
                new_text += alphabet[shifted_position]
            else:
                new_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {new_text}")


def decrypt(original_text, shift):
    new_text = ""

    for letter in original_text:
        if letter not in alphabet:
            new_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift

            if shifted_position < 0:
                shifted_position = shifted_position + 26
                new_text += alphabet[shifted_position]
            else:
                new_text += alphabet[shifted_position]

    print(f"Here is the decrypted result: {new_text}")


while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if direction == "decode":
        print("\nDecrypting...")
        decrypt(text, shift)
    else:
        print("\nEncrypting...")
        encrypt(text, shift)

    should_continue = input("\nDo you want to continue? Yes or no: ").lower()
    if should_continue[0] == "n":
        print("Closing...")
        running = False

'''def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the result: {output_text}")'''
