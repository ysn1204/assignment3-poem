import random

def generate_poem(word):
    # Randomly select some vocabulary to construct the three-line poem
    descriptors = ["beautiful", "twinkling", "aching", "lonely", "warm"]
    actions = ["dancing in the night sky", "like a breeze brushing by", "as if time stands still", "shining like the stars"]
    feelings = ["makes my heart flutter", "brings endless longing", "stirs in my heart", "fills me with tenderness"]

    # Generate three lines
    line1 = f"{descriptors[random.randint(0, len(descriptors)-1)]} {word},"
    line2 = f"{actions[random.randint(0, len(actions)-1)]},"
    line3 = f"{feelings[random.randint(0, len(feelings)-1)]}."

    return line1 + " " + line2 + " " + line3

# Prompt the user to input a word
input_word = input("Please enter a word: ")
poem = generate_poem(input_word)
print(" Generated three-line poem:")
print(poem)