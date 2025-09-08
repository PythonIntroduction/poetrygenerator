import random


def main():
    print("Hello world!")
    print("Let flowers bloom happily.")

    nouns=["flowers", "rain", "trees", "grass"]
    verbs=["bloom", "fall", "shake", "flow"]
    adverbs=["happily", "angrily", "anxiously", "calmly"]

    print(nouns)
    print(verbs)
    print(adverbs)

    print(random.choice(nouns))
    print(random.choice(verbs))
    print(random.choice(adverbs))

if __name__ == "__main__":
    main()