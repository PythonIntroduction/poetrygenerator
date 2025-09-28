import random

class Poem:
    EXAMPLE_NOUNS = ["flowers", "rain", "trees", "grass"]
    EXAMPLE_VERBS = ["bloom", "fall", "shake", "flow"]
    EXAMPLE_ADVERBS = ["happily", "angrily", "anxiously", "calmly"]

    def __init__(self, nouns, verbs, adverbs):
        self.nouns=nouns
        self.verbs=verbs
        self.adverbs=adverbs
    
    def __str__(self):
        return self.poem
    
    def generate(self):
        # Generate poem line by line
        poem=[]
        while self.nouns and self.verbs and self.adverbs:
            poem.append(self.get_poem_line(self.nouns, self.verbs, self.adverbs))
    
        # Transform the list into one string
        poem_string = "\n".join(poem)
        self.poem = poem_string

    def get_poem_line(self, nouns, verbs, adverbs): 
        sentence_structure = random.randint(0,1)

        noun = self.pick_one_of(nouns)
        verb = self.pick_one_of(verbs)
        adverb = self.pick_one_of(adverbs)

        if sentence_structure == 0: 
            return f"Let {noun} {verb} {adverb}."
        else:
            return f"Why would {noun} not {verb} {adverb}?"

    def pick_one_of(self, list):
        '''
        Select a random element from the list and before returning it,
        remove it from the list
        '''
        res = random.choice(list)
        list.remove(res)
        return res