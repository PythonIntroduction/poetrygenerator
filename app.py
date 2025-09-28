from generator import generate_poem
from encryption import rotate_string

def main():
    do = input("Welcome to the poetry generator. What do you want to do?\n" \
    "Generate a new poem (enter g) or decrypt a poem (enter d)")

    if do == "g":
        print("Here is your poem:\n")
        poem = generate_poem()
        print(poem)
        shouldEncrypt = input("Do you want to encrypt the poem? Enter yes or no.")
        if shouldEncrypt == "yes":
            rotated_poem = rotate_string(poem)
            print("Here is your secret poem:")
            print(rotated_poem)
        else: 
            print("Okay, bye.")
    else:
        poem_string = input("Sure. Please enter the encrypted poem.\n")
        rotated_poem = rotate_string(poem_string)
        print("Here is your decrypted poem:")
        print(rotated_poem)

if __name__ == "__main__":
    main()