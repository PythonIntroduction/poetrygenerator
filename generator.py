import random
import string

LOOKUP_TABLE = string.ascii_letters + ".,!? \n"

def pick_one_of(list):
    '''
    Select a random element from the list and before returning it,
    remove it from the list
    '''
    res = random.choice(list)
    list.remove(res)
    return res

def get_poem_line(nouns, verbs, adverbs): 
    sentence_structure = random.randint(0,1)

    noun = pick_one_of(nouns)
    verb = pick_one_of(verbs)
    adverb = pick_one_of(adverbs)

    if sentence_structure == 0: 
        return f"Let {noun} {verb} {adverb}."
    else:
        return f"Why would {noun} not {verb} {adverb}?"

def rotate_character(character):
    current_position = LOOKUP_TABLE.index(character)
    rotate_by = len(LOOKUP_TABLE) // 2 #Floor division
    next_position = (current_position + rotate_by) % len(LOOKUP_TABLE)
    return LOOKUP_TABLE[next_position]

def rotate_string(string):
    rotated_string = ""
    for character in string:
        rotated_string += rotate_character(character)
    return rotated_string

def generate_poem():
    nouns=["flowers", "rain", "trees", "grass"]
    verbs=["bloom", "fall", "shake", "flow"]
    adverbs=["happily", "angrily", "anxiously", "calmly"]

    # Generate poem line by line
    poem=[]
    while nouns and verbs and adverbs:
        poem.append(get_poem_line(nouns, verbs, adverbs))
    
    # Transform the list into one string
    return "\n".join(poem)