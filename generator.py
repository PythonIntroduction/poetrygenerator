import random

def get_poem_line(nouns, verbs, adverbs): 
    return f"Let {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)}"

def main():
    nouns=["flowers", "rain", "trees", "grass"]
    verbs=["bloom", "fall", "shake", "flow"]
    adverbs=["happily", "angrily", "anxiously", "calmly"]

    # Generate poem line by line
    poem=[]
    for i in range(0,5):
        poem.append(get_poem_line(nouns, verbs, adverbs))
    
    # Print out poem line by line
    for line in poem:
        print(line)

if __name__ == "__main__":
    main()